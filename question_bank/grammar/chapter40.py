"""Chapter 40 (The Conjunction): Exercises 96 and 97 (fill in the blank) plus generated questions.

Answers: key page 37 (keyimg p-040). Only blanks with a single key answer are used; blanks where the key
gives alternatives (for example 'as/because') are left out so no question has two right answers.
"""

LETTERS = "ABCD"
POOL = ["and", "but", "or", "if", "unless", "till", "though", "that", "when", "because",
        "since", "as", "yet", "for", "lest", "whether", "than", "while", "until", "so that", "where", "before"]

# Exercise in Grammar 96: (item, sentence with blank, correct conjunction from key)
EX96 = [
    (1, "Be just ____ fear not.", "and"),
    (2, "I ran fast, ____ I missed the train.", "but"),
    (3, "He fled, ____ he was afraid.", "for"),
    (5, "____ you try, you will not succeed.", "Unless"),
    (6, "I am sure ____ he said so.", "that"),
    (7, "Wait ____ I return.", "till"),
    (8, "Do not go ____ I come.", "till"),
    (10, "Take care ____ you fall.", "lest"),
    (13, "Open rebuke is better ____ secret love.", "than"),
    (14, "____ you eat too much you will be ill.", "If"),
    (15, "I shall not go ____ I am invited.", "unless"),
    (16, "He has succeeded better ____ he hoped.", "than"),
    (17, "I do it ____ I choose to.", "as"),
    (18, "____ duty calls us we must obey.", "If"),
    (19, "Live well ____ you may die well.", "so that"),
    (21, "The purse has been lost ____ stolen.", "or"),
    (22, "Rustum is slow ____ sure.", "but"),
    (24, "____ he was industrious, I encouraged him.", "As"),
]

# Exercise in Grammar 97: (item, sentence with blank, correct conjunction from key)
EX97 = [
    (1, "Three ____ three make six.", "and"),
    (2, "Is his name Sen ____ Gupta?", "or"),
    (3, "He will not come ____ it rains.", "if"),
    (4, "____ you run, you will not overtake him.", "Unless"),
    (5, "He is very rich ____ he is not happy.", "yet"),
    (6, "____ I return, stay where you are.", "Until"),
    (7, "He was punished, ____ he was guilty.", "for"),
    (9, "There is no doubt ____ the earth is round.", "that"),
    (10, "I wonder ____ he will come.", "when"),
    (11, "He is witty ____ vulgar.", "though"),
    (12, "Will you kindly wait ____ I return?", "till"),
    (14, "He lost his balance ____ fell off the bicycle.", "and"),
    (15, "He tried hard ____ did not succeed.", "but"),
    (16, "Is this my book ____ yours?", "or"),
    (17, "Water ____ oil will not mix.", "and"),
    (19, "The vase will break ____ you drop it.", "if"),
    (22, "Man proposes ____ God disposes.", "but"),
    (23, "Time ____ tide do not wait for anybody.", "and"),
    (24, "Virtue ennobles, ____ vice degrades.", "but"),
    (25, "This ____ that must suffice.", "or"),
    (26, "The train was derailed ____ no one was hurt.", "but"),
    (29, "You will not get the prize ____ you deserve it.", "unless"),
    (31, "Hari will do all right, ____ he perseveres.", "if"),
    (32, "Catch me ____ you can.", "if"),
    (33, "He told me ____ you had arrived an hour ago.", "that"),
    (34, "You will never succeed ____ you try.", "unless"),
    (35, "____ I were you, I'd keep quiet.", "If"),
    (36, "Wait ____ I come.", "till"),
    (37, "Be just ____ fear not.", "and"),
    (38, "Tell me ____ you understand.", "whether"),
    (41, "It is a long time ____ we last saw him.", "since"),
    (42, "Please write ____ I dictate.", "as"),
    (43, "It is hoped ____ all will go well.", "that"),
    (45, "He is taller ____ I (am).", "than"),
    (46, "____ I cannot get away, I will go next week.", "Since"),
    (47, "____ you wish it, it shall be done.", "If"),
    (48, "Why is our food so sweet? ____ we earn before we eat.", "Because"),
    (49, "Take heed ____ you fall.", "lest"),
    (50, "He gazed so long ____ both his eyes were dazzled.", "that"),
    (51, "____ there is life there is hope.", "While"),
    (53, "They say ____ he is better.", "that"),
    (54, "I have been in such a pickle ____ I saw you last.", "since"),
    (55, "His plans, ____ vast, were never visionary.", "though"),
    (56, "Some people live ____ they may eat.", "so that"),
    (58, "He will starve ____ he will steal.", "before"),
    (59, "There were more people ____ we had expected.", "than"),
    (60, "____ there is something to be done, the world knows how to get it done.", "If"),
    (63, "No one knows ____ he went.", "where"),
    (65, "Do ____ you are bidden.", "as"),
    (68, "We all know ____ sin and sorrow go together.", "that"),
    (70, "Grievances cannot be redressed ____ they are known.", "unless"),
    (71, "We shall fail ____ we are industrious.", "unless"),
    (73, "I am well, ____ I do not feel very strong.", "but"),
    (74, "____ he is there, I shall see him.", "If"),
    (75, "How can he buy it ____ he has no money?", "if"),
    (77, "The building has been razed ____ I visited the city.", "since"),
    (78, "Love not sleep, ____ thou come to poverty.", "lest"),
    (79, "He bled so profusely ____ he died.", "that"),
    (80, "I know you better ____ he (does).", "than"),
]

