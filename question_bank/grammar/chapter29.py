"""Chapter 29 (The Participle): Exercises 51 and 52 plus generated questions.

Answers: key page 19 (keyimg p-022). Each participle gets two questions: its kind (Present, Past or
Perfect) and how it is used in the sentence.
"""

LETTERS = "ABCD"
KINDS = ["Present Participle", "Past Participle", "Perfect Participle", "Gerund"]
ROLES = [
    "qualifies a noun",
    "qualifies a pronoun",
    "governs a noun",
    "governs a pronoun",
    "attached to a noun",
    "attached to a verb",
    "used absolutely (impersonal absolute)",
    "used absolutely with a noun",
]

# (exercise, item, participle word, kind, use) from key page 19.
EX = [
    (51, 1, "speaking", "Present Participle", "used absolutely (impersonal absolute)"),
    (51, 2, "Having gained", "Perfect Participle", "governs a noun"),
    (51, 3, "approaching", "Present Participle", "attached to a noun"),
    (51, 4, "Hearing", "Present Participle", "governs a noun"),
    (51, 5, "considering", "Present Participle", "used absolutely (impersonal absolute)"),
    (51, 6, "beaten", "Past Participle", "qualifies a noun"),
    (51, 7, "Being dissatisfied", "Present Participle", "qualifies a pronoun"),
    (51, 8, "pouring", "Present Participle", "attached to a verb"),
    (51, 9, "Having elected", "Perfect Participle", "governs a pronoun"),
    (51, 10, "being", "Present Participle", "used absolutely with a noun"),
    (52, 1, "laid", "Past Participle", "qualifies a noun"),
    (52, 2, "Being occupied", "Present Participle", "qualifies a pronoun"),
    (52, 3, "coming", "Present Participle", "qualifies a noun"),
    (52, 4, "bereft", "Past Participle", "qualifies a noun"),
    (52, 5, "read", "Past Participle", "qualifies a noun"),
    (52, 6, "learned", "Past Participle", "qualifies a noun"),
    (52, 7, "spoken", "Past Participle", "qualifies a noun"),
    (52, 8, "Seeing", "Present Participle", "governs a noun"),
    (52, 9, "Seizing", "Present Participle", "governs a pronoun"),
    (52, 10, "Encouraged", "Past Participle", "qualifies a pronoun"),
    (52, 11, "Overcome", "Past Participle", "qualifies a pronoun"),
]

