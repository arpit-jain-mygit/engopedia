"""Build the Wren & Martin grammar question workbook, chapter by chapter.

Each question has a Source: "Book" (an exercise printed in the book) or "Generated".
Layout follows the Word Wizard QuestionBank sheet: question, four options, correct letter,
explanation and a reason for each option.

Usage: backend/.venv/bin/python question_bank/grammar/build_wren_martin.py
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

HERE = Path(__file__).resolve().parent
OUT = HERE / "wren_martin_grammar_questions.xlsx"
LETTERS = "ABCD"

# Each chapter: (chapter number, chapter title, [questions])
# A question: (source, exercise, stem, [A, B, C, D], correct letter, explanation, [reason A, B, C, D])
CHAPTERS = [
    (1, "The Sentence", [
        ("Generated", "", "Which of these is a declarative (assertive) sentence?",
         ["Where do you live?", "Humpty Dumpty sat on a wall.", "Be quiet.", "What a shame!"], "B",
         "A declarative sentence makes a statement.",
         ["Wrong: it asks a question (interrogative).",
          "Correct: it makes a statement (declarative).",
          "Wrong: it gives a command (imperative).",
          "Wrong: it expresses strong feeling (exclamatory)."]),
        ("Generated", "", "Which sentence is interrogative?",
         ["Close the door.", "How cold the night is!", "Did you finish your homework?", "The sun rises in the east."], "C",
         "An interrogative sentence asks a question and ends with a question mark.",
         ["Wrong: it is an imperative command.",
          "Wrong: it expresses strong feeling (exclamatory).",
          "Correct: it asks a question (interrogative).",
          "Wrong: it makes a statement (declarative)."]),
        ("Generated", "", "Which sentence is imperative?",
         ["He is very tall.", "Is he very tall?", "How tall he is!", "Have mercy upon us."], "D",
         "An imperative sentence expresses a command, request or entreaty.",
         ["Wrong: it makes a statement.",
          "Wrong: it asks a question.",
          "Wrong: it expresses strong feeling.",
          "Correct: it expresses an entreaty (imperative)."]),
        ("Generated", "", "Which sentence is exclamatory?",
         ["Where is the bus?", "The day is lovely.", "Open the window.", "What a lovely day!"], "D",
         "An exclamatory sentence expresses strong feeling.",
         ["Wrong: it asks a question.",
          "Wrong: it makes a plain statement.",
          "Wrong: it is a command.",
          "Correct: it expresses strong feeling (exclamatory)."]),
        ("Generated", "", "A group of words that makes complete sense is called a:",
         ["phrase", "clause", "sentence", "word"], "C",
         "A sentence is a group of words that makes complete sense.",
         ["Wrong: a phrase does not make complete sense.",
          "Wrong: a clause is part of a sentence.",
          "Correct: a group of words that makes complete sense is a sentence.",
          "Wrong: a single word is not a group of words."]),
        ("Generated", "", "Which of these is a sentence, not just a group of words?",
         ["in a corner", "under the tree", "Little Jack Horner sat in a corner.", "a wall"], "C",
         "Only the group that makes complete sense is a sentence.",
         ["Wrong: it is a phrase that does not make complete sense.",
          "Wrong: it is a phrase that does not make complete sense.",
          "Correct: it makes complete sense.",
          "Wrong: it is a single word."]),
        ("Generated", "", "The sentence \"Thank him.\" is which kind?",
         ["declarative", "interrogative", "imperative", "exclamatory"], "C",
         "It expresses a command. Its subject 'You' is understood.",
         ["Wrong: it does not make a statement.",
          "Wrong: it does not ask a question.",
          "Correct: it expresses a command (imperative).",
          "Wrong: it does not express strong feeling."]),
        ("Generated", "", "\"Please pass the salt.\" is which kind of sentence?",
         ["declarative", "interrogative", "imperative", "exclamatory"], "C",
         "A request is an imperative sentence.",
         ["Wrong: it is a request, not a statement.",
          "Wrong: it does not ask a question.",
          "Correct: it expresses a request (imperative).",
          "Wrong: it does not express strong feeling."]),
        ("Generated", "", "\"What a shame!\" is which kind of sentence?",
         ["declarative", "interrogative", "imperative", "exclamatory"], "D",
         "It expresses strong feeling.",
         ["Wrong: it is not a statement of fact.",
          "Wrong: it is not a question.",
          "Wrong: it is not a command.",
          "Correct: it expresses strong feeling (exclamatory)."]),
        ("Generated", "", "\"Where do you live?\" is which kind of sentence?",
         ["declarative", "interrogative", "imperative", "exclamatory"], "B",
         "It asks a question.",
         ["Wrong: it does not make a statement.",
          "Correct: it asks a question (interrogative).",
          "Wrong: it is not a command.",
          "Wrong: it does not express strong feeling."]),
    ]),
]


def chapter2_rows():
    """Chapter 2 comes from chapter2.py: book Exercise 1 items first, then generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter2
    rows = [(2, "Subject and Predicate", q) for q in chapter2.book_questions() + chapter2.generated_questions()]
    return rows


