"""Build the three hints for every question offline, save them in quiz_database.xlsx, and sync quiz.json.

The API never builds hints. It reads the stored text, so every hint can be reviewed in Excel.

Columns written to the Questions sheet:
  K  Hint 2 (clue)    Fill in the blank: the word's sample sentence with the answer blanked out.
                      If the sentence does not contain the word, the word's meaning is used.
  N  Hint 1 (root)    The root and its meaning, from the Root and Root meaning columns.
  O  Hint 3 (letters) The first three letters and the length of the answer.
  P  Reviewed         Blank for you to fill in (for example "ok" or a note).

Usage: backend/.venv/bin/python scripts/fill_hints.py   (needs openpyxl)
"""
import json
import re
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
WORKBOOK = ROOT / "quiz_database.xlsx"
QUIZ = ROOT / "backend" / "data" / "quiz.json"
WORDS = ROOT / "backend" / "data" / "words.json"
BLANK = "____"
HEADERS = {"hint2": "Hint 2 (clue)", "hint1": "Hint 1 (root)", "hint3": "Hint 3 (letters)", "reviewed": "Reviewed"}


def hint1(root, root_meaning):
    return f'The root "{root}" means "{root_meaning}".'


def hint3(answer):
    return f'It starts with "{answer[:3]}" and has {len(answer)} letters.'


def hint2(word, sentence, meaning):
    """Fill in the blank from the sample sentence; the meaning when the sentence lacks the word."""
    stem = word[:-1] if word.endswith("e") else word
    if sentence and len(stem) >= 4:
        pattern = re.compile(r"\b" + re.escape(stem) + r"\w*", re.IGNORECASE)
        if pattern.search(sentence):
            return f'Fill in the blank: "{pattern.sub(BLANK, sentence, count=1)}"', "sentence"
    return f"Clue: {meaning}", "meaning"


def meaning_from_explanation(explanation, word):
    prefix = f"{word}: "
    return explanation[len(prefix):] if explanation and explanation.startswith(prefix) else ""


def main():
    sentences = {w["word"]: w["sentence"] for w in json.loads(WORDS.read_text(encoding="utf-8"))}
    wb = load_workbook(WORKBOOK)
    ws = wb["Questions"]
    headers = [c.value for c in ws[1]]
    # The Hint column was called "Hint" before it became "Hint 2 (clue)"; accept either.
    hint_name = "Hint 2 (clue)" if "Hint 2 (clue)" in headers else "Hint"
    col = {h: headers.index(h) for h in ("Question ID", "Root", "Root meaning", "Target word", "Explanation", hint_name)}
    ws.cell(1, col[hint_name] + 1).value = HEADERS["hint2"]
    # Add the new columns at the end (or reuse them if they are already there).
    new_cols = {}
    for key in ("hint1", "hint3", "reviewed"):
        if HEADERS[key] in headers:
            new_cols[key] = headers.index(HEADERS[key]) + 1
        else:
            ws.cell(1, ws.max_column + 1).value = HEADERS[key]
            new_cols[key] = ws.max_column
    hints, counts = {}, {"sentence": 0, "meaning": 0}
    for row in ws.iter_rows(min_row=2):
        qid, root, root_meaning = row[col["Question ID"]].value, row[col["Root"]].value, row[col["Root meaning"]].value
        word, expl = row[col["Target word"]].value, row[col["Explanation"]].value
        clue, how = hint2(word, sentences.get(word, ""), meaning_from_explanation(expl, word))
        counts[how] += 1
        h = {"hint2": clue, "hint1": hint1(root, root_meaning), "hint3": hint3(word)}
        row[col[hint_name]].value = clue
        row[new_cols["hint1"] - 1].value = h["hint1"]
        row[new_cols["hint3"] - 1].value = h["hint3"]
        hints[qid] = h
    wb.save(WORKBOOK)

    data = json.loads(QUIZ.read_text(encoding="utf-8"))
    changed = 0
    for q in data["questions"]:
        if q["id"] in hints:
            h = hints[q["id"]]
            new = {"hint1": h["hint1"], "hint2": h["hint2"], "hint3": h["hint3"]}
            q.pop("hint", None)
            if any(q.get(k) != v for k, v in new.items()):
                changed += 1
            q.update(new)
    QUIZ.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"clue sources: {counts}; quiz.json questions updated: {changed}")


if __name__ == "__main__":
    main()