GEN = [
    ("'Seen from the hill, the town looked small.' The participle 'Seen' is a:", "Past Participle", ["Present Participle", "Perfect Participle", "Gerund"],
     "'Seen' is the past participle, here describing the town.",
     ["Correct: 'seen' is a past participle.", "Wrong: the present participle ends in '-ing'.", "Wrong: a perfect participle uses 'having'.", "Wrong: a gerund is a noun ending in '-ing'."]),
    ("'Running fast, he caught the bus.' The participle 'Running' is a:", "Present Participle", ["Past Participle", "Perfect Participle", "Gerund"],
     "'Running' is the present participle, showing action in progress.",
     ["Correct: 'running' is a present participle.", "Wrong: the past participle is 'run' in its past form.", "Wrong: a perfect participle uses 'having'.", "Wrong: a gerund is used as a noun."]),
    ("'Having finished the work, she went home.' The participle 'Having finished' is a:", "Perfect Participle", ["Present Participle", "Past Participle", "Gerund"],
     "'Having finished' shows an action completed before the main verb.",
     ["Correct: 'having finished' is a perfect participle.", "Wrong: a present participle does not use 'having'.", "Wrong: a past participle alone is not used here.", "Wrong: a gerund is a noun."]),
    ("In 'The broken window was repaired.', the participle 'broken' qualifies:", "a noun", ["a pronoun", "a verb", "a preposition"],
     "'Broken' describes the noun 'window'.",
     ["Correct: it describes the noun 'window'.", "Wrong: it does not describe a pronoun.", "Wrong: it is not a verb in this sentence.", "Wrong: it does not describe a preposition."]),
    ("'Tired, he went to sleep.' The participle 'Tired' qualifies:", "a pronoun", ["a noun", "a verb", "an adverb"],
     "'Tired' describes 'he'.",
     ["Correct: it describes the pronoun 'he'.", "Wrong: there is no noun described here.", "Wrong: it does not describe the verb.", "Wrong: it does not describe an adverb."]),
    ("'Being hungry, the child ate quickly.' The participle 'Being' is:", "a present participle", ["a past participle", "a gerund", "a finite verb"],
     "'Being hungry' shows the state of the child at the time of eating.",
     ["Correct: it is a present participle.", "Wrong: it is not a past participle.", "Wrong: a gerund is used as a noun.", "Wrong: it is not a finite verb."]),
    ("'He walked home, singing a song.' The participle 'singing' qualifies:", "the pronoun 'he'", ["the noun 'home'", "the verb 'walked'", "the noun 'song'"],
     "'Singing' describes what he was doing while walking home.",
     ["Correct: it describes 'he', the subject.", "Wrong: 'home' is a place, not described by 'singing'.", "Wrong: the verb 'walked' is the main verb.", "Wrong: 'song' is the object of 'singing', not what it qualifies."]),
    ("'Written in haste, the letter had mistakes.' The participle 'Written' is a:", "Past Participle", ["Present Participle", "Perfect Participle", "Gerund"],
     "'Written' is the past participle of 'write'.",
     ["Correct: 'written' is a past participle.", "Wrong: present participle ends in '-ing'.", "Wrong: a perfect participle uses 'having'.", "Wrong: a gerund ends in '-ing' and is a noun."]),
    ("'Having lost his way, he asked for help.' The participle 'Having lost' is a:", "Perfect Participle", ["Past Participle", "Present Participle", "Gerund"],
     "'Having lost' shows the loss happened before he asked.",
     ["Correct: 'having lost' is a perfect participle.", "Wrong: a past participle does not use 'having'.", "Wrong: a present participle ends in '-ing' without 'having'.", "Wrong: a gerund is a noun."]),
    ("'The boy, seeing the snake, ran away.' The participle 'seeing' qualifies:", "the noun 'boy'", ["the noun 'snake'", "the verb 'ran'", "the adverb 'away'"],
     "'Seeing the snake' describes the boy.",
     ["Correct: it describes 'the boy'.", "Wrong: 'snake' is the object of 'seeing'.", "Wrong: 'ran' is the main verb.", "Wrong: 'away' is an adverb, not described by the participle."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex_questions():
    out = []
    for n, (ex, item, word, kind, use) in enumerate(EX):
        # Kind
        others = [k for k in KINDS if k != kind]
        pos = n % 4
        reasons = [f"Correct: '{word}' is a {kind.lower()}."] + \
                  [f"Wrong: '{word}' is not a {k.lower()} here." for k in others[:3]]
        out.append({"chapter": 29, "source": "Book", "exercise": f"Exercise in Grammar {ex}, item {item}",
                    "stem": f'What kind of participle is "{word}"?',
                    "options": _rotate([kind] + others, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is a {kind.lower()}.", "reasons": _rotate(reasons, pos)})
        n2 = n + 1
        # Use
        other_roles = [r for r in ROLES if r != use][:3]
        pos = n2 % 4
        reasons = [f"Correct: '{word}' {use}."] + [f"Wrong: this is not how '{word}' is used here." for r in other_roles]
        out.append({"chapter": 29, "source": "Book", "exercise": f"Exercise in Grammar {ex}, item {item}",
                    "stem": f'How is the participle "{word}" used?',
                    "options": _rotate([use] + other_roles, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' {use}.", "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 29, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Grammar 55: participles and gerunds (key page 20, keyimg p-023).
# (item, sentence, word, kind, use)
EX55 = [
    (1, "He was found fighting desperately for his life.", "fighting", "Participle", "qualifies a noun or pronoun"),
    (2, "He has ruined his sight by reading small print.", "reading", "Gerund", "object of a preposition"),
    (3, "Hearing the noise, he ran to the window.", "Hearing", "Participle", "qualifies a noun or pronoun"),
    (4, "We saw a clown standing on his head.", "standing", "Participle", "qualifies a noun or pronoun"),
    (5, "Asking questions is easier than answering them.", "Asking", "Gerund", "subject of a verb"),
    (5, "Asking questions is easier than answering them.", "answering", "Gerund", "subject of a verb"),
    (6, "Waving their hats and handkerchiefs, the people cheered the king.", "Waving", "Participle", "qualifies a noun or pronoun"),
    (7, "Walking on the grass is forbidden.", "Walking", "Gerund", "subject of a verb"),
    (8, "Jumping over the fence, the thief escaped.", "Jumping", "Participle", "qualifies a noun or pronoun"),
    (9, "The miser spends his time in hoarding money.", "hoarding", "Gerund", "object of a preposition"),
    (10, "Much depends on Rama's returning before noon.", "returning", "Gerund", "object of a preposition"),
    (11, "Amassing wealth often ruins health.", "Amassing", "Gerund", "subject of a verb"),
    (12, "I was surprised at Hari's being absent.", "being", "Gerund", "object of a preposition"),
]
USES55 = ["qualifies a noun or pronoun", "subject of a verb", "object of a preposition", "object of a verb"]


def ex55_questions():
    out = []
    for n, (item, sentence, word, kind, use) in enumerate(EX55):
        other_kind = "Gerund" if kind == "Participle" else "Participle"
        pos = n % 4
        reasons = [f"Correct: '{word}' is a {kind.lower()}.",
                   f"Wrong: '{word}' is not a {other_kind.lower()} here.",
                   "Wrong: a perfect participle uses 'having'.",
                   "Wrong: a past participle is not used here."]
        out.append({"chapter": 29, "source": "Book", "exercise": f"Exercise in Grammar 55, item {item}",
                    "stem": f'In "{sentence}", is "{word}" a participle or a gerund?',
                    "options": _rotate([kind, other_kind, "Perfect Participle", "Past Participle"], pos),
                    "correct": LETTERS[pos], "explanation": f"'{word}' is a {kind.lower()}.",
                    "reasons": _rotate(reasons, pos)})
        pos = (n + 1) % 4
        others = [u for u in USES55 if u != use][:3]
        reasons = [f"Correct: '{word}' is used as {use}."] + [f"Wrong: '{word}' is not used as {u} here." for u in others]
        out.append({"chapter": 29, "source": "Book", "exercise": f"Exercise in Grammar 55, item {item}",
                    "stem": f'In "{sentence}", how is "{word}" used?',
                    "options": _rotate([use] + others, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is used as {use}.", "reasons": _rotate(reasons, pos)})
    return out
