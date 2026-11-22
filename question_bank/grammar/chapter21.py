"""Chapter 21 (Verbs of Incomplete Predication): Exercise in Grammar 38 plus generated questions.

Answers: key page 14 (Exercise 38). Each verb gets a transitive/intransitive question; transitive verbs
get an object question; verbs with a complement get a complement question.
"""

LETTERS = "ABCD"
KINDS = ["Transitive", "Intransitive", "Auxiliary verb", "Modal verb"]

# (item, sentence, verb, kind, object or None, complement or None) from key page 14.
EX38 = [
    (1, "The hungry lion roars.", "roars", "Intransitive", None, None),
    (2, "The report proved false.", "proved", "Intransitive", None, "false"),
    (3, "The boy stood on the burning deck.", "stood", "Intransitive", None, None),
    (4, "The child had fallen sick.", "had fallen", "Intransitive", None, "sick"),
    (5, "The ass continued braying.", "continued", "Transitive", "braying", None),
    (6, "The wind is cold.", "is", "Intransitive", None, "cold"),
    (7, "The results are out.", "are", "Intransitive", None, "out"),
    (8, "He tried again and again.", "tried", "Intransitive", None, None),
    (9, "We see with our eyes.", "see", "Intransitive", None, None),
    (10, "The child fell asleep.", "fell", "Intransitive", None, "asleep"),
    (11, "The weather is hot.", "is", "Intransitive", None, "hot"),
    (12, "They are Europeans.", "are", "Intransitive", None, "Europeans"),
    (13, "The rumour seems true.", "seems", "Intransitive", None, "true"),
    (14, "Owls hide in the daytime.", "hide", "Intransitive", None, None),
    (15, "Bad boys hide their faults.", "hide", "Transitive", "their faults", None),
    (16, "The poor woman went mad.", "went", "Intransitive", None, "mad"),
    (17, "We waited patiently at the station.", "waited", "Intransitive", None, None),
    (18, "He told a lie.", "told", "Transitive", "a lie", None),
    (19, "They elected him president.", "elected", "Transitive", "him", "president"),
    (20, "I found her weeping.", "found", "Transitive", "her", "weeping"),
    (21, "He struck the man dead.", "struck", "Transitive", "the man", "dead"),
    (22, "The crow flew down and stole the cheese.", "flew", "Intransitive", None, None),
    (22, "The crow flew down and stole the cheese.", "stole", "Transitive", "the cheese", None),
    (23, "The sky looks threatening.", "looks", "Intransitive", None, "threatening"),
    (24, "They made him general.", "made", "Transitive", "him", "general"),
    (25, "He waited an hour.", "waited", "Intransitive", None, None),
    (26, "New brooms sweep clean.", "sweep", "Intransitive", None, "clean"),
]
OBJECTS = [o for _, _, _, _, o, _ in EX38 if o]
COMPLEMENTS = [c for _, _, _, _, _, c in EX38 if c]

