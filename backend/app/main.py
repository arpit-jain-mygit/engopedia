"""Word Wizard API: FastAPI routes. Mangum wraps the app for AWS Lambda."""
import random
from typing import Optional

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel, Field

from . import cambridge, content, game, shop, wm_tests
from .store import make_store

CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # no 0/O or 1/I/L, easy to read aloud


class NewPlayer(BaseModel):
    name: str = Field(min_length=1, max_length=16)


class ShopItemIn(BaseModel):
    item_id: str = Field(min_length=1, max_length=40)


class WmAnswerIn(BaseModel):
    chapter: int
    question_id: str = Field(min_length=1, max_length=40)
    choice: int = Field(ge=0, le=3)


class WmTestAnswerIn(BaseModel):
    id: str = Field(min_length=1, max_length=80)
    answer: str = Field(default="", max_length=300)


class WmGradeIn(BaseModel):
    items: list[WmTestAnswerIn] = Field(max_length=50)


class AnswerIn(BaseModel):
    root: str
    question_id: str
    choice: Optional[int] = Field(default=None, ge=0, le=3)   # choice-style formats and two-step
    text: Optional[str] = Field(default=None, max_length=40)  # build and type formats
    pairs: Optional[list[str]] = Field(default=None, max_length=8)  # match format, right side in left order


