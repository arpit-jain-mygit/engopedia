"""Chapter 23 (Mood): Exercise in Grammar 45 plus generated questions.

Answers: key pages 16 and 17 (Exercise 45, keyimg p-019 for items 1-11 and p-020 for items 12-28).
Each verb gets a mood question and a tense question.
"""

LETTERS = "ABCD"
MOODS = ["Indicative", "Subjunctive", "Imperative"]
TENSES = [
    "Simple Present", "Simple Past", "Simple Future", "Present Continuous", "Past Continuous",
    "Present Perfect", "Past Perfect", "Future Perfect", "Present Perfect Continuous",
    "Past Perfect Continuous", "Future Continuous", "Future Perfect Continuous",
]

# (item, sentence, verb, mood, tense) from key pages 16-17 (Exercise 45).
EX45 = [
    (1, "The river flows under the bridge.", "flows", "Indicative", "Simple Present"),
    (2, "I shall answer the letter to night.", "shall answer", "Indicative", "Simple Future"),
    (3, "I knew he was there, for I had seen him come.", "knew", "Indicative", "Simple Past"),
    (3, "I knew he was there, for I had seen him come.", "was", "Indicative", "Simple Past"),
    (3, "I knew he was there, for I had seen him come.", "had seen", "Indicative", "Past Perfect"),
    (4, "It has been raining all night.", "has been raining", "Indicative", "Present Perfect Continuous"),
    (5, "I hear he has passed all right.", "hear", "Indicative", "Simple Present"),
    (5, "I hear he has passed all right.", "has passed", "Indicative", "Present Perfect"),
    (6, "I had finished when he came.", "had finished", "Indicative", "Past Perfect"),
    (6, "I had finished when he came.", "came", "Indicative", "Simple Past"),
    (7, "He takes but little pride in his work.", "takes", "Indicative", "Simple Present"),
    (8, "I have been living here for months.", "have been living", "Indicative", "Present Perfect Continuous"),
    (9, "Be good, sweet maid.", "Be", "Imperative", "Simple Present"),
    (10, "By this time tomorrow I shall have reached my home.", "shall have reached", "Indicative", "Future Perfect"),
    (11, "It is time we left.", "is", "Indicative", "Simple Present"),
    (11, "It is time we left.", "left", "Subjunctive", "Simple Past"),
    (12, "He told me that he had finished the work.", "told", "Indicative", "Simple Past"),
    (12, "He told me that he had finished the work.", "had finished", "Indicative", "Past Perfect"),
    (13, "God forgive you!", "forgive", "Subjunctive", "Simple Present"),
    (14, "He is waiting for you in the compound.", "is waiting", "Indicative", "Present Continuous"),
    (15, "Piper, pipe that song again.", "pipe", "Imperative", "Simple Present"),
    (16, "I am hoping to get a holiday soon.", "am hoping", "Indicative", "Present Continuous"),
    (17, "Perhaps it were better to obey him.", "were", "Subjunctive", "Simple Past"),
    (18, "Do noble deeds, not dream them all the day.", "Do", "Imperative", "Simple Present"),
    (18, "Do noble deeds, not dream them all the day.", "dream", "Imperative", "Simple Present"),
    (19, "I shall have plenty of time tomorrow.", "shall have", "Indicative", "Simple Future"),
    (20, "Though this be madness, yet there is method in it.", "be", "Subjunctive", "Simple Present"),
    (21, "The king had never before led his troops in battle.", "had led", "Indicative", "Past Perfect"),
    (22, "If he was guilty, his punishment was too light.", "was", "Indicative", "Simple Past"),
    (23, "We have heard a strange story.", "have heard", "Indicative", "Present Perfect"),
    (24, "The travellers, all of whom had seen the chameleon, could not agree about its colour.", "had seen", "Indicative", "Past Perfect"),
    (24, "The travellers, all of whom had seen the chameleon, could not agree about its colour.", "could (not) agree", "Indicative", "Simple Past"),
    (25, "Beware lest something worse should happen to you.", "Beware", "Imperative", "Simple Present"),
    (25, "Beware lest something worse should happen to you.", "happen", "Subjunctive", "Simple Present"),
    (26, "The farmer is cutting the corn which has ripened.", "is cutting", "Indicative", "Present Continuous"),
    (26, "The farmer is cutting the corn which has ripened.", "has ripened", "Indicative", "Present Perfect"),
    (27, "I wish my brother were here.", "wish", "Indicative", "Simple Present"),
    (27, "I wish my brother were here.", "were", "Subjunctive", "Simple Past"),
    (28, "She would rather we stayed till tomorrow.", "would", "Indicative", "Simple Past"),
    (28, "She would rather we stayed till tomorrow.", "stayed", "Subjunctive", "Simple Past"),
]

