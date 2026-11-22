"""Build the QuestionBank sheet from per-root JSON files in question_bank/roots/.

Each root file: a list of questions, one per word built from that root (column E).
Each question: word, question, options (A-D), correct (letter), explanation,
reasons (A-D: "Correct: ..." or "Wrong: ...").

The build checks coverage: every (word, root) pair in column E must have exactly one question.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

HERE = Path(__file__).resolve().parent
SOURCE = Path("/private/tmp/claude-501/-Users-arpit-Documents-claude-transcription-workspace/583ec6a4-edd8-4cd2-a679-113f05b63d47/scratchpad/word_power_made_easy_sessions_1_to_47.xlsx")
OUT = HERE / "word_power_made_easy_with_QuestionBank.xlsx"
LETTERS = "ABCD"


def expected_pairs():
    wb = load_workbook(SOURCE, read_only=True, data_only=True)
    pairs = set()
    for row in wb["Words"].iter_rows(min_row=2, values_only=True):
        word, roots = row[2], row[4]
        if not word or not roots or roots == "-":
            continue
        for r in str(roots).split(","):
            r = r.strip()
            if r:
                pairs.add((word, r))
    return pairs


def load_questions():
    rows, problems = [], []
    for path in sorted((HERE / "roots").glob("*.json")):
        root = path.stem
        for n, q in enumerate(json.loads(path.read_text(encoding="utf-8")), start=1):
            where = f"{root} #{n} ({q.get('word')})"
            opts = q.get("options", [])
            if len(opts) != 4 or len(set(opts)) != 4:
                problems.append(f"{where}: needs 4 different options")
                continue
            if q.get("correct") not in LETTERS:
                problems.append(f"{where}: correct must be A-D")
                continue
            reasons = q.get("reasons", {})
            if set(reasons) != set(LETTERS):
                problems.append(f"{where}: needs a reason for A, B, C and D")
                continue
            rows.append((root, q))
    return rows, problems


def main():
    rows, problems = load_questions()
    expected = expected_pairs()
    have = Counter((q["word"], root) for root, q in rows)
    missing = sorted(p for p in expected if have[p] == 0)
    dupes = sorted(p for p, c in have.items() if c > 1)
    extra = sorted(p for p in have if p not in expected)

    wb = load_workbook(SOURCE)
    if "QuestionBank" in wb.sheetnames:
        del wb["QuestionBank"]
    ws = wb.create_sheet("QuestionBank")
    ws.append(["Q No", "Root", "Word", "Question", "Option A", "Option B", "Option C", "Option D",
               "Correct answer", "Explanation", "Why each option is right or wrong"])
    for i, (root, q) in enumerate(rows, start=1):
        why_each = "\n".join(f"{L}. {q['options'][j]}: {q['reasons'][L]}" for j, L in enumerate(LETTERS))
        ws.append([i, root, q["word"], q["question"], *q["options"], q["correct"], q["explanation"], why_each])

    thin = Side(style="thin", color="BFBFBF")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    widths = {"A": 7, "B": 12, "C": 16, "D": 60, "E": 18, "F": 18, "G": 18, "H": 18, "I": 12, "J": 60, "K": 90}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows():
        for cell in row:
            cell.font = Font(name="Arial", size=11, bold=cell.row == 1)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = border
            if cell.row == 1:
                cell.fill = PatternFill("solid", fgColor="D9E1F2")
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    wb.save(OUT)

    print(f"questions written: {len(rows)} of {len(expected)} word-root pairs")
    print(f"roots covered: {len({r for r, _ in rows})}")
    print(f"missing pairs: {len(missing)}")
    print(f"duplicate pairs: {len(dupes)} {dupes[:5]}")
    print(f"extra pairs not in column E: {len(extra)} {extra[:5]}")
    for p in problems:
        print("PROBLEM:", p)


if __name__ == "__main__":
    main()
