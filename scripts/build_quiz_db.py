"""Build the quiz database workbook from the Word Power Made Easy workbook.

For every root, every word built from that root becomes one question:
"Which word is built from <root>?" with four word choices. Distractors never
share a root with the answer, so each question has exactly one right answer.

Outputs:
  quiz_database.xlsx          the quiz database (edit this in Excel)
  backend/data/quiz.json      generated from the workbook for the API

Usage: python3 scripts/build_quiz_db.py <source word workbook .xlsx>
"""
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(sys.argv[1])
MIN_WORDS_PER_ROOT = 5
MAX_MEANING_LEN = 40
LETTERS = "ABCD"
FONT = "Arial"
HEADER_FILL = PatternFill("solid", fgColor="D9E1F2")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def load_existing_hints():
    """Hint column of the workbook already on disk, keyed by Question ID."""
    path = ROOT / "quiz_database.xlsx"
    if not path.exists():
        return {}
    ws = load_workbook(path, read_only=True)["Questions"]
    return {row[0]: row[10] for row in ws.iter_rows(min_row=2, values_only=True) if row[0] and row[10]}


EXISTING_HINTS = load_existing_hints()


def read_source(path):
    wb = load_workbook(path, read_only=True, data_only=True)
    morph = {}
    for name, mtype, meaning, *_ in wb["Morphemes"].iter_rows(min_row=2, values_only=True):
        if name:
            morph[name] = {"type": mtype, "meaning": meaning or ""}
    words = []
    for _no, _session, word, built_from, roots, meaning, sentence, *_ in wb["Words"].iter_rows(min_row=2, values_only=True):
        if not word:
            continue
        root_list = [r.strip() for r in (roots or "").split(",") if r.strip() and r.strip() != "-"]
        words.append({"word": word, "roots": root_list, "meaning": meaning or "", "sentence": sentence or ""})
    return morph, words


def build_questions(morph, words):
    by_root = defaultdict(list)
    for w in words:
        for r in w["roots"]:
            by_root[r].append(w)
    roots = []
    questions = []
    for root, members in sorted(by_root.items()):
        info = morph.get(root)
        if not info or info["type"] != "Root":
            continue
        if len(members) < MIN_WORDS_PER_ROOT or len(info["meaning"]) > MAX_MEANING_LEN:
            continue
        roots.append({"root": root, "meaning": info["meaning"], "words": len(members)})
        rng = random.Random(root)
        others = [w for w in words if root not in w["roots"]]
        for target in sorted(members, key=lambda w: w["word"]):
            pool = [w for w in others if not set(w["roots"]) & set(target["roots"])]
            distractors = rng.sample(pool, 3)
            choices = [target["word"]] + [d["word"] for d in distractors]
            rng.shuffle(choices)
            questions.append({
                "question_id": f"{root}-{target['word']}",
                "root": root,
                "root_meaning": info["meaning"],
                "target_word": target["word"],
                "prompt": f'Which word is built from "{root}"?',
                "choices": choices,
                "answer": LETTERS[choices.index(target["word"])],
                # Keep the clue already in the workbook (hand-edited or from fill_hints.py).
                "hint": EXISTING_HINTS.get(f"{root}-{target['word']}", f'Look for the root "{root}" inside the word.'),
                "explanation": f'{target["word"]}: {target["meaning"]}',
                "try_again": f'Find the word that has "{root}" in it.',
            })
    return roots, questions


def style(ws, widths):
    for col, width in widths.items():
        ws.column_dimensions[col].width = width
    for row in ws.iter_rows():
        for cell in row:
            cell.font = Font(name=FONT, size=11, bold=cell.row == 1)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = BORDER
            if cell.row == 1:
                cell.fill = HEADER_FILL
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions


def write_workbook(roots, questions, path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Questions"
    headers = ["Question ID", "Root", "Root meaning", "Target word", "Prompt",
               "Choice A", "Choice B", "Choice C", "Choice D", "Correct",
               "Hint", "Explanation", "Try again"]
    ws.append(headers)
    for q in questions:
        ws.append([q["question_id"], q["root"], q["root_meaning"], q["target_word"], q["prompt"],
                   *q["choices"], q["answer"], q["hint"], q["explanation"], q["try_again"]])
    style(ws, {"A": 22, "B": 12, "C": 30, "D": 18, "E": 36, "F": 16, "G": 16, "H": 16, "I": 16,
               "J": 10, "K": 34, "L": 50, "M": 34})

    rs = wb.create_sheet("Roots")
    counts = Counter(q["root"] for q in questions)
    rs.append(["Root", "Meaning", "Words in this level", "Questions"])
    for r in roots:
        rs.append([r["root"], r["meaning"], r["words"], counts[r["root"]]])
    style(rs, {"A": 16, "B": 36, "C": 20, "D": 12})

    wb.save(path)


def write_json(roots, questions, path):
    data = {
        "roots": roots,
        "questions": [
            {
                "id": q["question_id"],
                "root": q["root"],
                "prompt": q["prompt"],
                "choices": q["choices"],
                "answer": LETTERS.index(q["answer"]),
                "hint": q["hint"],
                "good": q["explanation"],
                "try": q["try_again"],
                "roots": [[q["root"], q["root_meaning"]]],
            }
            for q in questions
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    # The workbook holds the reviewed hints (Hint 1, 2, 3) and this script does not write them,
    # so refuse to overwrite it. To change hints, edit quiz_database.xlsx and run scripts/fill_hints.py.
    if (ROOT / "quiz_database.xlsx").exists() and "--force" not in sys.argv:
        sys.exit("quiz_database.xlsx exists and holds reviewed hints; not overwriting. Use --force only to start over.")
    morph, words = read_source(SOURCE)
    roots, questions = build_questions(morph, words)
    write_workbook(roots, questions, ROOT / "quiz_database.xlsx")
    write_json(roots, questions, ROOT / "backend" / "data" / "quiz.json")
    print(f"levels: {len(roots)}  questions: {len(questions)}")