GEN = [
    ("The mood of 'If I were you, I would rest.' is:", "Subjunctive", ["Indicative", "Imperative", "Infinitive"],
     "'Were' expresses an unreal or imagined condition, which is the subjunctive.",
     ["Correct: 'were' in an unreal condition is subjunctive.", "Wrong: the indicative states facts.", "Wrong: the imperative gives commands.", "Wrong: infinitive is not a mood."]),
    ("The mood of 'Close the door.' is:", "Imperative", ["Indicative", "Subjunctive", "Infinitive"],
     "A command is in the imperative mood.",
     ["Correct: it gives a command.", "Wrong: the indicative states facts or asks questions.", "Wrong: the subjunctive expresses wishes or doubt.", "Wrong: infinitive is not a mood."]),
    ("The mood of 'She sings well.' is:", "Indicative", ["Subjunctive", "Imperative", "Infinitive"],
     "A plain statement of fact is in the indicative mood.",
     ["Correct: it states a fact.", "Wrong: it is not an unreal or wished-for statement.", "Wrong: it is not a command.", "Wrong: infinitive is not a mood."]),
    ("The tense of 'They have finished the work.' is:", "Present Perfect", ["Simple Past", "Past Perfect", "Simple Present"],
     "'Have finished' links a past action to the present.",
     ["Correct: 'have finished' is present perfect.", "Wrong: simple past uses no 'have'.", "Wrong: past perfect uses 'had'.", "Wrong: simple present uses no 'have' with the past participle."]),
    ("The tense of 'I had eaten before he arrived.' is:", "Past Perfect", ["Present Perfect", "Simple Past", "Future Perfect"],
     "'Had eaten' shows an action completed before another past action.",
     ["Correct: 'had eaten' is past perfect.", "Wrong: present perfect uses 'have'.", "Wrong: simple past has no 'had'.", "Wrong: future perfect uses 'will have'."]),
    ("The tense of 'We will leave tomorrow.' is:", "Simple Future", ["Simple Present", "Present Continuous", "Simple Past"],
     "'Will leave' refers to a future action.",
     ["Correct: 'will leave' is simple future.", "Wrong: simple present refers to habits or facts.", "Wrong: present continuous uses 'is' or 'are' with '-ing'.", "Wrong: simple past refers to a finished past action."]),
    ("The tense of 'She is reading a novel.' is:", "Present Continuous", ["Simple Present", "Present Perfect", "Simple Past"],
     "'Is reading' shows an action happening now.",
     ["Correct: 'is reading' shows an action in progress now.", "Wrong: simple present has no 'is' with '-ing'.", "Wrong: present perfect uses 'have' or 'has'.", "Wrong: simple past shows a finished past action."]),
    ("The mood of 'Long live the king!' is:", "Subjunctive", ["Indicative", "Imperative", "Infinitive"],
     "The sentence expresses a wish, which is the subjunctive.",
     ["Correct: it expresses a wish.", "Wrong: it is not a plain statement of fact.", "Wrong: it is not a command.", "Wrong: infinitive is not a mood."]),
    ("The tense of 'He had been working for hours.' is:", "Past Perfect Continuous", ["Present Perfect Continuous", "Past Perfect", "Simple Past"],
     "'Had been working' shows an action continuing up to a past time.",
     ["Correct: 'had been working' is past perfect continuous.", "Wrong: present perfect continuous uses 'have' or 'has'.", "Wrong: past perfect is 'had' plus the participle, without '-ing'.", "Wrong: simple past has no 'had'."]),
    ("'I wish I were rich.' The verb 'were' is in the:", "Subjunctive", ["Indicative", "Imperative", "Infinitive"],
     "'Were' expresses an unreal wish, so it is subjunctive.",
     ["Correct: it expresses an unreal wish.", "Wrong: it is not stating a fact.", "Wrong: it is not a command.", "Wrong: infinitive is not a mood."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex45_questions():
    out = []
    n = 0
    for item, sentence, verb, mood, tense in EX45:
        # Mood
        pos = n % 4
        other_moods = [m for m in MOODS if m != mood]
        options = [mood] + other_moods + ["Infinitive"]
        options = options[:4]
        reasons = [f"Correct: '{verb}' is in the {mood.lower()} mood."] + \
                  [f"Wrong: '{verb}' is not in the {m.lower()} mood here." for m in other_moods[:2]] + \
                  [f"Wrong: infinitive is not a mood."]
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 45, item {item}",
                    "stem": f'In "{sentence}", what is the mood of "{verb}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{verb}' is in the {mood.lower()} mood.", "reasons": _rotate(reasons, pos)})
        n += 1
        # Tense
        pos = n % 4
        distractors = [t for t in TENSES if t != tense][:3]
        options = [tense] + distractors
        reasons = [f"Correct: '{verb}' is {tense.lower()}."] + \
                  [f"Wrong: '{verb}' is not {d.lower()} here." for d in distractors]
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 45, item {item}",
                    "stem": f'In "{sentence}", what is the tense of "{verb}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{verb}' is in the {tense.lower()} tense.", "reasons": _rotate(reasons, pos)})
        n += 1
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 23, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