# Generated questions for Chapter 40.
GEN40 = [
    ("Which conjunction joins two equal clauses? 'He tried, ____ he failed.'", "but", ["because", "if", "when"],
     "'But' joins two equal, contrasting clauses.",
     ["Correct: 'but' joins two equal clauses.", "Wrong: 'because' joins a reason to a result.", "Wrong: 'if' introduces a condition.", "Wrong: 'when' introduces a time clause."]),
    ("'I will wait ____ you come.' The best conjunction is:", "until", ["because", "though", "since"],
     "'Until' shows the time up to which the waiting continues.",
     ["Correct: 'until' shows the time limit.", "Wrong: 'because' gives a reason.", "Wrong: 'though' shows contrast.", "Wrong: 'since' shows a starting point."]),
    ("'She was tired, ____ she kept working.' The best conjunction is:", "yet", ["because", "if", "unless"],
     "'Yet' joins a contrasting result to the first clause.",
     ["Correct: 'yet' shows contrast.", "Wrong: 'because' gives a reason.", "Wrong: 'if' introduces a condition.", "Wrong: 'unless' means 'if not'."]),
    ("'You must hurry ____ you will miss the bus.' The best conjunction is:", "or", ["and", "because", "though"],
     "'Or' gives an alternative, meaning 'otherwise'.",
     ["Correct: 'or' gives an alternative result.", "Wrong: 'and' adds, not warns.", "Wrong: 'because' gives a reason.", "Wrong: 'though' shows contrast."]),
    ("'He is poor ____ he is honest.' The best conjunction is:", "but", ["or", "since", "if"],
     "'But' shows contrast between poverty and honesty.",
     ["Correct: 'but' shows contrast.", "Wrong: 'or' gives an alternative.", "Wrong: 'since' gives a reason.", "Wrong: 'if' introduces a condition."]),
    ("'Both Ravi ____ Sita passed the exam.' The best pair is:", "and", ["or", "but", "yet"],
     "'Both ... and' joins two items together.",
     ["Correct: 'both ... and' joins two items.", "Wrong: 'or' gives a choice.", "Wrong: 'but' shows contrast.", "Wrong: 'yet' shows contrast."]),
    ("'Either tea ____ coffee will do.' The best pair is:", "or", ["and", "nor", "but"],
     "'Either ... or' gives a choice between two.",
     ["Correct: 'either ... or' gives a choice.", "Wrong: 'and' adds two things.", "Wrong: 'nor' is used after 'neither'.", "Wrong: 'but' shows contrast."]),
    ("'He was not only clever ____ also kind.' The best pair is:", "but", ["or", "nor", "either"],
     "'Not only ... but also' joins two qualities.",
     ["Correct: 'not only ... but also' is the pair.", "Wrong: 'or' gives a choice.", "Wrong: 'nor' is used with 'neither'.", "Wrong: 'either' is used with 'or'."]),
    ("'Lest' in 'Work hard lest you fail.' means:", "so that ... not", ["because", "even if", "until"],
     "'Lest' introduces the thing to be avoided, meaning 'so that ... not'.",
     ["Correct: 'lest' means 'so that ... not'.", "Wrong: 'because' gives a reason, not a warning.", "Wrong: 'even if' is a concession.", "Wrong: 'until' gives a time limit."]),
    ("'I did not go out ____ it was raining.' The best conjunction is:", "because", ["though", "or", "until"],
     "'Because' gives the reason for not going out.",
     ["Correct: 'because' gives the reason.", "Wrong: 'though' shows contrast.", "Wrong: 'or' gives an alternative.", "Wrong: 'until' gives a time limit."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def _distractors(correct, count=3):
    out = []
    for c in POOL:
        if c.lower() != correct.lower() and c not in out:
            out.append(c)
        if len(out) == count:
            break
    return out


def _fill_questions(rows, exercise):
    out = []
    for n, (item, sentence, correct) in enumerate(rows):
        dis = _distractors(correct)
        options = [correct] + dis
        pos = n % 4
        reasons = [f"Correct: '{correct}' fits the meaning of the sentence."] + \
                  [f"Wrong: '{d}' does not fit the meaning of this sentence." for d in dis]
        out.append({"chapter": 40, "source": "Book", "exercise": f"Exercise in Grammar {exercise}, item {item}",
                    "stem": f"Fill in the blank with the right conjunction: {sentence}",
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"The right conjunction is '{correct}'.", "reasons": _rotate(reasons, pos)})
    return out


def ex96_questions():
    return _fill_questions(EX96, 96)


def ex97_questions():
    return _fill_questions(EX97, 97)


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN40):
        pos = n % 4
        out.append({"chapter": 40, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Grammar 98: join each pair with a suitable conjunction (key page 37, keyimg p-040).
# Only items with a single key answer are used; items 5, 9, 13 and 15 list alternatives and are skipped.
EX98 = [
    (1, "My brother is well. My sister is ill.", "but"),
    (2, "He sells mangoes. He sells oranges.", "and"),
    (3, "He did not succeed. He worked hard.", "though"),
    (4, "Rama played well. Hari played well.", "and"),
    (6, "You may go. I will stay.", "but"),
    (7, "Rama reads for pleasure. Hari reads for profit.", "but"),
    (8, "We decided to set out. It was late.", "though"),
    (10, "He is not a knave. He is not a fool.", "neither ... nor"),
    (11, "We love Bahadur. He is a faithful dog.", "as"),
    (12, "Rustum made twelve runs. He was caught at the wicket.", "before"),
    (14, "The sheep are grazing. The oxen are grazing.", "and"),
    (16, "This mango is large. This mango is sweet.", "and"),
    (17, "My brother was not there. My sister was not there.", "neither ... nor"),
]


def ex98_questions():
    out = []
    pool = POOL + ["neither ... nor"]
    for n, (item, pair, correct) in enumerate(EX98):
        dis = []
        for c in pool:
            if c != correct and c not in dis:
                dis.append(c)
            if len(dis) == 3:
                break
        pos = n % 4
        options = [correct] + dis
        reasons = [f"Correct: '{correct}' joins the two sentences correctly."] + \
                  [f"Wrong: '{d}' does not join these two sentences correctly." for d in dis]
        out.append({"chapter": 40, "source": "Book", "exercise": f"Exercise in Grammar 98, item {item}",
                    "stem": f"Join these two sentences with a suitable conjunction: {pair}",
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"The joining conjunction is '{correct}'.", "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Grammar 98, items 18-32 (key page 38, keyimg p-041). Items 19, 21, 28, 29 and 30 list
# alternatives on the key and are skipped.
EX98B = [
    (18, "The boy is here. The girl is here.", "and"),
    (20, "You must be quiet. You must leave the room.", "or"),
    (22, "Rama works hard. Hari is idle.", "but"),
    (23, "I lost the prize. I tried my best.", "though"),
    (24, "I like him. He is dangerous.", "though"),
    (25, "I went to the shop. I bought a slate.", "and"),
    (26, "He is slow. He is sure.", "but"),
    (27, "I know. He does not think so.", "that"),
    (31, "I shall sit still. I shall listen to the music.", "and"),
    (32, "Hari did not come. He did not send a letter.", "neither ... nor"),
]


def ex98b_questions():
    out = []
    pool = POOL + ["neither ... nor"]
    for n, (item, pair, correct) in enumerate(EX98B):
        dis = []
        for c in pool:
            if c != correct and c not in dis:
                dis.append(c)
            if len(dis) == 3:
                break
        pos = n % 4
        options = [correct] + dis
        reasons = [f"Correct: '{correct}' joins the two sentences correctly."] + \
                  [f"Wrong: '{d}' does not join these two sentences correctly." for d in dis]
        out.append({"chapter": 40, "source": "Book", "exercise": f"Exercise in Grammar 98, item {item}",
                    "stem": f"Join these two sentences with a suitable conjunction: {pair}",
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"The joining conjunction is '{correct}'.", "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Grammar 94: point out the conjunction and say whether it is Co-ordinating or Subordinating.
# Key from key page 36 (keyimg p-039). Items 1-33, all verified against key page 36.
EX94 = [
    (1, "You will not succeed unless you work harder.", "unless", "Subordinating"),
    (2, "We arrived after you had gone.", "after", "Subordinating"),
    (3, "I waited till the train arrived.", "till", "Subordinating"),
    (4, "Bread and milk is wholesome food.", "and", "Co-ordinating"),
    (5, "You will get the prize if you deserve it.", "if", "Subordinating"),
    (6, "When you are called, you must come in at once.", "When", "Subordinating"),
    (7, "Do not go before I come.", "before", "Subordinating"),
    (8, "I cannot give you any money, for I have none.", "for", "Co-ordinating"),
    (9, "Since you say so, I must believe it.", "Since", "Subordinating"),
    (10, "He fled lest he should be killed.", "lest", "Subordinating"),
    (11, "I shall be vexed if you do that.", "if", "Subordinating"),
    (12, "We got into the port before the storm came on.", "before", "Subordinating"),
    (13, "He was sorry after he had done it.", "after", "Subordinating"),
    (14, "I did not come because you did not call me.", "because", "Subordinating"),
    (15, "He is richer than I am.", "than", "Subordinating"),
    (16, "My grandfather died before I was born.", "before", "Subordinating"),
    (17, "I will stay until you return.", "until", "Subordinating"),
    (18, "Catch me if you can.", "if", "Subordinating"),
    (19, "Tom runs faster than Harry.", "than", "Subordinating"),
    (20, "Is that story true or false ?", "or", "Co-ordinating"),
    (21, "You will be late unless you hurry.", "unless", "Subordinating"),
    (22, "He asked whether he might have a holiday.", "whether", "Subordinating"),
    (23, "Give me to drink, else I shall die of thirst.", "else", "Co-ordinating"),
    (24, "If I feel any doubt, I ask.", "If", "Subordinating"),
    (25, "He deserved to succeed, for he worked hard.", "for", "Co-ordinating"),
    (26, "He will be sure to come if you invite him.", "if", "Subordinating"),
    (27, "We can travel by land or water.", "or", "Co-ordinating"),
    (28, "The earth is larger than the moon.", "than", "Subordinating"),
    (29, "Either you are mistaken, or I am.", "either...or", "Co-ordinating"),
    (30, "I shall go, whether you come or not.", "whether...or", "Co-ordinating"),
    (31, "Unless you tell me the truth, I shall punish you.", "Unless", "Subordinating"),
    (32, "I hear that your brother is in London.", "that", "Subordinating"),
    (33, "Blessed are the merciful, for they shall obtain mercy.", "for", "Co-ordinating"),
]


def ex94_questions():
    out = []
    for n, (item, sentence, word, kind) in enumerate(EX94):
        other = "Co-ordinating" if kind == "Subordinating" else "Subordinating"
        pos = n % 4
        options = [kind, other, "Preposition", "Adverb"]
        reasons = [f"Correct: '{word}' is a {kind.lower()} conjunction.",
                   f"Wrong: '{word}' is not a {other.lower()} conjunction here.",
                   f"Wrong: '{word}' is a conjunction here, not a preposition.",
                   f"Wrong: '{word}' is a conjunction here, not an adverb."]
        out.append({"chapter": 40, "source": "Book", "exercise": f"Exercise in Grammar 94, item {item}",
                    "stem": f'In "{sentence}", what kind of conjunction is "{word}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is a {kind.lower()} conjunction.", "reasons": _rotate(reasons, pos)})
    return out
