"""Chapter 22 (Active and Passive Voice): Exercise in Grammar 39 plus generated questions.

Answers: key page 14 (Exercise 39, keyimg p-017). The printed key covers items 1-22.
Items 23-25 are not on the key page; their voice is derived from the sentence and marked
"derived" in the explanation.
"""

LETTERS = "ABCD"
KINDS = ["Active", "Passive", "Linking verb", "Helping verb"]

# (item, sentence, verb, voice, derived?) from key page 14.
EX39 = [
    (1, "The cat killed the mouse.", "killed", "Active", False),
    (2, "We compelled the enemy to surrender.", "compelled", "Active", False),
    (3, "The boy was bitten by a dog.", "was bitten", "Passive", False),
    (4, "The thief was caught.", "was caught", "Passive", False),
    (5, "The boy made a kite.", "made", "Active", False),
    (6, "The ship was burned.", "was burned", "Passive", False),
    (7, "The young man made a disturbance at the meeting.", "made", "Active", False),
    (8, "The captive was bound to a tree.", "was bound", "Passive", False),
    (9, "The bird was killed by a cruel boy.", "was killed", "Passive", False),
    (10, "The sudden noise frightened the horse.", "frightened", "Active", False),
    (11, "He is loved by all.", "is loved", "Passive", False),
    (12, "The exhibition was opened by the Governor.", "was opened", "Passive", False),
    (13, "I see a dark cloud.", "see", "Active", False),
    (14, "His command was promptly obeyed.", "was obeyed", "Passive", False),
    (15, "Some of the cargo had been damaged by the sea water.", "had been damaged", "Passive", False),
    (16, "Nothing will be gained by hurry.", "will be gained", "Passive", False),
    (17, "The dog chased the sheep.", "chased", "Active", False),
    (18, "This letter was posted last night.", "was posted", "Passive", False),
    (19, "The field is ploughed.", "is ploughed", "Passive", False),
    (20, "The dog was teased by the boy.", "was teased", "Passive", False),
    (21, "The cat drank all the milk.", "drank", "Active", False),
    (22, "A stone struck me on the head.", "struck", "Active", False),
    (23, "The old gentleman takes snuff.", "takes", "Active", True),
    (24, "The money was lost.", "was lost", "Passive", True),
    (25, "The letter has just been posted.", "has been posted", "Passive", True),
]

GEN = [
    ("In 'The door was closed by Ravi.', the voice is:", "Passive", ["Active", "Linking verb", "Helping verb"],
     "The subject 'the door' receives the action.",
     ["Correct: the subject receives the action.", "Wrong: in the active voice the subject does the action.", "Wrong: it is not a linking verb.", "Wrong: 'was closed' is the main verb, not a helping verb."]),
    ("In 'Ravi closed the door.', the voice is:", "Active", ["Passive", "Linking verb", "Helping verb"],
     "The subject 'Ravi' does the action.",
     ["Correct: the subject does the action.", "Wrong: in the passive voice the subject receives the action.", "Wrong: it is not a linking verb.", "Wrong: 'closed' is the main verb."]),
    ("The passive form of 'The cat chased the rat.' is:", "The rat was chased by the cat.", ["The cat was chased by the rat.", "The rat chased the cat.", "The cat is chasing the rat."],
     "The object 'the rat' becomes the subject, and 'by' brings in the doer.",
     ["Correct: the object 'the rat' becomes the subject.", "Wrong: this swaps the doer and receiver.", "Wrong: this keeps the active voice.", "Wrong: this is still active, with a new verb form."]),
    ("A verb can be made passive only when it has:", "an object", ["a complement", "no subject", "an adverb"],
     "Only a transitive verb with an object can change to the passive.",
     ["Correct: only an object can become the subject of a passive.", "Wrong: complements do not allow the passive.", "Wrong: every sentence has a subject.", "Wrong: an adverb does not change the voice."]),
    ("The passive is formed with:", "a form of 'be' plus the past participle", ["the base verb alone", "a form of 'have' only", "the present participle alone"],
     "Forms like 'was seen' and 'is loved' use 'be' and the past participle.",
     ["Correct: 'be' plus the past participle, as in 'was seen'.", "Wrong: the base verb alone gives the active form.", "Wrong: 'have' alone does not form the passive.", "Wrong: the present participle alone is not passive."]),
    ("In 'The window was broken.', the agent is:", "not stated", ["the window", "was broken", "the glass"],
     "No doer is named after 'by', so the agent is not stated.",
     ["Correct: no doer follows 'by'.", "Wrong: 'the window' is the subject.", "Wrong: 'was broken' is the verb.", "Wrong: 'the glass' is not in the sentence."]),
    ("Which sentence is in the passive voice?", "The letter was written yesterday.", ["She wrote the letter yesterday.", "He writes letters daily.", "They will write to us."],
     "'Was written' shows the letter receiving the action.",
     ["Correct: the subject 'the letter' receives the action.", "Wrong: 'wrote' is active with the doer as subject.", "Wrong: 'writes' is active.", "Wrong: 'will write' is active."]),
    ("Which sentence is in the active voice?", "The farmer grows rice.", ["Rice is grown by the farmer.", "Rice was grown by the farmer.", "Rice has been grown by the farmer."],
     "'The farmer' is the subject and does the growing.",
     ["Correct: the subject 'the farmer' does the action.", "Wrong: this is passive.", "Wrong: this is passive.", "Wrong: this is passive."]),
    ("'Is loved' in 'He is loved by all.' is:", "passive", ["active", "a linking verb", "a helping verb only"],
     "The subject 'he' receives the love.",
     ["Correct: the subject receives the action.", "Wrong: it is not active here.", "Wrong: 'is' is a helping verb, but 'is loved' as a whole is passive.", "Wrong: it is not a plain helping verb alone."]),
    ("'Frightened' in 'The noise frightened the horse.' is:", "active", ["passive", "a helping verb", "a modal verb"],
     "'The noise' does the frightening; the horse receives it.",
     ["Correct: the subject does the action.", "Wrong: the horse receives the action, but the verb is active.", "Wrong: it is the main verb.", "Wrong: it is not a modal verb."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex39_questions():
    out = []
    for n, (item, sentence, verb, voice, derived) in enumerate(EX39):
        pos = n % 4
        other = "Passive" if voice == "Active" else "Active"
        options = [voice, other, "Linking verb", "Helping verb"]
        reasons = [f"Correct: '{verb}' is {voice.lower()} voice.",
                   f"Wrong: '{verb}' is {other.lower()} voice here.",
                   f"Wrong: '{verb}' is not a linking verb.",
                   f"Wrong: '{verb}' is not used as a helping verb here."]
        note = " (derived from the sentence; not on the printed key)" if derived else ""
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 39, item {item}",
                    "stem": f'In "{sentence}", is "{verb}" active or passive?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{verb}' is in the {voice.lower()} voice{note}.",
                    "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 22, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
