"""Add a QuestionBank sheet (19 aequus questions) to a copy of the Word Power workbook."""
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

SOURCE = Path("/private/tmp/claude-501/-Users-arpit-Documents-claude-transcription-workspace/583ec6a4-edd8-4cd2-a679-113f05b63d47/scratchpad/word_power_made_easy_sessions_1_to_47.xlsx")
OUT = Path(__file__).resolve().parent / "word_power_made_easy_with_QuestionBank.xlsx"
ROOT = "aequus"

# (word, question, correct, three wrong options, explanation)
QUESTIONS = [
    ("equivocate", "When asked if the project would finish on time, the manager said, \"Well, that depends on many things,\" and never gave a clear answer. What did the manager do?",
     "Equivocated", ["Equated", "Equalized", "Equilibrated"],
     "Equi (equal) + voc (voice): using deliberately vague words to avoid a clear answer."),
    ("equality", "Under the law, ___ means every citizen has the same rights, whatever their background.",
     "Equality", ["Equanimity", "Equinox", "Equilibrium"],
     "Equality is the state of being equal. Equanimity is calm, equinox is equal day and night, equilibrium is balance."),
    ("equivocation", "\"I neither confirm nor deny the report, and I'm not saying it's false.\" This statement is an example of:",
     "Equivocation", ["Equilateral", "Equity", "Equinoctial"],
     "A deliberately vague statement that avoids a clear yes or no."),
    ("equivocal", "The mayor gave an ___ answer, so the reporters were still confused.",
     "Equivocal", ["Unequivocal", "Equable", "Equilateral"],
     "Equivocal means open to two meanings. Unequivocal (the trap) means clear with one meaning."),
    ("unequivocal", "The witness said, \"Yes, I saw him at nine o'clock,\" leaving no room for doubt. The answer was:",
     "Unequivocal", ["Equivocal", "Equitable", "Equinoctial"],
     "Un- (not) + equivocal: one clear meaning only."),
    ("equity", "Two runners start a race, but one gets a head start to make up for a slower leg. Which word describes this kind of fairness?",
     "Equity", ["Equality", "Equanimity", "Equinox"],
     "Equity is fairness that adjusts for different needs. Equality (the trap) gives everyone the same treatment."),
    ("equitable", "A rule that gives students with a disability extra time is best described as:",
     "Equitable", ["Equilateral", "Equable", "Equivocal"],
     "Equitable means fair and just to all. Equable (the trap) means calm in temper."),
    ("inequity", "A rule that pays men more than women for the same job shows an ___ in pay.",
     "Inequity", ["Equity", "Equinox", "Equilibrium"],
     "In- (not) + equity: the unfairness itself."),
    ("inequitable", "Which word describes a rule that treats students unfairly because of where they come from?",
     "Inequitable", ["Equitable", "Equable", "Equilateral"],
     "Unfair or unjust. Equitable is the opposite."),
    ("iniquity", "The villain's ___ shocked the whole town: he had poisoned the well everyone drank from.",
     "Iniquity", ["Equity", "Equilibrium", "Equanimity"],
     "Iniquity means wickedness, a much stronger word than inequity."),
    ("iniquitous", "The ___ scheme cheated poor families out of their homes.",
     "Iniquitous", ["Equitable", "Equable", "Unequivocal"],
     "Iniquitous means wicked or sinful."),
    ("equinox", "On the day of the spring ___, day and night last about the same length.",
     "Equinox", ["Equivocation", "Equanimity", "Equilateral"],
     "The equinox is the time when day and night are about equal in length."),
    ("equinoctial", "Which word describes storms that happen around the time of the equinox?",
     "Equinoctial", ["Equilateral", "Equable", "Equity"],
     "Equinoctial means relating to the equinox."),
    ("equanimity", "Even after losing the final, she accepted the result with calm and composure. Which word fits?",
     "Equanimity", ["Equivocation", "Equinox", "Equilibrium"],
     "Equanimity is calm, even temper, especially under stress."),
    ("equability", "Which word describes a steady, even-tempered calm that makes someone easy to work with?",
     "Equability", ["Equilibrium", "Equilateral", "Equivocation"],
     "Equability is evenness of temper. Equilibrium (the trap) is balance between forces."),
    ("equable", "He stayed ___ even when the crowd shouted at him.",
     "Equable", ["Equilateral", "Equinox", "Iniquitous"],
     "Equable means calm and unruffled."),
    ("equilibrium", "A tightrope walker keeps her body in ___ by moving her arms.",
     "Equilibrium", ["Equanimity", "Equity", "Equinox"],
     "Equilibrium is a balance between opposing forces."),
    ("equilibrist", "A tightrope walker in the circus is called an:",
     "Equilibrist", ["Equinoctial", "Equanimity", "Equity"],
     "An equilibrist is a performer who keeps their balance."),
    ("equilateral", "A triangle with all three sides the same length is called:",
     "Equilateral", ["Equilibrium", "Equivocal", "Equinox"],
     "Equi (equal) + latus (side): equal sides."),
]