CHAPTER_TITLES = {3: "Phrase and Clause", 4: "Parts of Speech", 5: "The Noun: Kinds of Nouns", 6: "The Noun: Gender", 7: "The Noun: Number", 8: "The Noun: Case", 9: "The Adjective", 10: "Comparison of Adjectives", 11: "Adjectives Used as Nouns", 12: "Position of Adjectives", 13: "Correct Use of Some Adjectives", 14: "Articles", 15: "Personal Pronouns", 16: "Reflexive and Emphatic Pronouns", 17: "Demonstrative, Indefinite and Distributive Pronouns", 18: "Relative Pronouns", 19: "Interrogative Pronouns", 20: "Transitive and Intransitive Verbs", 21: "Verbs of Incomplete Predication", 22: "Active and Passive Voice", 23: "Mood", 25: "The Uses of the Present and Past Tenses", 26: "The Future", 28: "The Infinitive", 29: "The Participle", 38: "The Preposition", 40: "The Conjunction", 41: "Some Conjunctions and Their Uses", 42: "The Interjection", 43: "The Same Word Used as Different Parts of Speech"}


def chapter5_rows():
    """Chapter 5 from chapter5.py: Exercise in Grammar 3 items first, then generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter5
    return [(5, CHAPTER_TITLES[5], q) for q in chapter5.book_questions() + chapter5.generated_questions()]


def chapters6_9_rows():
    """Chapters 6-9 from chapters6_9.py: Exercise in Grammar 6 (chapter 9) plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapters6_9
    rows = [(9, CHAPTER_TITLES[9], q) for q in chapters6_9.book_questions()]
    rows += [(q["chapter"], CHAPTER_TITLES[q["chapter"]], q) for q in chapters6_9.generated_questions()]
    return rows


def chapter10_rows():
    """Chapter 10 from chapter10.py: Exercises 13, 15, 16 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter10
    rows = [(10, CHAPTER_TITLES[10], q) for q in chapter10.book_questions()]
    rows += [(10, CHAPTER_TITLES[10], q) for q in chapter10.generated_questions()]
    return rows


def chapters11_13_rows():
    """Chapters 11-13 from chapters11_13.py: generated questions only (no grammar exercise)."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapters11_13
    return [(q["chapter"], CHAPTER_TITLES[q["chapter"]], q) for q in chapters11_13.generated_questions()]


def chapters14_15_rows():
    """Chapters 14-15 from chapters14_15.py: Exercise in Grammar 25 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapters14_15
    rows = [(14, CHAPTER_TITLES[14], q) for q in chapters14_15.generated_questions(14)]
    rows += [(15, CHAPTER_TITLES[15], q) for q in chapters14_15.ex25_questions()]
    rows += [(15, CHAPTER_TITLES[15], q) for q in chapters14_15.generated_questions(15)]
    return rows


def chapter16_rows():
    """Chapter 16 from chapter16.py: Exercise in Grammar 28 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter16
    rows = [(16, CHAPTER_TITLES[16], q) for q in chapter16.ex28_questions() + chapter16.generated_questions()]
    return rows


def chapters17_19_rows():
    """Chapters 17-19 from chapters17_19.py: Exercise in Grammar 29 (chapter 18) plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapters17_19
    rows = [(18, CHAPTER_TITLES[18], q) for q in chapters17_19.ex29_questions()]
    for ch in (17, 18, 19):
        rows += [(ch, CHAPTER_TITLES[ch], q) for q in chapters17_19.generated_questions(ch)]
    return rows


def chapter20_rows():
    """Chapter 20 from chapter20.py: Exercise in Grammar 36 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter20
    return [(20, CHAPTER_TITLES[20], q) for q in chapter20.ex36_questions() + chapter20.generated_questions()]


def chapter22_rows():
    """Chapter 22 from chapter22.py: Exercise in Grammar 39 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter22
    return [(22, CHAPTER_TITLES[22], q) for q in chapter22.ex39_questions() + chapter22.generated_questions()]


def chapter23_rows():
    """Chapter 23 from chapter23.py: Exercise in Grammar 45 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter23
    return [(23, CHAPTER_TITLES[23], q) for q in chapter23.ex45_questions() + chapter23.generated_questions()]


def chapter25_rows():
    """Chapter 25 from chapter25.py: Exercises 46 and 47 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter25
    return [(25, CHAPTER_TITLES[25], q) for q in chapter25.book_questions() + chapter25.generated_questions()]


def chapter26_rows():
    """Chapter 26 from chapter26.py: Exercise in Grammar 48 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter26
    return [(26, CHAPTER_TITLES[26], q) for q in chapter26.book_questions() + chapter26.generated_questions()]


