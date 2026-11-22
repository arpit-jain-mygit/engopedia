"""Chapter 16 (Reflexive and Emphatic Pronouns): Exercise in Grammar 28 plus generated questions.

Answers: key page 9 (items 1-20) and page 10 (items 21-27).
"""

LETTERS = "ABCD"
KINDS = ["Reflexive", "Emphatic", "Personal pronoun", "Relative pronoun"]
KIND_REASON = {
    "Reflexive": "the action goes back to the doer",
    "Emphatic": "it only adds emphasis and can be left out",
    "Personal pronoun": "it stands for a person without showing the action going back",
    "Relative pronoun": "it links a clause to a noun before it",
}

# (item, sentence, pronoun, kind from key)
EX28 = [
    (1, "I will go myself.", "myself", "Emphatic"),
    (2, "Rama has hurt himself.", "himself", "Reflexive"),
    (3, "We often deceive ourselves.", "ourselves", "Reflexive"),
    (4, "I myself heard the remark.", "myself", "Emphatic"),
    (5, "You express yourself very imperfectly.", "yourself", "Reflexive"),
    (6, "I wash myself when I get up.", "myself", "Reflexive"),
    (7, "The boys hid themselves.", "themselves", "Reflexive"),
    (8, "They have got themselves into a mess.", "themselves", "Emphatic"),
    (9, "Boadicea poisoned herself.", "herself", "Reflexive"),
    (10, "They loved themselves so much that they thought of no one else.", "themselves", "Reflexive"),
    (11, "The prisoner hanged himself.", "himself", "Reflexive"),
    (12, "The poor widow poisoned herself.", "herself", "Reflexive"),
    (13, "They enjoyed themselves.", "themselves", "Reflexive"),
    (14, "Don't you deceive yourself?", "yourself", "Reflexive"),
    (15, "I myself heard the remark.", "myself", "Emphatic"),
    (16, "He set himself a hard task.", "himself", "Reflexive"),
    (17, "We exerted ourselves.", "ourselves", "Reflexive"),
    (18, "The dog choked itself.", "itself", "Reflexive"),
    (19, "They gave themselves a lot of trouble.", "themselves", "Reflexive"),
    (20, "We seldom see ourselves as others see us.", "ourselves", "Reflexive"),
    (21, "A house divided against itself cannot stand.", "itself", "Reflexive"),
    (22, "He that wrongs his friend wrongs himself more.", "himself", "Reflexive"),
    (23, "Some people are always talking about themselves.", "themselves", "Reflexive"),
    (24, "Xerxes himself was the last to cross the Hellespont.", "himself", "Emphatic"),
    (25, "He has landed himself in difficulties.", "himself", "Reflexive"),
    (26, "Thou shalt love thy neighbour as thyself.", "thyself", "Reflexive"),
    (27, "Acquit yourselves like men.", "yourselves", "Reflexive"),
]

GEN = [
    ("A reflexive pronoun is used when:", "the action goes back to the doer",
     ["it asks a question", "it joins two clauses", "it shows ownership"],
     "'I wash myself' - the action returns to the subject 'I'.",
     ["Wrong: asking a question is not its job.", "Wrong: joining clauses is a conjunction's job.", "Wrong: showing ownership is a possessive's job."]),
    ("Emphatic pronouns are used to:", "emphasise the noun or pronoun",
     ["show possession", "ask a question", "replace a noun"],
     "'I myself heard it' adds emphasis to 'I'.",
     ["Wrong: possession is shown by possessive forms.", "Wrong: questions use interrogative pronouns.", "Wrong: replacing a noun is a personal pronoun's job."]),
    ("Which is a reflexive pronoun in 'She hurt herself.'?", "herself",
     ["her", "she", "hers"],
     "'Herself' shows the action going back to 'she'.",
     ["Wrong: 'her' is a personal pronoun.", "Wrong: 'she' is the subject.", "Wrong: 'hers' is a possessive pronoun."]),
    ("Which is an emphatic pronoun in 'I myself did it.'?", "myself",
     ["I", "did", "it"],
     "'Myself' adds emphasis to 'I'.",
     ["Wrong: 'I' is the subject, not the emphatic word.", "Wrong: 'did' is a verb.", "Wrong: 'it' is the object."]),
    ("The reflexive pronoun for 'they' is:", "themselves",
     ["them", "theirs", "their"],
     "'Themselves' is the reflexive form for 'they'.",
     ["Wrong: 'them' is objective.", "Wrong: 'theirs' is possessive.", "Wrong: 'their' is possessive."]),
    ("The reflexive pronoun for 'it' is:", "itself",
     ["its", "it", "itselves"],
     "'Itself' is the reflexive form for 'it'.",
     ["Wrong: 'its' is possessive.", "Wrong: 'it' is not reflexive.", "Wrong: 'itselves' is not a word."]),
    ("'Thyself' is the reflexive pronoun for:", "thou",
     ["you", "thee", "they"],
     "'Thyself' goes with the older pronoun 'thou'.",
     ["Wrong: 'you' takes 'yourself'.", "Wrong: 'thee' is objective.", "Wrong: 'they' takes 'themselves'."]),
    ("Reflexive pronouns end in:", "-self or -selves",
     ["-s only", "-ing", "-ed"],
     "'Myself', 'ourselves' and similar forms end in -self or -selves.",
     ["Wrong: they do not end in -s alone.", "Wrong: -ing is a verb form.", "Wrong: -ed is a verb form."]),
    ("Can an emphatic pronoun be left out without changing the basic meaning?", "Yes",
     ["No", "Never", "Only in questions"],
     "Emphatic pronouns only add emphasis, so the sentence still works without them.",
     ["Wrong: the sentence still makes sense without it.", "Wrong: it is not needed for the sentence to work.", "Wrong: this is not limited to questions."]),
    ("In 'He hurt himself.', 'himself' is:", "reflexive",
     ["emphatic", "relative", "interrogative"],
     "The action of hurting goes back to 'he'.",
     ["Wrong: it is needed; it is not only emphasis.", "Wrong: it does not link a clause.", "Wrong: it does not ask a question."]),
]

def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex28_questions():
    out = []
    for n, (item, sentence, pron, kind) in enumerate(EX28):
        pos = n % 4
        wrong = [k for k in KINDS if k != kind]
        reasons = [f"Correct: '{pron}' is {kind.lower()} because {KIND_REASON[kind]}."] + \
                  [f"Wrong: '{pron}' is {kind.lower()}, not {w.lower()}." for w in wrong if w != kind][:3]
        # the wrong list has three kinds; reasons line up with them in order
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 28, item {item}",
                    "stem": f'In "{sentence}", is "{pron}" reflexive, emphatic, personal or relative?',
                    "options": _rotate([kind] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": f"'{pron}' is {kind.lower()}.", "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 16, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate([f"Correct: {expl}"] + reasons, pos)})
    return out
