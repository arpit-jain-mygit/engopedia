"""Export the Wren & Martin question bank into JSON seed data for the app.

Reads question_bank/grammar/wren_martin_grammar_questions.xlsx (built by
question_bank/grammar/build_wren_martin.py) and writes
backend/data/wren_martin.json. Run again after the workbook changes.

Each question keeps its four options, the index of the correct option, the
explanation, and one reason per option (from the "Why each option..." column).
"""
import json
from collections import OrderedDict
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "question_bank" / "grammar" / "wren_martin_grammar_questions.xlsx"
OUT = ROOT / "backend" / "data" / "wren_martin.json"
LETTERS = "ABCD"


def parse_reasons(cell, options):
    """Turn 'A. <option>: <reason>' lines into one reason per option, in A-D order."""
    lines = [line for line in (cell or "").split("\n") if line.strip()]
    reasons = []
    for letter, option in zip(LETTERS, options):
        prefix = f"{letter}. {option}: "
        match = next((line[len(prefix):] for line in lines if line.startswith(prefix)), None)
        if match is None:
            raise ValueError(f"No reason for option {letter} in: {cell!r}")
        reasons.append(match)
    return reasons


def main():
    ws = load_workbook(SOURCE, read_only=True)["QuestionBank"]
    chapters = OrderedDict()
    questions = []
    seen = set()
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] is None:
            continue
        qno, chapter, title, source, exercise, stem = row[:6]
        options = list(row[6:10])
        correct = LETTERS.index(row[10])
        question_id = f"c{chapter}-q{qno}"
        if question_id in seen:
            raise ValueError(f"Duplicate question id {question_id}")
        seen.add(question_id)
        chapters.setdefault(chapter, {"chapter": chapter, "title": title, "count": 0})["count"] += 1
        questions.append({
            "id": question_id,
            "chapter": chapter,
            "source": source,
            "exercise": exercise or "",
            "stem": stem,
            "options": options,
            "correct": correct,
            "explanation": row[11],
            "reasons": parse_reasons(row[12], options),
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"chapters": sorted(chapters.values(), key=lambda c: c["chapter"]), "questions": questions},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {len(questions)} questions in {len(chapters)} chapters to {OUT}")


if __name__ == "__main__":
    main()
