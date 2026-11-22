"""Chapter 10 (Comparison of Adjectives): Exercises in Grammar 13, 15 and 16 plus generated questions.

Answers come from the answer key: page 5 (Exercises 13 and 15) and page 6 (Exercise 16).
Distractors are other forms or degrees from the same exercise.
"""

LETTERS = "ABCD"
DEGREES = ["Positive", "Comparative", "Superlative"]
NO_DEGREE = "No degree of comparison"

# Exercise 13: (word, comparative, superlative), as in the key.
EX13 = [
    ("black", "blacker", "blackest"), ("excellent", "more excellent", "most excellent"),
    ("ill", "worse", "worst"), ("gloomy", "gloomier", "gloomiest"), ("mad", "madder", "maddest"),
    ("safe", "safer", "safest"), ("bad", "worse", "worst"), ("unjust", "more unjust", "most unjust"),
    ("gay", "gayer", "gayest"), ("able", "abler", "ablest"), ("dry", "drier", "driest"),
    ("timid", "more timid", "most timid"), ("ugly", "uglier", "ugliest"), ("true", "truer", "truest"),
    ("severe", "more severe", "most severe"), ("exact", "more exact", "most exact"),
    ("agreeable", "more agreeable", "most agreeable"), ("difficult", "more difficult", "most difficult"),
    ("little", "less", "least"), ("few", "fewer", "fewest"), ("numerous", "more numerous", "most numerous"),
    ("merry", "merrier", "merriest"),
]

# Exercise 16: (word, comparative, superlative), as in the key (pleasant has two forms, so it is left out).
EX16 = [
    ("shameful", "more shameful", "most shameful"), ("clever", "cleverer", "cleverest"),
    ("pretty", "prettier", "prettiest"), ("interesting", "more interesting", "most interesting"),
    ("hopeful", "more hopeful", "most hopeful"), ("honest", "more honest", "most honest"),
    ("important", "more important", "most important"), ("patient", "more patient", "most patient"),
    ("rude", "ruder", "rudest"), ("delightful", "more delightful", "most delightful"),
    ("stupid", "more stupid", "most stupid"), ("attractive", "more attractive", "most attractive"),
    ("heavy", "heavier", "heaviest"), ("beautiful", "more beautiful", "most beautiful"),
    ("fortunate", "more fortunate", "most fortunate"),
]

# Exercise 15: (item, sentence, adjective, degree as in the key).
EX15 = [
    (1, "The poor woman had seen happier days.", "poor", "Positive"),
    (1, "The poor woman had seen happier days.", "happier", "Comparative"),
    (3, "Make less noise.", "less", "Comparative"),
    (4, "That child has a slight cold.", "slight", "Positive"),
    (5, "A live ass is stronger than a dead lion.", "stronger", "Comparative"),
    (7, "Solomon was one of the wisest men.", "wisest", "Superlative"),
    (8, "Hunger is the best sauce.", "best", "Superlative"),
    (9, "His simple word is as good as an oath.", "simple", "Positive"),
    (9, "His simple word is as good as an oath.", "good", "Positive"),
    (10, "There was not the slightest excuse for it.", "slightest", "Superlative"),
    (11, "My knife is sharper than yours.", "sharper", "Comparative"),
    (12, "Small people love to talk of great men.", "Small", "Positive"),
    (12, "Small people love to talk of great men.", "great", "Positive"),
    (13, "Of two evils choose the less.", "less", "Comparative"),
    (19, "Hari is the idlest boy in the class.", "idlest", "Superlative"),
    (20, "I promise you a fair hearing.", "fair", "Positive"),
    (22, "He gave the boys much wholesome advice.", "wholesome", "Positive"),
    (23, "He thinks he is wiser than his father.", "wiser", "Comparative"),
    (24, "No news is good news.", "good", "Positive"),
    (25, "Bangladesh has the largest tea garden in the world.", "largest", "Superlative"),
    (26, "Lead is heavier than any other metal.", "heavier", "Comparative"),
    (27, "I congratulated him on his good fortune.", "good", "Positive"),
    (28, "He has many powerful friends.", "powerful", "Positive"),
    (29, "The longest lane has a turning.", "longest", "Superlative"),
]

