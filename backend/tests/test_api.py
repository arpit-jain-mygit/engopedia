from fastapi.testclient import TestClient

from app import content, game
from app.main import create_app
from app.store import MemoryStore


def client():
    return TestClient(create_app(MemoryStore()))


def new_player(c, name="Maya"):
    return c.post("/api/players", json={"name": name}).json()


def right_body(full, stage=0):
    """The correct answer body for one question, from the answer key (tests only)."""
    fmt = full["format"]
    if fmt == "two":
        return {"choice": full["stages"][stage]["answer"]}
    if fmt in ("build", "type"):
        return {"text": full["target"]}
    if fmt == "match":
        return {"pairs": [p[1] for p in full["pairs"]]}
    return {"choice": full["answer"]}


def play_level(c, code, root):
    """Answer every question in a level correctly, all steps included (tests only)."""
    qs = c.get(f"/api/players/{code}/levels/{root}/questions").json()["questions"]
    results = []
    for q in qs:
        full = content.find_question(root, q["id"])
        for stage in range(len(full["stages"]) if full["format"] == "two" else 1):
            results.append(c.post(f"/api/players/{code}/answers",
                                  json={"root": root, "question_id": q["id"], **right_body(full, stage)}).json())
    return results


def choice_level():
    """A level whose first question is a choice format, so a wrong pick can be tried."""
    for lv in content.levels():
        q = content.questions(lv["root"])[0]
        if q["format"] in ("emoji", "scenario", "hear", "odd", "tf"):
            return lv["root"], q
    raise AssertionError("no choice question")


def unlock(c, code, root):
    """Finish every level before root, so root is open."""
    for lv in content.levels()[:content.level_index(root)]:
        play_level(c, code, lv["root"])
        c.post(f"/api/players/{code}/levels/{lv['root']}/finish")


# ---- Quiz content comes only from the QuestionBank sheet ----

def test_levels_and_questions_come_from_the_sheet():
    lvls = content.levels()
    assert len(lvls) == 175
    assert sum(lv["word_count"] for lv in lvls) == 239
    assert all(lv["meaning"] for lv in lvls)


def test_every_question_matches_its_format():
    for q in content._quiz()["questions"]:
        fmt = q["format"]
        assert q["good"], q["id"]
        if fmt in ("emoji", "scenario", "hear", "odd", "tf"):
            assert len(q["choices"]) >= 2 and len(set(q["choices"])) == len(q["choices"]), q["id"]
            assert 0 <= q["answer"] < len(q["choices"]), q["id"]
        elif fmt == "two":
            assert len(q["stages"]) == 2, q["id"]
            for st in q["stages"]:
                assert 0 <= st["answer"] < len(st["choices"]), q["id"]
        elif fmt == "build":
            assert sorted("".join(q["tiles"])) == sorted(q["target"]), q["id"]
        elif fmt == "type":
            assert q["target"], q["id"]
        elif fmt == "match":
            assert 2 <= len(q["pairs"]) <= 4 and all(p[1] for p in q["pairs"]), q["id"]
        else:
            raise AssertionError((q["id"], fmt))


def test_choice_questions_keep_reasons_for_the_wrong_answer():
    for q in content._quiz()["questions"]:
        if q["format"] in ("emoji", "scenario", "hear"):
            assert len(q["reasons"]) == 4 and all(q["reasons"]), q["id"]


def test_no_hint_fields_are_left_in_the_content():
    for q in content._quiz()["questions"]:
        assert not any(k.startswith("hint") for k in q), q["id"]


def test_public_questions_do_not_leak_answers_or_reasons():
    c = client()
    p = new_player(c)
    root, _ = choice_level()
    data = c.get(f"/api/players/{p['code']}/levels/{root}/questions").json()
    for q in data["questions"]:
        assert not {"answer", "good", "try", "reasons", "roots"} & set(q), q["id"]


def test_hint_route_is_gone():
    c = client()
    p = new_player(c)
    root, _ = choice_level()
    r = c.post(f"/api/players/{p['code']}/hints", json={"root": root, "question_id": "x"})
    assert r.status_code == 404 or r.status_code == 405


# ---- Answering ----

def test_correct_first_try_scores_and_collects_candy():
    c = client()
    p = new_player(c)
    root, _ = choice_level()
    q = c.get(f"/api/players/{p['code']}/levels/{root}/questions").json()["questions"][0]
    full = content.find_question(root, q["id"])
    r = c.post(f"/api/players/{p['code']}/answers",
               json={"root": root, "question_id": q["id"], "choice": full["answer"]}).json()
    assert r["correct"] is True and r["first_try"] is True
    assert r["points_awarded"] == game.POINTS_CORRECT + game.FIRST_TRY_BONUS
    assert r["candies_awarded"] == 1
    assert "hint_penalty" not in r


def test_wrong_answer_shows_the_reason_for_the_option_picked():
    c = client()
    p = new_player(c)
    root, _ = choice_level()
    q = c.get(f"/api/players/{p['code']}/levels/{root}/questions").json()["questions"][0]
    full = content.find_question(root, q["id"])
    wrong = (full["answer"] + 1) % 4
    r = c.post(f"/api/players/{p['code']}/answers",
               json={"root": root, "question_id": q["id"], "choice": wrong}).json()
    assert r["correct"] is False and r["points_awarded"] == 0 and r["candies_awarded"] == 0
    assert r["explanation"] == full["reasons"][wrong]
    # Right answer after a miss counts, but not as first try.
    r2 = c.post(f"/api/players/{p['code']}/answers",
                json={"root": root, "question_id": q["id"], "choice": full["answer"]}).json()
    assert r2["points_awarded"] == game.POINTS_CORRECT and r2["candies_awarded"] == 1