def chapter28_rows():
    """Chapter 28 from chapter28.py: Exercise in Grammar 49 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter28
    return [(28, CHAPTER_TITLES[28], q) for q in chapter28.ex49_questions() + chapter28.generated_questions()]


def chapter29_rows():
    """Chapter 29 from chapter29.py: Exercises 51 and 52 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter29
    return [(29, CHAPTER_TITLES[29], q) for q in chapter29.ex_questions() + chapter29.ex55_questions() + chapter29.generated_questions()]


def chapter22b_rows():
    """Chapter 22 continued: Exercise in Grammar 40 and Exercise 41 (passive conversion)."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter22b
    return [(22, CHAPTER_TITLES[22], q) for q in chapter22b.ex40_questions() + chapter22b.ex41_questions()]


def chapter38_rows():
    """Chapter 38 from chapter38.py: Exercises 64, 65 and 68 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter38
    return [(38, CHAPTER_TITLES[38], q) for q in chapter38.ex64_questions() + chapter38.ex65_questions() + chapter38.ex68_questions() + chapter38.ex69_questions() + chapter38.ex90_questions() + chapter38.generated_questions()]


def chapter40_rows():
    """Chapter 40 from chapter40.py: Exercises 96 and 97 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter40
    return [(40, CHAPTER_TITLES[40], q) for q in chapter40.ex96_questions() + chapter40.ex97_questions() + chapter40.ex98_questions() + chapter40.ex98b_questions() + chapter40.ex94_questions() + chapter40.generated_questions()]


def chapter41_rows():
    """Chapter 41 from chapter41.py: Exercise in Grammar 99 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter41
    return [(41, CHAPTER_TITLES[41], q) for q in chapter41.ex99_questions() + chapter41.ex100_questions() + chapter41.generated_questions()]


def chapter42_rows():
    """Chapter 42 from chapter42.py: generated questions only (no printed exercise in the book)."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter42
    return [(42, CHAPTER_TITLES[42], q) for q in chapter42.generated_questions()]


def chapter43_rows():
    """Chapter 43 from chapter43.py: questions from the book's word-list examples."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter43
    return [(43, CHAPTER_TITLES[43], q) for q in chapter43.word_questions() + chapter43.ex102_questions() + chapter43.ex103_questions()]


def chapter21_rows():
    """Chapter 21 from chapter21.py: Exercise in Grammar 38 plus generated questions."""
    import sys
    sys.path.insert(0, str(HERE))
    import chapter21
    return [(21, CHAPTER_TITLES[21], q) for q in chapter21.ex38_questions() + chapter21.generated_questions()]


def chapter34_rows():
    """Chapters 3 and 4: generated questions from generated_ch3_4.py (chapter 4's book exercise is pending)."""
    import sys
    sys.path.insert(0, str(HERE))
    import generated_ch3_4
    return [(q["chapter"], CHAPTER_TITLES[q["chapter"]], q) for q in generated_ch3_4.questions()]


def build():
    wb = Workbook()
    ws = wb.active
    ws.title = "QuestionBank"
    header = ["Q No", "Chapter No", "Chapter", "Source", "Exercise", "Question",
              "Option A", "Option B", "Option C", "Option D", "Correct answer", "Explanation",
              "Why each option is right or wrong"]
    ws.append(header)
    qno = 0
    for ch_no, ch_title, questions in CHAPTERS:
        for source, exercise, stem, options, correct, explanation, reasons in questions:
            qno += 1
            why = "\n".join(f"{L}. {options[i]}: {reasons[i]}" for i, L in enumerate(LETTERS))
            ws.append([qno, ch_no, ch_title, source, exercise, stem, *options, correct, explanation, why])
    for ch_no, ch_title, q in chapter2_rows() + chapter34_rows() + chapter5_rows() + chapters6_9_rows() + chapter10_rows() + chapters11_13_rows() + chapters14_15_rows() + chapter16_rows() + chapters17_19_rows() + chapter20_rows() + chapter21_rows() + chapter22_rows() + chapter23_rows() + chapter25_rows() + chapter26_rows() + chapter28_rows() + chapter29_rows() + chapter22b_rows() + chapter38_rows() + chapter40_rows() + chapter41_rows() + chapter42_rows() + chapter43_rows():
        qno += 1
        why = "\n".join(f"{L}. {q['options'][i]}: {q['reasons'][i]}" for i, L in enumerate(LETTERS))
        ws.append([qno, ch_no, ch_title, q["source"], q["exercise"], q["stem"], *q["options"],
                   q["correct"], q["explanation"], why])

    thin = Side(style="thin", color="BFBFBF")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    widths = {"A": 7, "B": 11, "C": 22, "D": 12, "E": 12, "F": 60, "G": 22, "H": 22, "I": 22,
              "J": 22, "K": 14, "L": 50, "M": 90}
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
    print(f"questions written: {qno}")


if __name__ == "__main__":
    build()