GENERATED = [
    ("The comparative of 'good' is:", "better", ["gooder", "goodest", "best"],
     "'Better' is the irregular comparative of 'good'.", ["Correct: 'better' is the comparative of 'good'.", "Wrong: 'gooder' is not a standard form.", "Wrong: 'goodest' is a superlative-style form, not a comparative.", "Wrong: 'best' is the superlative of 'good'."]),
    ("The superlative of 'bad' is:", "worst", ["worse", "baddest", "most bad"],
     "'Worst' is the irregular superlative of 'bad'.", ["Correct: 'worst' is the superlative of 'bad'.", "Wrong: 'worse' is the comparative.", "Wrong: 'baddest' is not standard.", "Wrong: 'most bad' is not the standard form."]),
    ("The comparative of 'many' is:", "more", ["manier", "most", "many"],
     "'More' is the comparative of 'many' and 'much'.", ["Correct: 'more' is the comparative of 'many'.", "Wrong: 'manier' is not a word.", "Wrong: 'most' is a superlative.", "Wrong: 'many' is the positive form."]),
    ("The correct superlative of 'beautiful' is:", "most beautiful", ["beautifullest", "more beautiful", "beautifuler"],
     "Long adjectives form the superlative with 'most'.", ["Correct: long adjectives use 'most'.", "Wrong: 'beautifullest' is not a word.", "Wrong: 'more beautiful' is the comparative.", "Wrong: 'beautifuler' is not a word."]),
    ("The comparative of 'little' is:", "less", ["littler", "littlest", "least"],
     "'Less' is the comparative of 'little' (amount).", ["Correct: 'less' is the comparative of 'little'.", "Wrong: 'littler' is not used for amount.", "Wrong: 'littlest' is a superlative form.", "Wrong: 'least' is the superlative."]),
    ("In 'Iron is the most useful of all metals.', the adjective is in the:", "Superlative", ["Positive", "Comparative", NO_DEGREE],
     "'Most useful ... of all' compares one thing with all others: superlative.", ["Correct: it compares one thing with all others.", "Wrong: the positive is not comparing.", "Wrong: the comparative compares two things.", "Wrong: it does have a degree of comparison."]),
    ("In 'Mohan is taller than Ram.', the adjective is in the:", "Comparative", ["Positive", "Superlative", NO_DEGREE],
     "'Taller than' compares two things: comparative.", ["Wrong: the positive does not compare.", "Correct: it compares two things.", "Wrong: the superlative compares many.", "Wrong: it does have a degree of comparison."]),
    ("The positive form of 'happier' is:", "happy", ["happiest", "more happy", "happiness"],
     "'Happy' is the base (positive) form.", ["Correct: 'happy' is the positive form.", "Wrong: 'happiest' is the superlative.", "Wrong: 'more happy' is not standard.", "Wrong: 'happiness' is a noun."]),
    ("The superlative of 'late' (time) is:", "latest", ["lately", "later", "last"],
     "'Latest' refers to time; 'last' refers to position.", ["Correct: 'latest' is the superlative of 'late' for time.", "Wrong: 'lately' is an adverb.", "Wrong: 'later' is the comparative.", "Wrong: 'last' refers to position, not time."]),
    ("Which word is in the positive degree?", "tall", ["taller", "tallest", "tallness"],
     "'Tall' is the base form and does not compare.", ["Correct: 'tall' is the base (positive) form.", "Wrong: 'taller' is the comparative.", "Wrong: 'tallest' is the superlative.", "Wrong: 'tallness' is a noun."]),
]


def _rotate(items, pos):
    """Put the first item at position pos; keep the others in order."""
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def _question(n, stem, correct, wrong, explanation, reasons):
    pos = n % 4
    options = [correct] + wrong
    rs = [reasons[0]] + reasons[1:]
    return {"source": "Book", "exercise": "", "stem": stem, "options": _rotate(options, pos),
            "correct": LETTERS[pos], "explanation": explanation, "reasons": _rotate(rs, pos)}


def book_questions():
    out = []
    n = 0
    # Exercise 13: comparative and superlative for each word.
    for word, comp, sup in EX13:
        for degree, correct in (("comparative", comp), ("superlative", sup)):
            other = [x[1] if degree == "comparative" else x[2] for x in EX13 if x[0] != word]
            wrong = [o for o in other if o not in (comp, sup)][:3]
            n_stem = f"What is the {degree} of '{word}'?"
            reasons = [f"Correct: '{correct}' is the {degree} of '{word}'."] + \
                      [f"Wrong: '{w}' is not the {degree} of '{word}'." for w in wrong]
            q = _question(n, n_stem, correct, wrong, f"The {degree} of '{word}' is '{correct}'.", reasons)
            q["exercise"] = "Exercise in Grammar 13"
            out.append(q)
            n += 1
    # Exercise 16: comparative and superlative for each word in the table.
    for word, comp, sup in EX16:
        for degree, correct in (("comparative", comp), ("superlative", sup)):
            other = [x[1] if degree == "comparative" else x[2] for x in EX16 if x[0] != word]
            wrong = [o for o in other if o not in (comp, sup)][:3]
            reasons = [f"Correct: '{correct}' is the {degree} of '{word}'."] + \
                      [f"Wrong: '{w}' is not the {degree} of '{word}'." for w in wrong]
            q = _question(n, f"What is the {degree} of '{word}'?", correct, wrong,
                          f"The {degree} of '{word}' is '{correct}'.", reasons)
            q["exercise"] = "Exercise in Grammar 16"
            out.append(q)
            n += 1
    # Exercise 15: name the degree of the adjective in each sentence.
    for item, sentence, adj, degree in EX15:
        wrong = [d for d in DEGREES + [NO_DEGREE] if d != degree]
        correct_reason = f"Correct: '{adj}' is in the {degree.lower()} degree." if degree in DEGREES else ""
        reasons = [f"Correct: '{adj}' is in the {degree.lower()} degree."] + \
                  [f"Wrong: '{adj}' is in the {degree.lower()} degree." if w in DEGREES else
                   f"Wrong: '{adj}' does have a degree of comparison." for w in wrong]
        q = _question(n, f'In "{sentence}", what degree is "{adj}"?', degree, wrong,
                      f"'{adj}' is in the {degree.lower()} degree.", reasons)
        q["exercise"] = f"Exercise in Grammar 15, item {item}"
        out.append(q)
        n += 1
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GENERATED):
        q = _question(n, stem, correct, wrong, expl, reasons)
        q["source"] = "Generated"
        q["exercise"] = ""
        out.append(q)
    return out
