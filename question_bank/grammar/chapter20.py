"""Chapter 20 (Transitive and Intransitive Verbs): Exercise in Grammar 36 plus generated questions.

Answers: key page 13 (Exercise 36, keyimg p-016). Each verb gets a transitive/intransitive question;
transitive verbs get an object question.
"""

LETTERS = "ABCD"
KINDS = ["Transitive", "Intransitive", "Auxiliary verb", "Modal verb"]

# (item, sentence, verb, kind, object or None) from key page 13.
EX36 = [
    (1, "The sun shines brightly.", "shines", "Intransitive", None),
    (2, "The boy cut his hand with a knife.", "cut", "Transitive", "his hand"),
    (3, "The clock stopped this morning.", "stopped", "Intransitive", None),
    (4, "The policeman blew his whistle.", "blew", "Transitive", "his whistle"),
    (5, "The sun rises in the east.", "rises", "Intransitive", None),
    (6, "An old beggar stood by the gate.", "stood", "Intransitive", None),
    (7, "The clock ticks all day long.", "ticks", "Intransitive", None),
    (8, "I looked down from my window.", "looked", "Intransitive", None),
    (9, "Put away your books.", "put", "Transitive", "your books"),
    (10, "The moon rose early.", "rose", "Intransitive", None),
    (11, "The cat sleeps on the rug.", "sleeps", "Intransitive", None),
    (12, "Cocks crow in the morning.", "crow", "Intransitive", None),
    (13, "Your book lies on the table.", "lies", "Intransitive", None),
    (14, "The fire burns dimly.", "burns", "Intransitive", None),
    (15, "Time changes all things.", "changes", "Transitive", "all things"),
    (16, "We eat three times a day.", "eat", "Intransitive", None),
    (17, "Tell the truth.", "Tell", "Transitive", "the truth"),
    (18, "The birds sing in the green trees.", "sing", "Intransitive", None),
    (19, "The little bird hopped about and sang.", "hopped", "Intransitive", None),
    (19, "The little bird hopped about and sang.", "sang", "Intransitive", None),
    (20, "My new watch does not keep good time.", "does (not) keep", "Transitive", "good time"),
    (21, "The beggar sat down by the side of the road.", "sat", "Intransitive", None),
    (22, "I could not spare the time.", "could (not) spare", "Transitive", "the time"),
    (23, "He took shelter under a tree.", "took", "Transitive", "shelter"),
    (24, "The boy easily lifted the heavy weight.", "lifted", "Transitive", "the heavy weight"),
    (25, "Balu wrote a letter to his uncle.", "wrote", "Transitive", "a letter"),
    (26, "A tiny bird lived under the caves.", "lived", "Intransitive", None),
    (27, "I know a funny little man.", "know", "Transitive", "a funny little man"),
    (28, "Birds fly in the air.", "fly", "Intransitive", None),
    (29, "A light rain fell last night.", "fell", "Intransitive", None),
    (30, "I shall bring my camera with me.", "shall bring", "Transitive", "my camera"),
    (31, "You speak too loudly.", "speak", "Intransitive", None),
    (32, "The dog ran after me.", "ran", "Intransitive", None),
]
OBJECTS = [o for _, _, _, _, o in EX36 if o]