# Why each option is right or wrong. Keyed by the option text.
RATIONALE = {
    "equivocate": {
        "Equivocated": "Correct: a deliberately vague answer to avoid yes or no.",
        "Equated": "Wrong: equate means to treat as equal; it has nothing to do with dodging a question.",
        "Equalized": "Wrong: equalize means to make things even, such as scores; it is not about vague speech.",
        "Equilibrated": "Wrong: equilibrate means to bring into balance; it describes balance, not speech.",
    },
    "equality": {
        "Equality": "Correct: the state of being equal, with the same rights for everyone.",
        "Equanimity": "Wrong: calm, even temper; it is about emotion, not rights.",
        "Equinox": "Wrong: the time when day and night are equal; it is not about rights.",
        "Equilibrium": "Wrong: a balance between opposing forces; it does not describe rights.",
    },
    "equivocation": {
        "Equivocation": "Correct: a statement that neither confirms nor denies, on purpose.",
        "Equilateral": "Wrong: a shape with equal sides; not about speech.",
        "Equity": "Wrong: fairness; the sentence is about vague speech, not fairness.",
        "Equinoctial": "Wrong: relating to the equinox; not about speech.",
    },
    "equivocal": {
        "Equivocal": "Correct: open to two meanings, so the reporters were confused.",
        "Unequivocal": "Wrong: means clear with one meaning, the opposite of what confused the reporters.",
        "Equable": "Wrong: calm, even-tempered; it does not describe a vague answer.",
        "Equilateral": "Wrong: a shape with equal sides; not about answers.",
    },
    "unequivocal": {
        "Unequivocal": "Correct: un- (not) + equivocal, so only one meaning is possible.",
        "Equivocal": "Wrong: open to two meanings; the sentence says there is no doubt.",
        "Equitable": "Wrong: fair and just; it does not describe how clear a statement is.",
        "Equinoctial": "Wrong: relating to the equinox; not about a witness's answer.",
    },
    "equity": {
        "Equity": "Correct: fairness that adjusts for different needs, like a head start.",
        "Equality": "Wrong: everyone gets the same treatment; the runners do not, so this is not equality.",
        "Equanimity": "Wrong: calm temper; the sentence is about fairness.",
        "Equinox": "Wrong: a time when day and night are equal; not about fairness.",
    },
    "equitable": {
        "Equitable": "Correct: fair and just to all, which extra time helps achieve.",
        "Equilateral": "Wrong: a shape with equal sides; not about fairness.",
        "Equable": "Wrong: calm temper; it does not describe a rule.",
        "Equivocal": "Wrong: open to two meanings; the rule is clear, not vague.",
    },
    "inequity": {
        "Inequity": "Correct: in- (not) + equity; the unfairness in pay.",
        "Equity": "Wrong: fairness itself; the sentence describes unfairness.",
        "Equinox": "Wrong: a time of year; not about pay.",
        "Equilibrium": "Wrong: balance; not about pay.",
    },
    "inequitable": {
        "Inequitable": "Correct: unfair or unjust, because of where students come from.",
        "Equitable": "Wrong: fair and just; the opposite of the rule described.",
        "Equable": "Wrong: calm temper; not about fairness.",
        "Equilateral": "Wrong: a shape with equal sides; not about fairness.",
    },
    "iniquity": {
        "Iniquity": "Correct: wickedness; poisoning a well is grossly wrong.",
        "Equity": "Wrong: fairness; too mild a word for poisoning a well.",
        "Equilibrium": "Wrong: balance; not about wickedness.",
        "Equanimity": "Wrong: calm temper; not about wickedness.",
    },
    "iniquitous": {
        "Iniquitous": "Correct: wicked and sinful, as a scheme that cheats families.",
        "Equitable": "Wrong: fair and just; cheating families is the opposite.",
        "Equable": "Wrong: calm temper; the scheme is wicked, not calm.",
        "Unequivocal": "Wrong: clear with one meaning; not about wickedness.",
    },
    "equinox": {
        "Equinox": "Correct: the spring time when day and night are about equal in length.",
        "Equivocation": "Wrong: vague speech; not a time of year.",
        "Equanimity": "Wrong: calm composure; not a time of year.",
        "Equilateral": "Wrong: a shape with equal sides; not a time of year.",
    },
    "equinoctial": {
        "Equinoctial": "Correct: relating to the equinox, as in the storms in the sentence.",
        "Equilateral": "Wrong: a shape with equal sides; not about storms.",
        "Equable": "Wrong: calm temper; not about storms.",
        "Equity": "Wrong: fairness; not about storms.",
    },
    "equanimity": {
        "Equanimity": "Correct: calm composure after bad news or a loss.",
        "Equivocation": "Wrong: vague speech; the sentence describes calm, not speech.",
        "Equinox": "Wrong: a time of year; not about calm.",
        "Equilibrium": "Wrong: balance of forces; it is physical or general, not calm under stress.",
    },
    "equability": {
        "Equability": "Correct: a steady, even-tempered calm that makes someone easy to work with.",
        "Equilibrium": "Wrong: balance of forces; not a temper.",
        "Equilateral": "Wrong: a shape with equal sides; not a temper.",
        "Equivocation": "Wrong: vague speech; not a temper.",
    },
    "equable": {
        "Equable": "Correct: calm and unruffled, even when shouted at.",
        "Equilateral": "Wrong: a shape with equal sides; not about temper.",
        "Equinox": "Wrong: a time of year; not about temper.",
        "Iniquitous": "Wrong: wicked; the sentence describes calm, not wickedness.",
    },
    "equilibrium": {
        "Equilibrium": "Correct: balance between opposing forces, as a tightrope walker needs.",
        "Equanimity": "Wrong: emotional calm; the sentence is about physical balance.",
        "Equity": "Wrong: fairness; not about balance.",
        "Equinox": "Wrong: a time when day and night are equal; not about balance of a body.",
    },
    "equilibrist": {
        "Equilibrist": "Correct: a performer who keeps balance, such as a tightrope walker.",
        "Equinoctial": "Wrong: relating to the equinox; not a performer.",
        "Equanimity": "Wrong: calm temper; not a performer.",
        "Equity": "Wrong: fairness; not a performer.",
    },
    "equilateral": {
        "Equilateral": "Correct: equi (equal) + latus (side), so all three sides are equal.",
        "Equilibrium": "Wrong: balance; not about sides.",
        "Equivocal": "Wrong: open to two meanings; not about shapes.",
        "Equinox": "Wrong: a time when day and night are equal; not about shapes.",
    },
}