GEN = [
    ("A transitive verb is one that:", "takes an object", ["takes no object", "has no subject", "is always a helping verb"],
     "'Cut' in 'He cut the rope' takes the object 'the rope'.", ["Correct: a transitive verb takes an object.", "Wrong: that describes an intransitive verb.", "Wrong: every verb has a subject in a sentence.", "Wrong: helping verbs are auxiliaries, not a type of transitive verb."]),
    ("An intransitive verb is one that:", "takes no object", ["takes an object", "always needs a complement", "is a helping verb"],
     "'The sun shines' has no object.", ["Wrong: that describes a transitive verb.", "Wrong: intransitive verbs may not need a complement.", "Wrong: helping verbs are auxiliaries."]),
    ("The verb 'sleep' in 'The baby sleeps.' is:", "intransitive", ["transitive", "auxiliary", "modal"],
     "'Sleep' takes no object here.", ["Correct: it has no object.", "Wrong: it has no object, so it is not transitive.", "Wrong: it is not a helping verb.", "Wrong: it is not a modal verb."]),
    ("In 'She bought a book.', the object is:", "a book", ["she", "bought", "a"],
     "'A book' receives the action of buying.", ["Wrong: 'she' is the subject.", "Wrong: 'bought' is the verb.", "Wrong: 'a' is an article, part of the object."]),
    ("A verb of incomplete predication needs:", "a complement", ["an object", "no subject", "an adverb only"],
     "Verbs like 'seem' and 'become' need a complement to complete the meaning.", ["Wrong: it needs a complement, not an object.", "Wrong: every sentence has a subject.", "Wrong: it does not need only an adverb."]),
    ("In 'The wind is cold.', the complement is:", "cold", ["wind", "is", "the"],
     "'Cold' describes the subject and completes the verb 'is'.", ["Wrong: 'wind' is the subject.", "Wrong: 'is' is the verb.", "Wrong: 'the' is an article."]),
    ("'Seems' in 'The rumour seems true.' is:", "intransitive", ["transitive", "auxiliary", "modal"],
     "'Seems' needs the complement 'true' but takes no object.", ["Correct: it is intransitive with a complement.", "Wrong: it takes no object, so it is not transitive.", "Wrong: it is not a helping verb.", "Wrong: it is not a modal."]),
    ("In 'They elected him president.', the object is:", "him", ["president", "elected", "They"],
     "'Him' is the object; 'president' completes it.", ["Correct: 'him' is the object.", "Wrong: 'president' is the complement.", "Wrong: 'elected' is the verb.", "Wrong: 'They' is the subject."]),
    ("The verb 'is' in 'He is a teacher.' is:", "a linking verb", ["an object", "a modal", "an adverb"],
     "'Is' links the subject to the complement 'a teacher'.", ["Correct: it links subject and complement.", "Wrong: it is not an object.", "Wrong: it is not a modal.", "Wrong: it is not an adverb."]),
    ("A transitive verb can be turned into a passive when it:", "has an object", ["has a complement", "has no subject", "is intransitive"],
     "Only verbs with an object can become passive.", ["Correct: an object is needed for the passive.", "Wrong: complements alone do not allow the passive.", "Wrong: every sentence has a subject.", "Wrong: intransitive verbs cannot become passive."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex38_questions():
    out = []
    n = 0
    for item, sentence, verb, kind, obj, comp in EX38:
        # Transitive or intransitive?
        pos = n % 4
        wrong = [k for k in KINDS if k != kind]
        reasons = [f"Correct: '{verb}' is {kind.lower()}."] + \
                  [f"Wrong: '{verb}' is not {w.lower()} here." for w in wrong if w != kind][:3]
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 38, item {item}",
                    "stem": f'In "{sentence}", is "{verb}" transitive or intransitive?',
                    "options": _rotate([kind] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": f"'{verb}' is {kind.lower()}.", "reasons": _rotate(reasons, pos)})
        n += 1
        # Object
        if obj:
            pos = n % 4
            others = [o for o in OBJECTS if o != obj][: 3]
            reasons = [f"Correct: '{obj}' receives the action of '{verb}'."] + \
                      [f"Wrong: '{o}' is not the object of '{verb}' here." for o in others]
            out.append({"source": "Book", "exercise": f"Exercise in Grammar 38, item {item}",
                        "stem": f'In "{sentence}", what is the object of "{verb}"?',
                        "options": _rotate([obj] + others, pos), "correct": LETTERS[pos],
                        "explanation": f"The object of '{verb}' is '{obj}'.", "reasons": _rotate(reasons, pos)})
            n += 1
        # Complement
        if comp:
            pos = n % 4
            others = [c for c in COMPLEMENTS if c != comp][: 3]
            reasons = [f"Correct: '{comp}' completes the meaning of '{verb}'."] + \
                      [f"Wrong: '{c}' is not the complement of '{verb}' here." for c in others]
            out.append({"source": "Book", "exercise": f"Exercise in Grammar 38, item {item}",
                        "stem": f'In "{sentence}", what is the complement of "{verb}"?',
                        "options": _rotate([comp] + others, pos), "correct": LETTERS[pos],
                        "explanation": f"The complement of '{verb}' is '{comp}'.", "reasons": _rotate(reasons, pos)})
            n += 1
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        if len(reasons) == 3:  # the correct reason was left out
            reasons = [f"Correct: {expl}"] + reasons
        pos = n % 4
        out.append({"chapter": 21, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