GEN = [
    ("Which sentence has an intransitive verb?", "The bird sings.",
     ["She opened the door.", "He kicked the ball.", "We ate the cake."],
     "'Sings' has no object, so it is intransitive.",
     ["Correct: 'sings' has no object.", "Wrong: 'opened' takes the object 'the door'.", "Wrong: 'kicked' takes the object 'the ball'.", "Wrong: 'ate' takes the object 'the cake'."]),
    ("In 'He bought a pen.', the object is:", "a pen", ["He", "bought", "a"],
     "'A pen' receives the action of buying.",
     ["Correct: 'a pen' receives the action of buying.", "Wrong: 'He' is the subject.", "Wrong: 'bought' is the verb.", "Wrong: 'a' is only an article inside the object."]),
    ("The verb 'shines' in 'The sun shines.' is:", "intransitive", ["transitive", "auxiliary", "modal"],
     "No object follows 'shines'.",
     ["Correct: no object follows it.", "Wrong: it has no object, so it is not transitive.", "Wrong: it is not a helping verb.", "Wrong: it is not a modal verb."]),
    ("A transitive verb is one that:", "takes an object", ["takes no object", "always has a helping verb", "has no subject"],
     "Transitive verbs pass their action on to an object.",
     ["Correct: a transitive verb takes an object.", "Wrong: that describes an intransitive verb.", "Wrong: helping verbs are not what makes a verb transitive.", "Wrong: every sentence has a subject."]),
    ("In 'The teacher explained the lesson.', the verb 'explained' is:", "transitive", ["intransitive", "auxiliary", "modal"],
     "'Explained' takes the object 'the lesson'.",
     ["Correct: it takes the object 'the lesson'.", "Wrong: it has an object, so it is not intransitive.", "Wrong: it is not a helping verb.", "Wrong: it is not a modal verb."]),
    ("The verb 'stood' in 'He stood still.' is:", "intransitive", ["transitive", "auxiliary", "modal"],
     "No object follows 'stood'; 'still' describes the manner.",
     ["Correct: no object follows it.", "Wrong: it has no object, so it is not transitive.", "Wrong: it is not a helping verb.", "Wrong: it is not a modal verb."]),
    ("In 'Put away your books.', the object is:", "your books", ["put", "away", "Put away"],
     "'Your books' receives the action of 'put'.",
     ["Correct: 'your books' receives the action of 'put'.", "Wrong: 'put' is the verb.", "Wrong: 'away' is an adverb.", "Wrong: 'Put away' is the verb phrase, not the object."]),
    ("The verb 'rose' in 'The moon rose early.' is:", "intransitive", ["transitive", "auxiliary", "modal"],
     "No object follows 'rose'.",
     ["Correct: no object follows it.", "Wrong: it has no object, so it is not transitive.", "Wrong: it is not a helping verb.", "Wrong: it is not a modal verb."]),
    ("Which sentence has a transitive verb?", "She wrote a letter.", ["The sun shone.", "The baby slept.", "He arrived early."],
     "'Wrote' takes the object 'a letter'.",
     ["Correct: 'wrote' takes the object 'a letter'.", "Wrong: 'shone' has no object.", "Wrong: 'slept' has no object.", "Wrong: 'arrived' has no object."]),
    ("'Lies' in 'Your book lies on the table.' is:", "intransitive", ["transitive", "auxiliary", "modal"],
     "It is followed by a place, not an object.",
     ["Correct: it is followed by a place, not an object.", "Wrong: it has no object, so it is not transitive.", "Wrong: it is not a helping verb.", "Wrong: it is not a modal verb."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex36_questions():
    out = []
    n = 0
    for item, sentence, verb, kind, obj in EX36:
        # Transitive or intransitive?
        pos = n % 4
        wrong = [k for k in KINDS if k != kind]
        reasons = [f"Correct: '{verb}' is {kind.lower()}."] + \
                  [f"Wrong: '{verb}' is not {w.lower()} here." for w in wrong][:3]
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 36, item {item}",
                    "stem": f'In "{sentence}", is "{verb}" transitive or intransitive?',
                    "options": _rotate([kind] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": f"'{verb}' is {kind.lower()}.", "reasons": _rotate(reasons, pos)})
        n += 1
        # Object
        if obj:
            pos = n % 4
            others = [o for o in OBJECTS if o != obj][:3]
            reasons = [f"Correct: '{obj}' receives the action of '{verb}'."] + \
                      [f"Wrong: '{o}' is not the object of '{verb}' here." for o in others]
            out.append({"source": "Book", "exercise": f"Exercise in Grammar 36, item {item}",
                        "stem": f'In "{sentence}", what is the object of "{verb}"?',
                        "options": _rotate([obj] + others, pos), "correct": LETTERS[pos],
                        "explanation": f"The object of '{verb}' is '{obj}'.", "reasons": _rotate(reasons, pos)})
            n += 1
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 20, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
