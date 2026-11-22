"""Chapters 17 to 19 (Demonstrative, Indefinite and Distributive pronouns; Relative pronouns; Interrogative pronouns).

Exercise in Grammar 29 (book chapter 18) is answered from key page 10: relative pronoun, case and antecedent.
Chapters 17 and 19 have no grammar exercise and are generated only.
"""

LETTERS = "ABCD"
CASES = ["Nominative", "Accusative", "Possessive", "Vocative"]

# (item, sentence, relative pronoun, case, antecedent) from the key.
EX29 = [
    (1, "The pen that you gave me is a very good one.", "that", "Accusative", "pen"),
    (2, "The answer which you gave is not right.", "which", "Accusative", "answer"),
    (3, "I know the woman whose child was hurt.", "whose", "Possessive", "woman"),
    (4, "Bring me the letters which the postman left.", "which", "Accusative", "letters"),
    (5, "This is the house that Jack built.", "that", "Accusative", "house"),
    (6, "Hari saw the man who had been hurt.", "who", "Nominative", "man"),
    (7, "We met the sailors whose ship was wrecked.", "whose", "Possessive", "sailors"),
    (8, "Here are the books which I found.", "which", "Accusative", "books"),
    (9, "The cat killed the rat that ate the corn.", "that", "Nominative", "rat"),
    (10, "Bring me the books which lie on the table.", "which", "Nominative", "books"),
    (11, "Here is the book that you lent me.", "that", "Accusative", "book"),
    (12, "I hate children who are cruel.", "who", "Nominative", "children"),
    (13, "Show me the knife that you have bought.", "that", "Accusative", "knife"),
    (14, "He has not brought the knife that I asked for.", "that", "Accusative", "knife"),
    (15, "Dogs soon know the persons by whom they are kindly treated.", "whom", "Accusative", "persons"),
    (16, "This is the juggler whom we saw yesterday.", "whom", "Accusative", "juggler"),
    (17, "They that seek wisdom will be wise.", "that", "Nominative", "they"),
]
ANTECEDENTS = ["pen", "answer", "woman", "letters", "house", "man", "sailors", "books", "rat", "book", "children", "knife", "persons", "juggler", "they"]

GEN17 = [
    ("Which pronoun points to a thing near the speaker?", "this", ["who", "whom", "which"],
     "'This' points to something near the speaker.", ["Wrong: 'who' asks about or refers to people.", "Wrong: 'whom' is an objective pronoun for people.", "Wrong: 'which' asks about or refers to choice."]),
    ("The demonstrative pronoun for several things far away is:", "those", ["these", "them", "that"],
     "'Those' points to several things at a distance.", ["Wrong: 'these' points to things near the speaker.", "Wrong: 'them' is a personal pronoun.", "Wrong: 'that' is singular here."]),
    ("'Someone' is which kind of pronoun?", "indefinite pronoun", ["personal pronoun", "relative pronoun", "demonstrative pronoun"],
     "'Someone' refers to an unspecified person.", ["Wrong: 'someone' is not used as a personal pronoun here.", "Wrong: 'someone' does not link a clause.", "Wrong: 'someone' does not point out a thing."]),
    ("In 'Each of them won a prize.', 'each' is a:", "distributive pronoun", ["personal pronoun", "relative pronoun", "possessive pronoun"],
     "'Each' refers to every one of a group separately.", ["Wrong: 'each' is not a personal pronoun.", "Wrong: 'each' does not link a clause.", "Wrong: 'each' is not possessive."]),
    ("'Everybody' is which kind of pronoun?", "indefinite pronoun", ["demonstrative pronoun", "relative pronoun", "interrogative pronoun"],
     "'Everybody' refers to people without naming them.", ["Wrong: it does not point out a thing.", "Wrong: it does not link a clause.", "Wrong: it does not ask a question."]),
    ("'Neither' in 'Neither of them came.' is a:", "distributive pronoun", ["relative pronoun", "personal pronoun", "possessive pronoun"],
     "'Neither' is a distributive pronoun, like 'each' and 'either'.", ["Wrong: it does not link a clause.", "Wrong: it is not a personal pronoun.", "Wrong: it is not possessive."]),
    ("'These' in 'These are my books.' is a:", "demonstrative pronoun", ["relative pronoun", "possessive pronoun", "indefinite pronoun"],
     "'These' points out things near the speaker.", ["Wrong: it does not link a clause.", "Wrong: it does not show ownership.", "Wrong: it points out specific things."]),
    ("'Many' in 'Many were absent.' is an:", "indefinite pronoun", ["demonstrative pronoun", "distributive pronoun", "relative pronoun"],
     "'Many' refers to an unspecified number of people.", ["Wrong: it does not point out a thing.", "Wrong: it does not refer to each one separately.", "Wrong: it does not link a clause."]),
    ("'Such' in 'Such was his fate.' is a:", "demonstrative pronoun", ["interrogative pronoun", "relative pronoun", "possessive pronoun"],
     "'Such' points out a kind of thing.", ["Wrong: it is not asking a question.", "Wrong: it does not link a clause.", "Wrong: it does not show ownership."]),
    ("'Anybody' in 'Anybody can do it.' is an:", "indefinite pronoun", ["distributive pronoun", "relative pronoun", "personal pronoun"],
     "'Anybody' refers to any person, unspecified.", ["Wrong: it does not refer to each one of a group.", "Wrong: it does not link a clause.", "Wrong: it is not a personal pronoun here."]),
]