def create_app(store=None):
    store = store or make_store()
    app = FastAPI(title="Word Wizard API", version="1.0.0")

    def new_code():
        for _ in range(20):
            code = "".join(random.choice(CODE_ALPHABET) for _ in range(6))
            if not store.code_exists(code):
                return code
        raise HTTPException(status_code=503, detail="Could not create a player code, please try again")

    def load_player(code):
        player = store.get(f"PLAYER#{code.upper()}", "PROFILE")
        if not player:
            raise HTTPException(status_code=404, detail="Player code not found")
        return player

    def level_state(code):
        """Return {root: level item} for every level this player has touched."""
        items = store.query_prefix(f"PLAYER#{code}", "LEVEL#")
        return {i["root"]: i for i in items}

    def is_unlocked(index, progress):
        if index == 0:
            return True
        previous = content.levels()[index - 1]["root"]
        return bool(progress.get(previous, {}).get("completed"))

    def wrong_reason(question, body):
        """The reason for the option the child picked; the general tip when there is none."""
        reasons = question.get("reasons") or []
        if body.choice is not None and 0 <= body.choice < len(reasons):
            return reasons[body.choice]
        return question["try"]

    def profile_view(player):
        progress = level_state(player["code"])
        levels = []
        for i, lv in enumerate(content.levels()):
            state = progress.get(lv["root"], {})
            levels.append({
                **lv,
                "unlocked": is_unlocked(i, progress),
                "completed": bool(state.get("completed")),
                "stars": state.get("stars", 0),
            })
        return {
            "code": player["code"],
            "name": player["name"],
            "points": player.get("points", 0),
            "candies": player.get("candies", 0),
            "streak": player.get("streak", 0),
            "owned": player.get("owned", []),
            "equipped": player.get("equipped", {}),
            "levels": levels,
        }

    @app.get("/api/health")
    def health():
        return {"ok": True}

    @app.get("/api/roots")
    def roots():
        return {"levels": content.levels()}

    @app.get("/api/roots/{root}/words")
    def root_words(root: str):
        if content.level_index(root) is None:
            raise HTTPException(status_code=404, detail="Unknown root")
        meaning = content.morphemes()[root]["meaning"]
        return {"root": root, "meaning": meaning, "cards": content.learn_cards(root)}

    @app.post("/api/players", status_code=201)
    def create_player(body: NewPlayer):
        name = body.name.strip()
        if not name:
            raise HTTPException(status_code=422, detail="Please enter a name")
        code = new_code()
        player = {
            "pk": f"PLAYER#{code}", "sk": "PROFILE", "type": "PLAYER",
            "code": code, "name": name, "points": 0, "candies": 0, "streak": 0,
            "owned": [], "equipped": {},
        }
        store.put(player)
        return profile_view(player)

    @app.get("/api/players/{code}")
    def get_player(code: str):
        return profile_view(load_player(code))

    @app.get("/api/players/{code}/levels/{root}/questions")
    def get_questions(code: str, root: str):
        player = load_player(code)
        index = content.level_index(root)
        if index is None:
            raise HTTPException(status_code=404, detail="Unknown root")
        if not is_unlocked(index, level_state(player["code"])):
            raise HTTPException(status_code=403, detail="Finish the previous level first")
        # Answers are never sent; content.public_question strips them out for every format.
        public = [content.public_question(q) for q in content.questions(root)]
        return {"root": root, "meaning": content.morphemes()[root]["meaning"], "questions": public}

    @app.post("/api/players/{code}/answers")
    def answer(code: str, body: AnswerIn):
        player = load_player(code)
        index = content.level_index(body.root)
        if index is None:
            raise HTTPException(status_code=404, detail="Unknown root")
        if not is_unlocked(index, level_state(player["code"])):
            raise HTTPException(status_code=403, detail="Finish the previous level first")
        question = content.find_question(body.root, body.question_id)
        if question is None:
            raise HTTPException(status_code=404, detail="Unknown question")

        pk = player["pk"]
        q_sk = f"Q#{body.root}#{body.question_id}"
        q_state = store.get(pk, q_sk) or {"pk": pk, "sk": q_sk, "done": False, "wrong": 0, "stage": 0}
        totals = lambda p: {"points": p["points"], "candies": p["candies"], "streak": p["streak"]}  # noqa: E731
        stage = q_state.get("stage", 0)

        if q_state["done"]:
            return {"correct": True, "already_answered": True, "points_awarded": 0,
                    "candies_awarded": 0, "explanation": question["good"], **totals(player)}

        if content.is_correct(question, body, stage) and stage + 1 < content.stage_count(question):
            # Two-step question: first step passed, no points yet, show the second step.
            q_state["stage"] = stage + 1
            store.put(q_state)
            step = question["stages"][stage]
            return {"correct": True, "stage_passed": True, "already_answered": False,
                    "points_awarded": 0, "candies_awarded": 0, "explanation": step["good"],
                    "next": content.public_question(question, stage + 1), **totals(player)}

        if content.is_correct(question, body, stage):
            first_try = q_state["wrong"] == 0
            points, candies, streak = game.score_answer(first_try, player["streak"])
            q_state["done"] = True
            q_state["first_try"] = first_try
            store.put(q_state)

            level_sk = f"LEVEL#{body.root}"
            level = store.get(pk, level_sk) or {"pk": pk, "sk": level_sk, "root": body.root,
                                                 "completed": False, "correct": 0, "first_try": 0, "stars": 0}
            level["correct"] += 1
            level["first_try"] += 1 if first_try else 0
            store.put(level)

            player["points"] += points
            player["candies"] += candies
            player["streak"] = streak
            store.put(player)
            return {"correct": True, "already_answered": False, "points_awarded": points,
                    "candies_awarded": candies, "first_try": first_try,
                    "explanation": question["good"], **totals(player)}

        q_state["wrong"] += 1
        store.put(q_state)
        player["streak"] = 0
        store.put(player)
        return {"correct": False, "already_answered": False, "points_awarded": 0,
                "candies_awarded": 0, "explanation": wrong_reason(question, body),
                **totals(player)}

    @app.post("/api/players/{code}/levels/{root}/finish")
    def finish_level(code: str, root: str):
        player = load_player(code)
        if content.level_index(root) is None:
            raise HTTPException(status_code=404, detail="Unknown root")
        level_sk = f"LEVEL#{root}"
        level = store.get(player["pk"], level_sk)
        total = len(content.questions(root))
        if not level or level["correct"] < total:
            raise HTTPException(status_code=409, detail="Answer every question correctly first")
        stars = game.stars_for(level["first_try"], total)
        level["completed"] = True
        level["stars"] = max(stars, level.get("stars", 0))
        store.put(level)
        return {"root": root, "stars": level["stars"], "first_try": level["first_try"], "total": total,
                "points": player["points"], "candies": player["candies"]}

    @app.get("/api/shop")
    def get_shop():
        return {"items": shop.CATALOG}

    @app.post("/api/players/{code}/shop/buy")
    def buy(code: str, body: ShopItemIn):
        player = load_player(code)
        item = shop.find(body.item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Unknown item")
        owned = list(player.get("owned", []))
        if item["id"] in owned:
            raise HTTPException(status_code=409, detail="You already own this")
        if player.get("candies", 0) < item["price"]:
            raise HTTPException(status_code=400, detail="Not enough candies yet. Keep answering!")
        player["candies"] = player.get("candies", 0) - item["price"]
        owned.append(item["id"])
        player["owned"] = owned
        store.put(player)
        return profile_view(player)

    @app.post("/api/players/{code}/shop/equip")
    def equip(code: str, body: ShopItemIn):
        player = load_player(code)
        item = shop.find(body.item_id)
        if item is None or item["id"] not in player.get("owned", []):
            raise HTTPException(status_code=403, detail="Buy this item first")
        equipped = dict(player.get("equipped", {}))
        equipped[item["slot"]] = item["id"]
        player["equipped"] = equipped
        store.put(player)
        return profile_view(player)

    # ---- Wren & Martin grammar quiz: same player, points and candies as Word Wizard ----

    def wm_chapter_or_404(chapter):
        known = {c["chapter"]: c for c in content.wm_chapters()}
        if chapter not in known:
            raise HTTPException(status_code=404, detail="Unknown chapter")
        return known[chapter]

    @app.get("/api/wm/chapters")
    def wm_chapters():
        return {"chapters": content.wm_chapters()}

    @app.get("/api/players/{code}/wm/chapters/{chapter}/questions")
    def wm_questions(code: str, chapter: int):
        player = load_player(code)
        info = wm_chapter_or_404(chapter)
        pk = player["pk"]
        questions = []
        for q in content.wm_questions(chapter):
            state = store.get(pk, f"WM#{q['id']}") or {}
            questions.append({**content.wm_public_question(q), "done": bool(state.get("done"))})
        return {"chapter": chapter, "title": info["title"], "questions": questions,
                "done": sum(1 for q in questions if q["done"])}

    # Student-made tests: no login and nothing stored. Chapters are "1,5,9" (empty = all); formats are "ABCD" letters.
    @app.get("/api/wm/tests/build")
    def wm_build_test(chapters: str = "", formats: str = "ABCD", count: int = 10):
        known = [c["chapter"] for c in content.wm_chapters()]
        try:
            chosen = [int(c) for c in chapters.split(",") if c.strip()] or known
        except ValueError:
            raise HTTPException(status_code=400, detail="Chapters must be numbers")
        if any(c not in known for c in chosen):
            raise HTTPException(status_code=404, detail="Unknown chapter")
        wanted = [f for f in formats.upper() if f in wm_tests.FORMATS]
        if not wanted:
            raise HTTPException(status_code=400, detail="Pick at least one format")
        items = wm_tests.build(chosen, wanted, max(1, min(count, 50)))
        if not items:
            raise HTTPException(status_code=404, detail="No questions match this choice")
        return {"items": items}

    @app.post("/api/wm/tests/grade")
    def wm_grade_test(body: WmGradeIn):
        return wm_tests.grade([item.model_dump() for item in body.items])

    @app.get("/api/players/{code}/wm/progress")
    def wm_progress(code: str):
        player = load_player(code)
        done = {}
        for item in store.query_prefix(player["pk"], "WM#"):
            if item.get("done"):
                key = str(item.get("chapter"))
                done[key] = done.get(key, 0) + 1
        return {"done": done}

    @app.post("/api/players/{code}/wm/answers")
    def wm_answer(code: str, body: WmAnswerIn):
        player = load_player(code)
        wm_chapter_or_404(body.chapter)
        question = content.wm_find_question(body.chapter, body.question_id)
        if question is None:
            raise HTTPException(status_code=404, detail="Unknown question")

        pk = player["pk"]
        state_sk = f"WM#{body.question_id}"
        state = store.get(pk, state_sk) or {"pk": pk, "sk": state_sk, "done": False, "wrong": 0, "chapter": body.chapter}
        totals = lambda p: {"points": p["points"], "candies": p["candies"], "streak": p["streak"]}  # noqa: E731

        if state["done"]:
            return {"correct": True, "already_answered": True, "points_awarded": 0,
                    "candies_awarded": 0, "explanation": question["explanation"], **totals(player)}

        if body.choice == question["correct"]:
            first_try = state["wrong"] == 0
            points, candies, streak = game.score_answer(first_try, player["streak"])
            state["done"] = True
            store.put(state)
            player["points"] += points
            player["candies"] += candies
            player["streak"] = streak
            store.put(player)
            return {"correct": True, "already_answered": False, "points_awarded": points,
                    "candies_awarded": candies, "first_try": first_try,
                    "explanation": question["explanation"], **totals(player)}

        state["wrong"] += 1
        store.put(state)
        player["streak"] = 0
        store.put(player)
        return {"correct": False, "already_answered": False, "points_awarded": 0,
                "candies_awarded": 0, "explanation": question["reasons"][body.choice],
                **totals(player)}

    # ---- Cambridge Lower Secondary Maths Stage 8: notes, chapter quizzes and student-made tests ----
    # No login: the same wallet and board as the other sections. Nothing about these tests is stored.

    def cm_chapter_or_404(number):
        ch = cambridge.chapter(number)
        if ch is None:
            raise HTTPException(status_code=404, detail="Unknown chapter")
        return ch

    @app.get("/api/cm/chapters")
    def cm_chapters():
        return {"chapters": cambridge.chapters()}

    @app.get("/api/cm/chapters/{number}")
    def cm_chapter(number: int):
        ch = cm_chapter_or_404(number)
        return {"chapter": number, "title": ch["title"], "notes": ch["notes"],
                "questions": len(ch["questions"])}

    @app.get("/api/cm/chapters/{number}/quiz")
    def cm_quiz(number: int):
        ch = cm_chapter_or_404(number)
        return {"chapter": number, "title": ch["title"], "questions": cambridge.quiz(number)}

    @app.get("/api/cm/tests/build")
    def cm_build_test(chapters: str = "", formats: str = "ABCD", count: int = 10):
        known = [c["chapter"] for c in cambridge.chapters()]
        try:
            chosen = [int(c) for c in chapters.split(",") if c.strip()] or known
        except ValueError:
            raise HTTPException(status_code=400, detail="Chapters must be numbers")
        if any(c not in known for c in chosen):
            raise HTTPException(status_code=404, detail="Unknown chapter")
        wanted = [f for f in formats.upper() if f in cambridge.FORMATS]
        if not wanted:
            raise HTTPException(status_code=400, detail="Pick at least one format")
        items = cambridge.build(chosen, wanted, max(1, min(count, 50)))
        if not items:
            raise HTTPException(status_code=404, detail="No questions match this choice")
        return {"items": items}

    @app.post("/api/cm/tests/grade")
    def cm_grade_test(body: WmGradeIn):
        return cambridge.grade([item.model_dump() for item in body.items])

    @app.get("/api/leaderboard")
    def leaderboard(limit: int = 10):
        limit = max(1, min(limit, 50))
        rows = store.board(limit)
        return {"rows": [{"name": r["name"], "points": r.get("points", 0)} for r in rows]}

    return app


app = create_app()
handler = Mangum(app)
