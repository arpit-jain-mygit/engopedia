"""Chapter 28 (The Infinitive): Exercise in Grammar 49 plus generated questions.

Answers: key page 18 (keyimg p-021). Each infinitive gets two questions: its type (Simple or
Gerundial) and its use in the sentence.
"""

LETTERS = "ABCD"

ROLES = [
    "subject of the verb",
    "object of the verb",
    "objective complement",
    "complement of the verb",
    "object of a preposition",
    "used with a modal verb",
    "in apposition",
    "qualifies a noun",
    "qualifies an adjective",
    "qualifies a verb",
]

# (item, sentence, infinitive word, type, use) from key page 18.
EX49 = [
    (1, "There was nothing for it to fight.", "to fight", "Simple", "object of a preposition"),
    (2, "Let us pray.", "pray", "Simple", "objective complement"),
    (3, "The mango is fit to eat.", "to eat", "Gerundial", "qualifies an adjective"),
    (4, "I heard her sing.", "sing", "Simple", "objective complement"),
    (5, "I have come to see you.", "to see", "Gerundial", "qualifies a verb"),
    (6, "The order to advance was given.", "to advance", "Gerundial", "qualifies a noun"),
    (7, "Men must work and women must weep.", "work", "Simple", "used with a modal verb"),
    (7, "Men must work and women must weep.", "weep", "Simple", "used with a modal verb"),
    (8, "I am sorry to hear this.", "to hear", "Gerundial", "qualifies an adjective"),
    (9, "He is slow to forgive.", "to forgive", "Gerundial", "qualifies an adjective"),
    (10, "A man severe he was and stern to view.", "to view", "Gerundial", "qualifies an adjective"),
    (11, "And fools who came to scoff remained to pray.", "to scoff", "Gerundial", "qualifies a verb"),
    (12, "Thus to relieve the wretched was his pride.", "to relieve", "Simple", "subject of the verb"),
    (13, "Full many a flower is born to blush unseen.", "to blush", "Gerundial", "qualifies a verb"),
    (14, "Music hath charms to soothe the savage beast.", "to soothe", "Gerundial", "qualifies a noun"),
    (15, "Never seek to tell thy love.", "to tell", "Simple", "object of the verb"),
    (16, "To retreat was difficult; to advance was impossible.", "to retreat", "Simple", "subject of the verb"),
    (17, "Everybody wishes to enjoy life.", "to enjoy", "Simple", "object of the verb"),
    (18, "My desire is to see you again.", "to see", "Simple", "complement of the verb"),
    (19, "There was not a moment to be lost.", "to be lost", "Gerundial", "qualifies a noun"),
    (20, "The counsel rose to address the court.", "to address", "Gerundial", "qualifies a verb"),
    (21, "My right there is none to dispute.", "to dispute", "Gerundial", "qualifies a noun"),
    (22, "The ability to laugh is peculiar to mankind.", "to laugh", "Gerundial", "qualifies a noun"),
    (23, "He has the power to concentrate his thoughts.", "to concentrate", "Gerundial", "qualifies a noun"),
    (24, "He was quick to see the point.", "to see", "Gerundial", "qualifies an adjective"),
    (25, "I am not afraid to speak the truth.", "to speak", "Gerundial", "qualifies an adjective"),
    (26, "Better dwell in the midst of alarms than reign in this horrible place.", "dwell", "Simple", "used with a modal verb"),
    (26, "Better dwell in the midst of alarms than reign in this horrible place.", "reign", "Simple", "used with a modal verb"),
    (27, "Can you hope to count the stars?", "hope", "Simple", "used with a modal verb"),
    (27, "Can you hope to count the stars?", "to count", "Simple", "object of the verb"),
    (28, "To toil is the lot of mankind.", "To toil", "Simple", "subject of the verb"),
    (29, "It is delightful to hear the sound of the sea.", "to hear", "Simple", "in apposition"),
    (30, "It is a penal offence to bribe a public servant.", "to bribe", "Simple", "in apposition"),
]