def test_answering_same_question_twice_gives_no_extra_points():
    c = client()
    p = new_player(c)
    root, _ = choice_level()
    q = c.get(f"/api/players/{p['code']}/levels/{root}/questions").json()["questions"][0]
    full = content.find_question(root, q["id"])
    body = {"root": root, "question_id": q["id"], "choice": full["answer"]}
    c.post(f"/api/players/{p['code']}/answers", json=body)
    again = c.post(f"/api/players/{p['code']}/answers", json=body).json()
    assert again["already_answered"] is True and again["points_awarded"] == 0


# ---- Levels ----

def test_finish_requires_all_correct_then_unlocks_next_level():
    c = client()
    p = new_player(c)
    code = p["code"]
    first, second = content.levels()[0]["root"], content.levels()[1]["root"]
    assert c.post(f"/api/players/{code}/levels/{first}/finish").status_code == 409
    play_level(c, code, first)
    assert c.post(f"/api/players/{code}/levels/{first}/finish").status_code == 200
    assert c.get(f"/api/players/{code}/levels/{second}/questions").status_code == 200


def test_locked_level_is_forbidden():
    c = client()
    p = new_player(c)
    second = content.levels()[1]["root"]
    assert c.get(f"/api/players/{p['code']}/levels/{second}/questions").status_code == 403


def test_stars_follow_first_try_share():
    assert game.stars_for(10, 10) == 3
    assert game.stars_for(5, 10) == 2
    assert game.stars_for(1, 10) == 1


def test_streak_bonus_every_three_first_try_answers():
    _, _, s1 = game.score_answer(True, 0)
    _, _, s2 = game.score_answer(True, s1)
    points, _, s3 = game.score_answer(True, s2)
    assert s3 == 3 and points == game.POINTS_CORRECT + game.FIRST_TRY_BONUS + game.STREAK_BONUS


# ---- Players, shop, leaderboard ----

def test_create_and_fetch_player_by_code():
    c = client()
    p = new_player(c, "Leo")
    assert len(p["code"]) == 6
    assert c.get(f"/api/players/{p['code']}").json()["name"] == "Leo"


def test_unknown_code_is_404():
    assert client().get("/api/players/NOPE00").status_code == 404


def test_blank_name_rejected():
    assert client().post("/api/players", json={"name": "   "}).status_code == 422


def test_shop_lists_items_with_slots():
    items = client().get("/api/shop").json()["items"]
    assert items and all(i["slot"] in ("hat", "wand", "pet") for i in items)


def test_buy_needs_enough_candies_then_deducts_and_cannot_repeat():
    c = client()
    p = new_player(c)
    code = p["code"]
    assert c.post(f"/api/players/{code}/shop/buy", json={"item_id": "hat-cap"}).status_code == 400
    for lv in content.levels():
        play_level(c, code, lv["root"])
        c.post(f"/api/players/{code}/levels/{lv['root']}/finish")
        if c.get(f"/api/players/{code}").json()["candies"] >= 10:
            break
    candies = c.get(f"/api/players/{code}").json()["candies"]
    bought = c.post(f"/api/players/{code}/shop/buy", json={"item_id": "hat-cap"}).json()
    assert "hat-cap" in bought["owned"] and bought["candies"] == candies - 10
    assert c.post(f"/api/players/{code}/shop/buy", json={"item_id": "hat-cap"}).status_code == 409


def test_equip_requires_owning_and_wears_one_per_slot():
    c = client()
    p = new_player(c)
    code = p["code"]
    assert c.post(f"/api/players/{code}/shop/equip", json={"item_id": "hat-cap"}).status_code == 403
    for lv in content.levels():
        play_level(c, code, lv["root"])
        c.post(f"/api/players/{code}/levels/{lv['root']}/finish")
        if c.get(f"/api/players/{code}").json()["candies"] >= 10:
            break
    c.post(f"/api/players/{code}/shop/buy", json={"item_id": "hat-cap"})
    equipped = c.post(f"/api/players/{code}/shop/equip", json={"item_id": "hat-cap"}).json()["equipped"]
    assert equipped == {"hat": "hat-cap"}


def test_leaderboard_orders_by_points():
    c = client()
    assert c.get("/api/leaderboard").json()["rows"] == []
    p = new_player(c, "Ava")
    root, _ = choice_level()
    play_level(c, p["code"], root)
    rows = c.get("/api/leaderboard").json()["rows"]
    assert rows[0]["name"] == "Ava" and rows[0]["points"] > 0


def test_cambridge_quiz_awards_one_maths_candy_per_question_once():
    from app import cambridge
    c = client()
    code = new_player(c)["code"]
    chapter = c.get("/api/cm/chapters").json()["chapters"][0]["chapter"]
    quiz = c.get(f"/api/cm/chapters/{chapter}/quiz").json()["questions"]

    def right_items(items):
        out = []
        for q in items:
            found = cambridge._expected(q["id"])
            _, _, seed, expected = found
            shown = cambridge._shown_options(found[0], seed)
            letter = cambridge.LETTERS[shown.index(expected)]
            out.append({"id": q["id"], "answer": letter})
        return out

    first = c.post(f"/api/players/{code}/cm/grade", json={"items": right_items(quiz)}).json()
    assert first["candies_awarded"] == len(quiz)
    assert first["candies_by_category"]["cambridge_maths"] == len(quiz)
    # A second check with fresh shuffles of the same questions earns nothing more.
    again = c.get(f"/api/cm/chapters/{chapter}/quiz").json()["questions"]
    second = c.post(f"/api/players/{code}/cm/grade", json={"items": right_items(again)}).json()
    assert second["candies_awarded"] == 0
    profile = c.get(f"/api/players/{code}").json()
    assert profile["candies"] == len(quiz)
    assert profile["candies_by_category"]["word_wizard"] == 0
