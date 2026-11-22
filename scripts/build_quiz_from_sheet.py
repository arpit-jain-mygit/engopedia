"""Build backend/data/quiz.json from the QuestionBank sheet, and nothing else.

Source: question_bank/word_power_made_easy_with_QuestionBank.xlsx, sheet "QuestionBank".
One row is one question (4 options, the correct letter, the explanation, and a reason for
each option). Levels follow the order of first appearance of each Root in the sheet.

Each question keeps the four reasons on the server. A wrong answer returns the reason for the
option the child picked. Reasons are never sent with the question.

Usage: python3 scripts/build_quiz_from_sheet.py
"""
import json
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "question_bank" / "word_power_made_easy_with_QuestionBank.xlsx"
QUIZ = ROOT / "backend" / "data" / "quiz.json"
LETTERS = "ABCD"
REASON_LINE = re.compile(r"^([ABCD])\.\s*(.*)$")
LABEL = re.compile(r"^(Correct|Wrong):\s*", re.IGNORECASE)


def parse_reasons(text):
    """Split 'A. Word: Correct: reason' lines into four plain reasons, in A to D order."""
    reasons = {}
    for line in (text or "").splitlines():
        m = REASON_LINE.match(line.strip())
        if not m:
            continue
        body = m.group(2)
        # Drop the option word and the "Correct:" / "Wrong:" label, keep the reason itself.
        if ": " in body:
            body = body.split(": ", 1)[1]
        reasons[m.group(1)] = LABEL.sub("", body).strip()
    return [reasons.get(letter, "") for letter in LETTERS]


def fallback_meaning(explanation):
    """Root meaning when the Morphemes sheet has none: the first bracket in the explanation."""
    m = re.search(r"\(([^)]+)\)", explanation or "")
    return m.group(1) if m else ""


def main():
    wb = load_workbook(SOURCE, read_only=True)
    morphemes = {r[0]: r[2] for r in wb["Morphemes"].iter_rows(min_row=2, values_only=True) if r[0]}
    rows = [r for r in wb["QuestionBank"].iter_rows(min_row=2, values_only=True) if r[0] is not None]

    roots, root_index, questions = [], {}, []
    for qno, root, word, stem, a, b, c, d, letter, explanation, why in rows:
        if root not in root_index:
            meaning = morphemes.get(root) or fallback_meaning(explanation)
            root_index[root] = len(roots)
            roots.append({"root": root, "meaning": meaning, "words": 0})
        roots[root_index[root]]["words"] += 1
        choices = [a, b, c, d]
        questions.append({
            "id": f"{root.lower()}-{qno}",
            "root": root,
            "format": "choice",
            "prompt": stem,
            "choices": choices,
            "answer": LETTERS.index(letter.strip().upper()),
            "good": explanation,
            "try": "Read the reason for the option you picked, then try again.",
            "reasons": parse_reasons(why),
            "roots": [[root, roots[root_index[root]]["meaning"]]],
        })

    # Keep the levels in sheet order, and the questions of each level together.
    ordered = sorted(questions, key=lambda q: root_index[q["root"]])
    QUIZ.write_text(json.dumps({"roots": roots, "questions": ordered}, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    print(f"levels: {len(roots)}  questions: {len(ordered)}", file=sys.stderr)


if __name__ == "__main__":
    main()
