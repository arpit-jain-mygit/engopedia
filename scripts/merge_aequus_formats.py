"""Replace the aequus questions in backend/data/quiz.json with the nine-format set.

build_quiz_db.py regenerates quiz.json from the workbook and would bring back the
old template questions, so run this script again after any regeneration:

    python3 scripts/merge_aequus_formats.py
"""
import json
from pathlib import Path

QUIZ = Path(__file__).resolve().parent.parent / "backend" / "data" / "quiz.json"
ROOT = "aequus"


def choice(fmt, n, prompt, choices, answer, good, try_, **extra):
    return {"id": f"aequus-q{n:02d}", "format": fmt, "prompt": prompt, "choices": choices,
            "answer": answer, "hint": "", "good": good, "try": try_, **extra}


QUESTIONS = [
    choice("emoji", 1,
           "Asked a direct yes-or-no question, the manager replied in words that could be read either way, so no one could pin him down. Which verb describes what he did?",
           ["Equivocated", "Equated", "Equalized", "Equilibrated"], 0,
           "Equi (equal) + voc (voice): speaking so that two readings are possible, to avoid a clear answer.",
           "Think about speech that keeps two meanings open.", scene="🤷"),
    {"id": "aequus-q02", "format": "build",
     "prompt": "Tap the tiles in order to build the word for: every citizen counts the same before the law.",
     "tiles": ["equ", "al", "ity", "ivo", "ine"], "target": "equality", "hint": "",
     "good": "Equality is the state of being equal.", "try": "Equ, then a sound that means the same, then ity."},
    {"id": "aequus-q03", "format": "type",
     "prompt": "A minister, asked whether he approved the plan, said he 'would look at it carefully' and added nothing more. Type the noun for this deliberately unclear speech.",
     "target": "equivocation", "hint": "Starts with \"equ\", 12 letters.",
     "good": "Equi (equal) + voc (voice): a deliberately vague statement.",
     "try": "It is the noun form of equivocate."},
    choice("hear", 4,
           "Listen, then choose the word that completes the sentence.",
           ["Unequivocal", "Equable", "Equilateral", "Equivocal"], 3,
           "Equivocal means open to two meanings. Unequivocal means clear, with one meaning.",
           "Two readings means the answer is open to both.",
           speak="Two reporters read the mayor's sentence in opposite ways, because his wording could support both readings."),
    choice("odd", 5,
           "Which word is the odd one out? It is NOT about clear or vague speech.",
           ["Unequivocal", "Equivocal", "Equitable", "Equinoctial"], 2,
           "Equitable means fair and just to all. The other three describe clarity of speech or a time of year.",
           "Ask which word is about fairness, not speech."),
    {"id": "aequus-q06", "format": "match",
     "prompt": "Match each word to its meaning.",
     "pairs": [["Equity", "Fairness that adjusts for different needs"],
               ["Equality", "The same treatment for everyone"],
               ["Equanimity", "Calm, even temper under stress"],
               ["Equinox", "Day and night last about the same length"]],
     "hint": "",
     "good": "Equity adjusts for need, equality gives the same treatment, equanimity is calm, and equinox is the equal day and night.",
     "try": "Check the pairs that do not fit."},
    choice("tf", 7,
           "\"Equitable means calm and unruffled.\"",
           ["True", "False"], 1,
           "Equitable means fair and just to all. Equable means calm and unruffled.",
           "Compare with equable, the calm word."),
    choice("scenario", 8,
           "A company pays men more than women for the same job. This unfairness in pay is an:",
           ["Equity", "Equinox", "Equilibrium", "Inequity"], 3,
           "In- (not) + equity: the unfairness itself.",
           "The prefix in- means not.", scene="💼 💰"),
    {"id": "aequus-q09", "format": "two",
     "prompt": "Step 1: what does the prefix in- mean?",
     "stages": [
         {"prompt": "Step 1: what does the prefix in- mean?", "choices": ["Not", "Again", "Under", "Across"],
          "answer": 0, "good": "In- means not."},
         {"prompt": "A school admissions rule treats applicants unfairly because of their postcode. The rule is:",
          "choices": ["Inequitable", "Equitable", "Equable", "Equilateral"], "answer": 0,
          "good": "In- (not) + equitable: unfair or unjust."},
     ],
     "hint": "", "good": "In- (not) + equitable: unfair or unjust.", "try": "Step 1 is in-, which means not."},
    choice("emoji", 10,
           "The villain poisoned the well that the whole town drank from. His act was an example of:",
           ["Equity", "Iniquity", "Equilibrium", "Equanimity"], 1,
           "Iniquity means wickedness, a much stronger word than inequity.",
           "Think of the strongest word for wickedness.", scene="😈"),
    {"id": "aequus-q11", "format": "build",
     "prompt": "Tap the tiles in order to build the word for: a property scheme that was wicked in every detail.",
     "tiles": ["ini", "quit", "ous", "equ", "al"], "target": "iniquitous", "hint": "",
     "good": "Iniquitous means wicked or sinful.", "try": "Start with ini, then quit, then ous."},
    {"id": "aequus-q12", "format": "type",
     "prompt": "In late March, day and night last about the same length. Type the name of this moment of the year.",
     "target": "equinox", "hint": "Starts with \"equ\", 7 letters.",
     "good": "The equinox is the moment when day and night are about equal in length.",
     "try": "It is a date in spring or autumn."},
    choice("hear", 13,
           "Listen, then choose the word for these storms.",
           ["Equinoctial", "Equilateral", "Equable", "Equity"], 0,
           "Equinoctial means relating to the equinox.",
           "They are named after the equinox.",
           speak="Sailors in the Atlantic expect violent storms around March and September, when day and night are of similar length. What are these storms called?"),
    choice("odd", 14,
           "Which word is NOT about calm temper?",
           ["Equanimity", "Equable", "Equability", "Equinox"], 3,
           "Equinox is a time of year. The other three describe calm temper.",
           "Find the word that is about time."),
    {"id": "aequus-q15", "format": "match",
     "prompt": "Match each word to its meaning.",
     "pairs": [["Equability", "Steady, even-tempered calm"],
               ["Equable", "Calm and unruffled, even when provoked"],
               ["Equanimity", "Calm composure, especially under stress"],
               ["Equilibrium", "A balance between opposing forces"]],
     "hint": "",
     "good": "Each word is a calm or balanced state, but equilibrium is a physical balance, not a mood.",
     "try": "Check which word is about balance, not mood."},
    choice("tf", 16,
           "\"Equable means calm and unruffled.\"",
           ["True", "False"], 0,
           "Equable means calm and unruffled, even when provoked.",
           "Think about how calm the word sounds."),
    choice("scenario", 17,
           "A tightrope walker keeps her body steady by moving her arms, so that opposing forces stay in balance. She is maintaining her:",
           ["Equilibrium", "Equanimity", "Equity", "Equinox"], 0,
           "Equilibrium is a balance between opposing forces.",
           "The walker is balancing forces, not feelings.", scene="🤸 ⚖️"),
    {"id": "aequus-q18", "format": "two",
     "prompt": "Step 1: what does the prefix equi- mean?",
     "stages": [
         {"prompt": "Step 1: what does the prefix equi- mean?", "choices": ["Equal", "Wind", "Fire", "Stone"],
          "answer": 0, "good": "Equi- means equal."},
         {"prompt": "A performer walks a tightrope high above the crowd and never loses her footing. She is called an:",
          "choices": ["Equinoctial", "Equilibrist", "Equanimity", "Equity"], "answer": 1,
          "good": "An equilibrist is a performer who keeps their balance."},
     ],
     "hint": "", "good": "An equilibrist is a performer who keeps their balance.",
     "try": "Step 1 is equi-, which means equal."},
    choice("emoji", 19,
           "A triangle with three sides of exactly the same length is called:",
           ["Equilibrium", "Equivocal", "Equilateral", "Equinox"], 2,
           "Equi (equal) + latus (side): equal sides.",
           "Think of a triangle whose sides are equal.", scene="🔺"),
]