GEN18 = [
    ("Which word is a relative pronoun?", "who", ["he", "him", "his"],
     "'Who' links a clause to the noun before it: 'the man who came'.", ["Wrong: 'he' is a personal pronoun.", "Wrong: 'him' is a personal pronoun.", "Wrong: 'his' is a possessive."]),
    ("The relative pronoun 'whom' is used in which case?", "objective", ["nominative", "possessive", "vocative"],
     "'Whom' is the object of the clause: 'the girl whom I saw'.", ["Wrong: the nominative is for subjects.", "Wrong: the possessive shows ownership.", "Wrong: the vocative is for addressing someone."]),
    ("In 'the book which I read', the antecedent of 'which' is:", "book", ["I", "read", "which"],
     "The antecedent is the noun the relative clause describes: 'book'.", ["Wrong: 'I' is the subject of the clause.", "Wrong: 'read' is a verb.", "Wrong: 'which' is the relative pronoun itself."]),
    ("Which relative pronoun is used for things?", "which", ["who", "whom", "whose"],
     "'Which' is used for things and animals.", ["Wrong: 'who' is used for people.", "Wrong: 'whom' is used for people.", "Wrong: 'whose' shows possession, for people or things."]),
    ("'That' can be used as a relative pronoun for:", "persons and things", ["only animals", "only places", "only time"],
     "'That' can refer to people, things and animals.", ["Wrong: it is not limited to animals.", "Wrong: it is not limited to places.", "Wrong: it is not limited to time."]),
    ("The relative pronoun 'whose' shows:", "possession", ["the object", "the subject", "time"],
     "'Whose' shows that something belongs to the antecedent.", ["Wrong: the object is shown by 'whom' or 'which'.", "Wrong: the subject is shown by 'who'.", "Wrong: 'whose' does not show time."]),
    ("In 'the man who came', 'who' is in which case?", "nominative", ["objective", "possessive", "vocative"],
     "'Who' is the subject of 'came', so it is nominative.", ["Wrong: it is not the object.", "Wrong: it does not show ownership.", "Wrong: it is not being addressed."]),
    ("In 'the girl whom I saw', 'whom' is in which case?", "objective", ["nominative", "possessive", "vocative"],
     "'Whom' is the object of 'saw'.", ["Wrong: it is not the subject of the clause.", "Wrong: it does not show ownership.", "Wrong: it is not being addressed."]),
    ("A relative pronoun links:", "a clause to the noun it describes", ["two nouns only", "a verb to an adverb", "a question to a sentence"],
     "A relative clause describes the noun before it, and the relative pronoun joins them.", ["Wrong: it links a clause, not just two nouns.", "Wrong: it does not link verbs and adverbs.", "Wrong: it does not link questions."]),
    ("In 'This is the house that Jack built.', 'that' is a:", "relative pronoun", ["interrogative pronoun", "demonstrative pronoun", "indefinite pronoun"],
     "'That' links the clause 'Jack built' to 'house'.", ["Wrong: it does not ask a question.", "Wrong: it does not point out a thing here.", "Wrong: it does not refer to an unspecified thing."]),
]

