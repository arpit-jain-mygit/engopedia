"""Build chapter-wise Wren & Martin practice tests in several formats.

Reads backend/data/wren_martin.json (made by scripts/export_wren_martin.py) and writes:

  question_bank/grammar/tests/wren-martin-chapter-tests.md   printable tests, one section per chapter,
                                                             with an answer key at the end
  question_bank/grammar/tests/wren-martin-test-bank.xlsx     every item with a Format column, so a
                                                             student can filter and build their own test

Formats (each item is built from a workbook question, so no new facts are invented):
  A. Multiple choice        the question and four options, as in the workbook
  B. Fill in the blank      sentences from the book's fill-in exercises (stem with a blank, answer = the word)
  C. True or False          the same blank sentence with the right word (True) or a wrong option (False)
  D. Write the answer       the question with the options hidden; the answer is the correct option

B and C only exist for chapters whose workbook rows are fill-in sentences (25, 26, 38, 40, 41).
"""
import json
import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "backend" / "data" / "wren_martin.json"
OUT_DIR = Path(__file__).resolve().parent / "tests"
MD_OUT = OUT_DIR / "wren-martin-chapter-tests.md"
XLSX_OUT = OUT_DIR / "wren-martin-test-bank.xlsx"
LETTERS = "ABCD"

# How many items of each format go into one chapter's printed test.
PER_CHAPTER = {"A": 10, "B": 8, "C": 8, "D": 8}
BLANK = "___"
BLANK_RE = re.compile(r"_{3,}")  # the workbook writes blanks as 3 or 4 underscores
# Stems that point at answer options ("Which of these...", "Choose...") cannot be answered without them.
OPTION_REFERENCE = re.compile(r"\b(which|choose|select|following|of these)\b", re.I)
INSTRUCTION = re.compile(r"^(Choose the correct form|Fill in)[^:]*:\s*")


def spread(items, k):
    """Pick k items spread evenly across the list, so a test covers the whole chapter."""
    if len(items) <= k:
        return list(items)
    step = len(items) / k
    return [items[int(i * step)] for i in range(k)]


def blank_sentence(stem):
    """Return the sentence with the blank, without the instruction prefix, e.g. 'The earth ____ round.'"""
    return INSTRUCTION.sub("", stem, count=1).strip()


def true_false_items(q):
    """One True and one False statement per blank question (the False one uses a wrong option)."""
    sentence = blank_sentence(q["stem"])
    right = q["options"][q["correct"]]
    wrong = [o for i, o in enumerate(q["options"]) if i != q["correct"]]
    return [
        {"statement": BLANK_RE.sub(right, sentence), "answer": "True",
         "explanation": f"The right word for the blank is '{right}'."},
        {"statement": BLANK_RE.sub(wrong[0], sentence), "answer": "False",
         "explanation": f"'{wrong[0]}' is wrong here; the right word is '{right}'."},
    ]


def build_items(questions):
    """Return {chapter: {format: [items]}} with every item the bank can offer, in workbook order."""
    by_chapter = {}
    for q in questions:
        ch = by_chapter.setdefault(q["chapter"], {"A": [], "B": [], "C": [], "D": [], "blank": [], "plain": []})
        is_blank = BLANK in q["stem"]
        (ch["blank"] if is_blank else ch["plain"]).append(q)
    out = {}
    for chapter, ch in by_chapter.items():
        out[chapter] = {
            "A": [{"stem": q["stem"], "options": q["options"], "answer": LETTERS[q["correct"]],
                   "answer_text": q["options"][q["correct"]], "explanation": q["explanation"],
                   "source": q["source"], "exercise": q["exercise"]} for q in ch["plain"]],
            "B": [{"stem": blank_sentence(q["stem"]), "answer": q["options"][q["correct"]],
                   "explanation": q["explanation"], "source": q["source"], "exercise": q["exercise"]}
                  for q in ch["blank"]],
            "C": [dict(item, source=q["source"], exercise=q["exercise"])
                  for q in ch["blank"] for item in true_false_items(q)],
            # Write-the-answer only uses questions that make sense without their options.
            "D": [{"stem": q["stem"], "answer": q["options"][q["correct"]], "explanation": q["explanation"],
                   "source": q["source"], "exercise": q["exercise"]} for q in ch["plain"]
                  if not OPTION_REFERENCE.search(q["stem"])],
        }
    return out


def pick_test(chapter_items):
    """Choose the printed test for one chapter. Fill-in and True/False use blank sentences; the rest use plain questions."""
    test = {}
    test["A"] = spread(chapter_items["A"], PER_CHAPTER["A"])
    test["D"] = spread(chapter_items["D"], PER_CHAPTER["D"])
    fill = spread(chapter_items["B"], PER_CHAPTER["B"])
    test["B"] = fill
    # True/False must not reuse a sentence already used in the fill-in section.
    fill_keys = {b["stem"] for b in fill}
    tf_pool = [c for c in chapter_items["C"] if c["statement"] not in fill_keys]
    test["C"] = spread(tf_pool, PER_CHAPTER["C"])
    return test