# Hint 2 for each aequus question (hint 1 and hint 3 are computed by the API).
# Clues never give the letter count or first letters, so they do not repeat hint 3.
HINTS = {
    "aequus-q01": "A manager was asked a yes-or-no question and answered in words that could mean either yes or no.",
    "aequus-q02": "Think of a fair law: every citizen is treated the same.",
    "aequus-q03": "It is the noun for deliberately vague speech that keeps two meanings open.",
    "aequus-q04": "Think of a sentence that two reporters could read in opposite ways.",
    "aequus-q05": "Only one word is about fairness. The other three are about speech or the calendar.",
    "aequus-q06": "Equinox is about the calendar, not a feeling.",
    "aequus-q07": "Equitable is about fairness. Check which meaning equable has.",
    "aequus-q08": "The word is the unfairness itself: add the prefix in- (not) to equity.",
    "aequus-q09": "Think of prefixes like in- in incomplete or invisible.",
    "aequus-q10": "A much stronger word for wickedness than inequity.",
    "aequus-q11": "Wicked or sinful: the adjective form of iniquity.",
    "aequus-q12": "The moment in March or September when day and night are about equal.",
    "aequus-q13": "Think of storms named after a moment in the calendar.",
    "aequus-q14": "Only one word is about the calendar. The other three describe a calm temper.",
    "aequus-q15": "Only one of these is a physical balance rather than a mood.",
    "aequus-q16": "Think about how calm the word sounds.",
    "aequus-q17": "The walker keeps forces in balance, not feelings.",
    "aequus-q18": "A performer who keeps their balance on a tightrope.",
    "aequus-q19": "Equi- means equal, and latus means side.",
}