GEN19 = [
    ("Interrogative pronouns are used to:", "ask questions", ["join clauses", "show possession", "express feeling"],
     "'Who' and 'what' ask questions.", ["Wrong: joining clauses is a relative pronoun's job.", "Wrong: showing possession is a possessive's job.", "Wrong: expressing feeling is an interjection's job."]),
    ("In 'Who broke the window?', 'who' is:", "an interrogative pronoun", ["a relative pronoun", "an indefinite pronoun", "a personal pronoun"],
     "'Who' asks a question and is the subject of 'broke'.", ["Wrong: it does not link a clause.", "Wrong: it does not refer to an unspecified person.", "Wrong: it is used to ask, not as a personal pronoun."]),
    ("In 'Whom did you see?', 'whom' is:", "an interrogative pronoun, in the objective case", ["a relative pronoun", "a personal pronoun", "a possessive pronoun"],
     "'Whom' asks a question and is the object of 'see'.", ["Wrong: it does not link a clause here.", "Wrong: it is used to ask a question.", "Wrong: it does not show ownership."]),
    ("In 'Whose book is this?', 'whose' shows:", "possession", ["time", "place", "quantity"],
     "'Whose' asks who owns the book.", ["Wrong: it asks about ownership, not time.", "Wrong: it asks about ownership, not place.", "Wrong: it asks about ownership, not quantity."]),
    ("In 'Which of these is yours?', 'which' is an:", "interrogative pronoun", ["relative pronoun", "demonstrative pronoun", "indefinite pronoun"],
     "'Which' asks for a choice among these.", ["Wrong: it does not link a clause.", "Wrong: it does not point out a thing.", "Wrong: it is not an unspecified pronoun here."]),
    ("In 'What did he say?', 'what' is an:", "interrogative pronoun", ["relative pronoun", "indefinite pronoun", "personal pronoun"],
     "'What' asks about a thing.", ["Wrong: it does not link a clause here.", "Wrong: it asks a question.", "Wrong: it is not a personal pronoun."]),
    ("The interrogative pronoun for a choice of things is:", "which", ["who", "whom", "whose"],
     "'Which' asks for a choice of things.", ["Wrong: 'who' asks about people.", "Wrong: 'whom' asks about people.", "Wrong: 'whose' asks about ownership."]),
    ("'Who is at the door?' - 'who' is in which case?", "nominative", ["objective", "possessive", "vocative"],
     "'Who' is the subject of 'is', so it is nominative.", ["Wrong: it is not the object.", "Wrong: it does not show ownership.", "Wrong: it is not being addressed."]),
    ("Interrogative pronouns can also introduce:", "indirect questions", ["direct statements", "commands only", "exclamations only"],
     "For example, 'I asked who had come.'", ["Wrong: direct statements do not begin this way.", "Wrong: commands do not begin this way.", "Wrong: exclamations do not begin this way."]),
    ("Which question word asks about ownership?", "whose", ["who", "what", "which"],
     "'Whose' asks who something belongs to.", ["Wrong: 'who' asks about the person.", "Wrong: 'what' asks about a thing.", "Wrong: 'which' asks about choice."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex29_questions():
    out = []
    n = 0
    for item, sentence, rel, case, ant in EX29:
        # Case question
        pos = n % 4
        wrong = [c for c in CASES if c != case]
        reasons = [f"Correct: '{rel}' is in the {case.lower()} case here."] + \
                  [f"Wrong: '{rel}' is not {w.lower()} here." for w in wrong]
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 29, item {item}",
                    "stem": f'In "{sentence}", what is the case of the relative pronoun "{rel}"?',
                    "options": _rotate([case] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": f"'{rel}' is in the {case.lower()} case.", "reasons": _rotate(reasons, pos)})
        n += 1
        # Antecedent question
        pos = n % 4
        others = [a for a in ANTECEDENTS if a != ant][n % 5: n % 5 + 3]
        reasons = [f"Correct: '{rel}' refers back to '{ant}'."] + \
                  [f"Wrong: '{rel}' does not refer back to '{o}' here." for o in others]
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 29, item {item}",
                    "stem": f'In "{sentence}", what is the antecedent of "{rel}"?',
                    "options": _rotate([ant] + others, pos), "correct": LETTERS[pos],
                    "explanation": f"The antecedent of '{rel}' is '{ant}'.", "reasons": _rotate(reasons, pos)})
        n += 1
    return out


def generated_questions(chapter):
    data = {17: GEN17, 18: GEN18, 19: GEN19}[chapter]
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(data):
        pos = n % 4
        out.append({"chapter": chapter, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate([f"Correct: {expl}"] + reasons, pos)})
    return out
