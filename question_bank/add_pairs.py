"""Add the questions for missing (word, root) pairs from a spec file, merging into roots/<root>.json.

A spec module defines SPEC: a list of (word, root, stem, [three distractor words]).
Rules checked here:
  - the pair must be one of the missing (word, root) pairs in the Words sheet
  - each distractor must be a word in the Words sheet, different from the answer and from the others
  - the correct answer sits at A-D in turn, so answers are spread evenly

Reasons are built from the Words sheet meanings, so every "Wrong:" line tells the child what
the other word really means.

Usage: python3 question_bank/add_pairs.py spec_01    (spec files live in question_bank/specs/)
Needs openpyxl (backend/.venv has it).
"""
import importlib
import json
import sys
from pathlib import Path

from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "specs"))
WORKBOOK = HERE / "word_power_made_easy_with_QuestionBank.xlsx"
LETTERS = "ABCD"


def load_words():
    """Word meanings, and the (word, root) pairs that still have no question in roots/."""
    wb = load_workbook(WORKBOOK, read_only=True)
    words, pairs = {}, set()
    for r in wb["Words"].iter_rows(min_row=2, values_only=True):
        if not r[2]:
            continue
        words[r[2]] = (r[5] or "").strip()
        for x in str(r[4] or "").split(","):
            if x.strip() and x.strip() != "-":
                pairs.add((r[2], x.strip()))
    done = set()
    for path in (HERE / "roots").glob("*.json"):
        for q in json.loads(path.read_text(encoding="utf-8")):
            done.add((q["word"], path.stem))
    return words, pairs - done


def existing(root):
    path = HERE / "roots" / f"{root}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def main():
    spec = importlib.import_module(sys.argv[1]).SPEC
    words, missing = load_words()
    problems, added = [], defaultdict_list()
    for n, (word, root, stem, wrong) in enumerate(spec):
        where = f"{word}/{root}"
        if (word, root) not in missing:
            problems.append(f"{where}: not a missing pair (already done, or not in the sheet)")
            continue
        if len(wrong) != 3 or len(set(wrong)) != 3 or word in wrong:
            problems.append(f"{where}: needs 3 different distractors that are not the answer")
            continue
        if any(w not in words for w in wrong):
            bad = [w for w in wrong if w not in words]
            problems.append(f"{where}: distractor not in the Words sheet: {bad}")
            continue
        pos = n % 4
        options = list(wrong)
        options.insert(pos, word)
        reasons = {}
        for j, L in enumerate(LETTERS):
            opt = options[j]
            if opt == word:
                reasons[L] = f"Correct: {words[word]}"
            else:
                reasons[L] = f"Wrong: {words[opt]}"
        added[root].append({"word": word, "question": stem, "options": options, "correct": LETTERS[pos],
                            "explanation": f"{word}: {words[word]}", "reasons": reasons})
        missing.discard((word, root))
    if problems:
        print("NOT WRITTEN, fix these first:")
        print("\n".join(problems))
        sys.exit(1)
    for root, items in added.items():
        path = HERE / "roots" / f"{root}.json"
        path.write_text(json.dumps(existing(root) + items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"added {sum(len(v) for v in added.values())} questions into {len(added)} root files")


def defaultdict_list():
    from collections import defaultdict
    return defaultdict(list)


if __name__ == "__main__":
    main()