REVIEW_XLSX = Path(__file__).resolve().parent.parent / "quiz_database.xlsx"
REVIEW_SHEET = "Aequus formats"


def answer_text(q):
    """The answer as plain text for the letter hint, or None for a pairing."""
    fmt = q["format"]
    if fmt == "two":
        last = q["stages"][-1]
        return last["choices"][last["answer"]]
    if fmt in ("build", "type"):
        return q["target"]
    if fmt == "match":
        return None
    return q["choices"][q["answer"]]


def offline_hints(q):
    """All three hints, built now and saved in the workbook for review. The API only reads them."""
    ans = answer_text(q)
    if ans is None:
        left, right = q["pairs"][0]
        hint3 = f'"{left}" means "{right}".'
    else:
        hint3 = f'It starts with "{ans[:3]}" and has {len(ans)} letters.'
    return {"hint1": f'The root "{ROOT}" means "equal".', "hint2": HINTS[q["id"]], "hint3": hint3}


def write_review_sheet(hints):
    """Save the nine-format questions and their hints in the workbook, one row per question."""
    from openpyxl import load_workbook
    wb = load_workbook(REVIEW_XLSX)
    if REVIEW_SHEET in wb.sheetnames:
        del wb[REVIEW_SHEET]
    ws = wb.create_sheet(REVIEW_SHEET)
    ws.append(["Question ID", "Format", "Prompt", "Answer", "Hint 1 (root)", "Hint 2 (clue)", "Hint 3 (letters)", "Reviewed"])
    for q in QUESTIONS:
        ws.append([q["id"], q["format"], q["prompt"], answer_text(q) or "(pairs)",
                   hints[q["id"]]["hint1"], hints[q["id"]]["hint2"], hints[q["id"]]["hint3"], ""])
    for col, width in zip("ABCDEFGH", (16, 12, 60, 18, 40, 60, 40, 12)):
        ws.column_dimensions[col].width = width
    wb.save(REVIEW_XLSX)


def read_review_sheet():
    """Hints as edited in the workbook, if the sheet exists. The workbook wins over the built-in text."""
    from openpyxl import load_workbook
    wb = load_workbook(REVIEW_XLSX, read_only=True)
    if REVIEW_SHEET not in wb.sheetnames:
        return {}
    rows = wb[REVIEW_SHEET].iter_rows(min_row=2, values_only=True)
    return {r[0]: {"hint1": r[4], "hint2": r[5], "hint3": r[6]} for r in rows if r[0]}


def main():
    edited = read_review_sheet()
    hints = {}
    for q in QUESTIONS:
        hints[q["id"]] = edited.get(q["id"]) or offline_hints(q)
        q.update(hints[q["id"]])
        q.pop("hint", None)
    write_review_sheet(hints)
    data = json.loads(QUIZ.read_text(encoding="utf-8"))
    others = [q for q in data["questions"] if q["root"] != ROOT]
    new = []
    for q in QUESTIONS:
        q.setdefault("root", ROOT)
        q["roots"] = [[ROOT, "equal"]]
        new.append(q)
    # Keep the aequus block where the old one sat, so the rest of the file keeps its order.
    first = next(i for i, q in enumerate(data["questions"]) if q["root"] == ROOT)
    head = [q for q in data["questions"][:first] if q["root"] != ROOT]
    tail = [q for q in data["questions"][first:] if q["root"] != ROOT]
    data["questions"] = head + new + tail
    QUIZ.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"aequus questions: {len(new)}; total questions: {len(data['questions'])}")


if __name__ == "__main__":
    main()
