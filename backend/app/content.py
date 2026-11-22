"""Learning content.

Quiz questions and levels come from backend/data/quiz.json, which
scripts/build_quiz_db.py generates from quiz_database.xlsx (the quiz database).
Learn cards come from words.json and morphemes.json, which
scripts/export_workbook.py generates from the Word Power Made Easy workbook.
Answers stay on the server; the API never returns the correct choice.
"""
import json
import random
from functools import lru_cache
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@lru_cache(maxsize=1)
def words():
    return json.loads((DATA_DIR / "words.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def morphemes():
    return json.loads((DATA_DIR / "morphemes.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _quiz():
    return json.loads((DATA_DIR / "quiz.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def levels():
    """Root levels in play order, from the quiz database."""
    return [
        {"root": r["root"], "meaning": r["meaning"], "word_count": r["words"]}
        for r in _quiz()["roots"]
    ]


def level_index(root):
    for i, lv in enumerate(levels()):
        if lv["root"] == root:
            return i
    return None


@lru_cache(maxsize=None)
def questions(root):
    """Every question for one level: one per word built from the root."""
    return [q for q in _quiz()["questions"] if q["root"] == root]


def find_question(root, question_id):
    for q in questions(root):
        if q["id"] == question_id:
            return q
    return None


# Formats that are answered by picking one of "choices" (by index).
CHOICE_FORMATS = {"choice", "emoji", "hear", "odd", "tf", "scenario"}


def _shuffled(items, seed):
    """Same order every time for one question, and never the sheet's own order."""
    rng = random.Random(seed)
    out = list(items)
    for _ in range(20):
        rng.shuffle(out)
        if out != list(items):
            break
    return out


def public_question(q, stage=0):
    """What the client may see. Never the answer, the target word or the pair order."""
    fmt = q.get("format", "choice")
    out = {"id": q["id"], "format": fmt}
    if fmt != "two":
        out["prompt"] = q["prompt"]  # two-step questions carry their prompts per step
    if fmt in CHOICE_FORMATS:
        out["choices"] = q["choices"]
        out["scene"] = q.get("scene", "")    # emoji picture shown above the question
        if fmt == "hear":
            out["speak"] = q["speak"]        # the client reads this aloud; the choices are the words
    elif fmt == "two":
        st = q["stages"][stage]
        out.update({"prompt": st["prompt"], "choices": st["choices"], "stage": stage, "stage_total": len(q["stages"])})
    elif fmt == "build":
        out["tiles"] = _shuffled(q["tiles"], q["id"])
    elif fmt == "type":
        out["length"] = len(q["target"])
    elif fmt == "match":
        out["lefts"] = [p[0] for p in q["pairs"]]
        out["rights"] = _shuffled([p[1] for p in q["pairs"]], q["id"])
    return out


def is_correct(q, body, stage=0):
    """Check one answer. body is an AnswerIn; text, pairs and choice are optional."""
    fmt = q.get("format", "choice")
    if fmt in CHOICE_FORMATS:
        return body.choice is not None and body.choice == q["answer"]
    if fmt == "two":
        return body.choice is not None and body.choice == q["stages"][stage]["answer"]
    if fmt == "build":
        return body.text is not None and body.text == q["target"]
    if fmt == "type":
        return body.text is not None and body.text.strip().lower() == q["target"].lower()
    if fmt == "match":
        if body.pairs is None or len(body.pairs) != len(q["pairs"]):
            return False
        return all(body.pairs[i] == q["pairs"][i][1] for i in range(len(q["pairs"])))
    return False


def stage_count(q):
    return len(q["stages"]) if q.get("format") == "two" else 1


def learn_cards(root):
    """Every word built from a root, with each part explained."""
    morph = morphemes()
    meanings = {w["word"]: w["meaning"] for w in words()}
    cards = []
    for w in words():
        if root not in w["roots"]:
            continue
        parts = []
        for p in w["parts"]:
            if p in morph:
                parts.append({"text": p, "type": morph[p]["type"], "meaning": morph[p]["meaning"]})
            else:
                parts.append({"text": p, "type": "Word", "meaning": meanings.get(p, "")})
        cards.append({"word": w["word"], "parts": parts, "meaning": w["meaning"], "sentence": w["sentence"]})
    cards.sort(key=lambda c: c["word"])
    return cards