def main():
    wb = load_workbook(SOURCE)
    words = wb["Words"]
    # Check every word is in the sheet with the aequus root, so the bank matches the workbook.
    in_sheet = {}
    for row in words.iter_rows(min_row=2, values_only=True):
        if row[2] and row[4] and ROOT in str(row[4]).split(", "):
            in_sheet[row[2]] = True
    assert len(in_sheet) == 19, len(in_sheet)
    for word, *_ in QUESTIONS:
        assert word in in_sheet, word

    if "QuestionBank" in wb.sheetnames:
        del wb["QuestionBank"]
    ws = wb.create_sheet("QuestionBank")
    headers = ["Q No", "Root", "Word", "Question", "Option A", "Option B", "Option C", "Option D",
               "Correct answer", "Explanation", "Why each option is right or wrong"]
    ws.append(headers)
    letters = "ABCD"
    for i, (word, question, correct, wrong, why) in enumerate(QUESTIONS):
        pos = i % 4  # spread the correct answer across A to D
        options = list(wrong)
        options.insert(pos, correct)
        reasons = RATIONALE[word]
        why_each = "\n".join(
            f"{letters[j]}. {opt}: {reasons[opt]}" for j, opt in enumerate(options)
        )
        ws.append([i + 1, ROOT, word, question, *options, letters[pos], why, why_each])

    font = "Arial"
    fill = PatternFill("solid", fgColor="D9E1F2")
    thin = Side(style="thin", color="BFBFBF")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    widths = {"A": 7, "B": 10, "C": 16, "D": 60, "E": 16, "F": 16, "G": 16, "H": 16, "I": 14, "J": 60, "K": 80}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows():
        for cell in row:
            cell.font = Font(name=font, size=11, bold=cell.row == 1)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = border
            if cell.row == 1:
                cell.fill = fill
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    wb.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