GEN = [
    ("In 'I want to sleep.', the infinitive 'to sleep' is the:", "object of the verb", ["subject of the verb", "in apposition", "qualifies a noun"],
     "'To sleep' is what the subject wants, so it is the object.",
     ["Correct: it is the object of 'want'.", "Wrong: the subject is 'I'.", "Wrong: it is not in apposition.", "Wrong: it qualifies the verb, not a noun."]),
    ("In 'To err is human.', the infinitive 'To err' is the:", "subject of the verb", ["object of the verb", "objective complement", "in apposition"],
     "'To err' is what the sentence is about, so it is the subject.",
     ["Correct: it is the subject of 'is'.", "Wrong: it is not an object.", "Wrong: it is not an objective complement.", "Wrong: it is not in apposition."]),
    ("'She has a plan to start a business.' The infinitive 'to start' qualifies:", "a noun", ["a verb", "an adjective", "a preposition"],
     "'To start' describes the noun 'plan', so it qualifies a noun.",
     ["Correct: it describes the noun 'plan'.", "Wrong: it does not describe the verb.", "Wrong: it does not describe an adjective.", "Wrong: a preposition is not described by an infinitive."]),
    ("'He is happy to help.' The infinitive 'to help' qualifies:", "an adjective", ["a noun", "a verb", "a pronoun"],
     "'To help' explains the adjective 'happy'.",
     ["Correct: it explains the adjective 'happy'.", "Wrong: there is no noun it describes.", "Wrong: it does not describe the verb.", "Wrong: it does not describe a pronoun."]),
    ("In 'Let me go.', the verb 'go' is used:", "without 'to'", ["with 'to'", "as a gerund", "as a participle"],
     "After 'let', the simple infinitive is used without 'to'.",
     ["Correct: after 'let' the infinitive has no 'to'.", "Wrong: 'to go' would not be correct after 'let'.", "Wrong: a gerund ends in '-ing'.", "Wrong: a participle is not an infinitive."]),
    ("In 'He is too weak to walk.', the infinitive 'to walk' qualifies:", "an adjective", ["a noun", "a pronoun", "a preposition"],
     "'To walk' explains how the adjective 'weak' applies.",
     ["Correct: it explains the adjective 'weak'.", "Wrong: there is no noun modified here.", "Wrong: there is no pronoun modified.", "Wrong: a preposition is not described here."]),
    ("'I went out to buy milk.' The infinitive 'to buy' qualifies:", "the verb 'went'", ["a noun", "an adjective", "a pronoun"],
     "'To buy' tells why I went out, so it qualifies the verb.",
     ["Correct: it tells why the action 'went' happened.", "Wrong: there is no noun modified.", "Wrong: there is no adjective modified.", "Wrong: there is no pronoun modified."]),
    ("'You must try to listen.' The infinitive 'to listen' is used with:", "a finite verb", ["a gerund", "a participle", "a preposition"],
     "'To listen' completes the finite verb 'try'.",
     ["Correct: it completes the finite verb 'try'.", "Wrong: a gerund would end in '-ing'.", "Wrong: a participle describes nouns.", "Wrong: it is not a preposition."]),
    ("'It is easy to understand the lesson.' The infinitive 'to understand' qualifies:", "an adjective", ["a noun", "a verb", "a pronoun"],
     "'To understand' explains the adjective 'easy'.",
     ["Correct: it explains the adjective 'easy'.", "Wrong: there is no noun modified.", "Wrong: it does not describe the verb.", "Wrong: there is no pronoun modified."]),
    ("'He was made to wait.' The infinitive 'to wait' is:", "an objective complement or infinitive after 'made'", ["a subject", "a gerund", "a preposition"],
     "After 'made', the infinitive completes the sentence as an infinitive of purpose or complement.",
     ["Correct: it completes the sentence after 'made'.", "Wrong: it is not the subject.", "Wrong: a gerund would end in '-ing'.", "Wrong: it is not a preposition."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex49_questions():
    out = []
    counter = 0
    for n, (item, sentence, word, typ, use) in enumerate(EX49):
        counter += 1
        # Question 1: type (Simple or Gerundial)
        other_type = "Gerundial" if typ == "Simple" else "Simple"
        opts = [typ, other_type, "Gerund", "Participle"]
        reasons = [f"Correct: '{word}' is a {typ.lower()} infinitive.",
                   f"Wrong: '{word}' is not a {other_type.lower()} infinitive.",
                   "Wrong: a gerund ends in '-ing' and is a noun.",
                   "Wrong: a participle is a verb form used as an adjective."]
        pos = n % 4
        out.append({"chapter": 28, "source": "Book", "exercise": f"Exercise in Grammar 49, item {item}",
                    "stem": f'In "{sentence}", is "{word}" a Simple or Gerundial infinitive?',
                    "options": _rotate(opts, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is a {typ.lower()} infinitive.", "reasons": _rotate(reasons, pos)})
        # Question 2: use
        others = [r for r in ROLES if r != use][:3]
        opts = [use] + others
        reasons = [f"Correct: '{word}' is {use}."] + [f"Wrong: '{word}' is not {r} here." for r in others]
        pos = (n + 1) % 4
        out.append({"chapter": 28, "source": "Book", "exercise": f"Exercise in Grammar 49, item {item}",
                    "stem": f'In "{sentence}", how is "{word}" used?',
                    "options": _rotate(opts, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is {use}.", "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 28, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
