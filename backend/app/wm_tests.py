"""Student-made Wren & Martin tests: build a random test from chosen chapters and formats, then mark it.

Same rules as question_bank/grammar/build_tests.py, so the app and the printed tests match:
  A  multiple choice        every workbook question
  B  fill in the blank      questions whose stem has a blank; answer = the missing word
  C  true or false          a blank question filled with the right word (True) or a wrong option (False)
  D  write the answer       questions that make sense without their options; answer = the correct option

Nothing is stored. An item id carries the question id and format (e.g. "c40-q3|C|F"), so grading
rebuilds the expected answer from the workbook data.
"""
import random
import re

from . import content

FORMATS = ("A", "B", "C", "D")
LETTERS = "ABCD"
BLANK_RE = re.compile(r"_{3,}")
INSTRUCTION = re.compile(r"^(Choose the correct form|Fill in)[^:]*:\s*")
OPTION_REFERENCE = re.compile(r"\b(which|choose|select|following|of these)\b", re.I)


def _is_blank(q):
    return BLANK_RE.search(q["stem"]) is not None


def _sentence(stem):
    return INSTRUCTION.sub("", stem, count=1).strip()


def _true_false(q, variant):
    """Return the statement for a True (right word) or False (first wrong option) variant."""
    right = q["options"][q["correct"]]
    if variant == "T":
        word = right
    else:
        word = next(o for i, o in enumerate(q["options"]) if i != q["correct"])
    return BLANK_RE.sub(word, _sentence(q["stem"])), ("True" if variant == "T" else "False")


def _pool(chapters, formats):
    """Every possible item for the chosen chapters and formats. One True/False variant is picked per question."""
    items = []
    for chapter in chapters:
        for q in content.wm_questions(chapter):
            blank = _is_blank(q)
            if "A" in formats and not blank:
                items.append(("A", q, None))
            if "B" in formats and blank:
                items.append(("B", q, None))
            if "C" in formats and blank:
                items.append(("C", q, random.choice("TF")))
            if "D" in formats and not blank and not OPTION_REFERENCE.search(q["stem"]):
                items.append(("D", q, None))
    return items


def build(chapters, formats, count):
    """A random test: up to `count` items, shuffled. Answers are not included."""
    chosen = [f for f in FORMATS if f in formats]
    pool = _pool(chapters, chosen)
    random.shuffle(pool)
    out = []
    for fmt, q, variant in pool[:count]:
        base = {"chapter": q["chapter"], "format": fmt}
        if fmt == "A":
            out.append({**base, "id": f"{q['id']}|A", "stem": q["stem"], "options": q["options"]})
        elif fmt == "B":
            out.append({**base, "id": f"{q['id']}|B", "stem": _sentence(q["stem"])})
        elif fmt == "C":
            statement, _ = _true_false(q, variant)
            out.append({**base, "id": f"{q['id']}|C|{variant}", "stem": statement})
        else:
            out.append({**base, "id": f"{q['id']}|D", "stem": q["stem"]})
    return out


def _normal(text):
    return re.sub(r"\s+", " ", str(text or "").strip().lower()).rstrip(".!?")


def _expected(item_id):
    """Return (question, format, expected answer text, display text) for an item id, or None if unknown."""
    parts = item_id.split("|")
    if len(parts) < 2:
        return None
    qid, fmt = parts[0], parts[1]
    chapter_part = qid.split("-")[0]
    if not chapter_part.startswith("c") or not chapter_part[1:].isdigit():
        return None
    chapter = int(chapter_part[1:])
    q = content.wm_find_question(chapter, qid)
    if q is None:
        return None
    if fmt == "A":
        return q, fmt, LETTERS[q["correct"]], f"{LETTERS[q['correct']]}. {q['options'][q['correct']]}"
    if fmt == "B":
        answer = q["options"][q["correct"]]
        return q, fmt, answer, answer
    if fmt == "C" and len(parts) == 3 and parts[2] in ("T", "F"):
        answer = "True" if parts[2] == "T" else "False"
        return q, fmt, answer, answer
    if fmt == "D" and not OPTION_REFERENCE.search(q["stem"]):
        answer = q["options"][q["correct"]]
        return q, fmt, answer, answer
    return None


def grade(answers):
    """answers: list of {id, answer}. Returns per-item results and the score."""
    results = []
    for entry in answers:
        item_id = str(entry.get("id", ""))
        given = entry.get("answer", "")
        found = _expected(item_id)
        if found is None:
            results.append({"id": item_id, "known": False, "correct": False})
            continue
        q, fmt, expected, display = found
        if fmt == "A":
            ok = str(given).strip().upper()[:1] == LETTERS[q["correct"]]
        else:
            ok = _normal(given) == _normal(expected)
        results.append({"id": item_id, "known": True, "correct": ok,
                        "expected": display, "explanation": q["explanation"]})
    return {"results": results, "score": sum(1 for r in results if r["correct"]), "total": len(results)}