def write_markdown(tests, titles):
    lines = [
        "# Wren & Martin: Chapter-wise Practice Tests",
        "",
        "How to use: pick a chapter, then write your answers on paper. Each chapter has up to four parts:",
        "",
        "- **Part A - Multiple choice:** choose A, B, C or D.",
        "- **Part B - Fill in the blank:** write the missing word.",
        "- **Part C - True or False:** write True or False.",
        "- **Part D - Write the answer:** the question is complete on its own. Write the answer (a word or a short phrase). No options are given.",
        "",
        "Chapters 25, 26, 38, 40 and 41 have all four parts. The other chapters have Parts A and D, because their book exercises are not fill-in sentences.",
        "",
        "The answer key is at the end. Check your answers only after you finish the test.",
        "",
        "---",
        "",
    ]
    answers = ["# Answer key", ""]
    for chapter in sorted(tests):
        t = tests[chapter]
        title = titles[chapter]
        lines += [f"## Chapter {chapter}: {title}", ""]
        answers += [f"## Chapter {chapter}: {title}", ""]
        n = 0
        if t["A"]:
            lines += ["### Part A - Multiple choice", ""]
            for item in t["A"]:
                n += 1
                lines.append(f"{n}. {item['stem']}")
                for letter, option in zip(LETTERS, item["options"]):
                    lines.append(f"   - {letter}. {option}")
                lines.append("")
                answers.append(f"- Q{n} (A): {item['answer']}. {item['answer_text']}")
            answers.append("")
        if t["B"]:
            lines += ["### Part B - Fill in the blank", ""]
            answers += [""]
            for item in t["B"]:
                n += 1
                lines.append(f"{n}. {item['stem']}")
                lines.append("")
                answers.append(f"- Q{n} (B): {item['answer']}")
            answers.append("")
        if t["C"]:
            lines += ["### Part C - True or False", ""]
            for item in t["C"]:
                n += 1
                lines.append(f"{n}. {item['statement']}  (True / False)")
                lines.append("")
                answers.append(f"- Q{n} (C): {item['answer']}")
            answers.append("")
        if t["D"]:
            lines += ["### Part D - Write the answer", ""]
            for item in t["D"]:
                n += 1
                lines.append(f"{n}. {item['stem']}")
                lines.append("")
                answers.append(f"- Q{n} (D): {item['answer']}")
            answers.append("")
        lines += ["---", ""]
    return "\n".join(lines + answers) + "\n"


def write_bank(items_by_chapter, titles):
    wb = Workbook()
    ws = wb.active
    ws.title = "TestBank"
    headers = ["Chapter", "Chapter Title", "Format", "Question", "Option A", "Option B", "Option C",
               "Option D", "Answer", "Explanation", "Source"]
    ws.append(headers)
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    fmt_name = {"A": "Multiple choice", "B": "Fill in the blank", "C": "True or False", "D": "Write the answer"}
    for chapter in sorted(items_by_chapter):
        for fmt in "ABCD":
            for item in items_by_chapter[chapter][fmt]:
                if fmt == "A":
                    question, options, answer = item["stem"], item["options"], item["answer"]
                elif fmt == "B":
                    question, options, answer = item["stem"], ["", "", "", ""], item["answer"]
                elif fmt == "C":
                    question, options, answer = item["statement"], ["", "", "", ""], item["answer"]
                else:
                    question, options, answer = item["stem"], ["", "", "", ""], item["answer"]
                ws.append([chapter, titles[chapter], fmt_name[fmt], question, *options, answer,
                           item["explanation"], f"{item['source']} {item['exercise']}".strip()])
    for col, width in zip("ABCDEFGHIJK", [9, 30, 18, 70, 24, 24, 24, 24, 16, 50, 30]):
        ws.column_dimensions[col].width = width
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    wb.save(XLSX_OUT)


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    titles = {c["chapter"]: c["title"] for c in data["chapters"]}
    items = build_items(data["questions"])
    tests = {ch: pick_test(items[ch]) for ch in items}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MD_OUT.write_text(write_markdown(tests, titles), encoding="utf-8")
    write_bank(items, titles)
    total = sum(len(t["A"]) + len(t["B"]) + len(t["C"]) + len(t["D"]) for t in tests.values())
    bank = sum(len(v[f]) for v in items.values() for f in "ABCD")
    print(f"tests: {len(tests)} chapters, {total} items -> {MD_OUT}")
    print(f"bank: {bank} rows -> {XLSX_OUT}")


if __name__ == "__main__":
    main()
