"""Chapter 41 (Some Conjunctions and Their Uses): Exercise in Grammar 99 plus generated questions.

Answers: key page 38 (keyimg p-041). Each italicised word is tagged as a preposition, adverb or
conjunction. Options are the three parts of speech plus adjective as a distractor.
"""

LETTERS = "ABCD"
PARTS = ["Preposition", "Adverb", "Conjunction", "Adjective"]

# (item, sentence, italicised word, part of speech) from key page 38.
EX99 = [
    (1, "He came before me.", "before", "Preposition"),
    (2, "He came two hours before.", "before", "Adverb"),
    (3, "He came before I left.", "before", "Conjunction"),
    (4, "Have you ever seen him since?", "since", "Adverb"),
    (5, "I have not seen him since Monday.", "since", "Preposition"),
    (6, "I have not seen him since he was a child.", "since", "Conjunction"),
    (7, "Man wants but little here below.", "but", "Adverb"),
    (8, "He yearns for nothing but money.", "but", "Preposition"),
    (9, "We shall go, but you will remain.", "but", "Conjunction"),
    (10, "He arrived after the meeting was adjourned.", "after", "Conjunction"),
    (11, "He arrived after the meeting.", "after", "Preposition"),
    (12, "He arrived soon after.", "after", "Adverb"),
]

GEN = [
    ("'Since' in 'I have not seen him since he was a child.' is a:", "Conjunction", ["Preposition", "Adverb", "Adjective"],
     "'Since' joins a clause ('he was a child'), so it is a conjunction.",
     ["Correct: 'since' joins two clauses.", "Wrong: a preposition is followed by a noun, not a clause.", "Wrong: an adverb does not join clauses.", "Wrong: 'since' does not describe a noun here."]),
    ("'Since' in 'I have not seen him since Monday.' is a:", "Preposition", ["Conjunction", "Adverb", "Adjective"],
     "'Since' is followed by the noun 'Monday', so it is a preposition.",
     ["Correct: 'since' is followed by a noun.", "Wrong: 'since' does not join a clause here.", "Wrong: it is not used alone at the end.", "Wrong: it does not describe a noun."]),
    ("'Since' in 'Many things have happened since.' is a:", "Adverb", ["Conjunction", "Preposition", "Adjective"],
     "'Since' stands alone with no noun or clause after it, so it is an adverb.",
     ["Correct: 'since' stands alone.", "Wrong: a conjunction needs a clause after it.", "Wrong: a preposition needs a noun after it.", "Wrong: it does not describe a noun."]),
    ("'As' in 'As it was raining, we stayed in.' is a:", "Conjunction", ["Preposition", "Adverb", "Adjective"],
     "'As' joins the clause 'it was raining' to the main clause.",
     ["Correct: 'as' joins two clauses.", "Wrong: a preposition needs a noun after it.", "Wrong: an adverb does not join clauses.", "Wrong: it does not describe a noun."]),
    ("'Before' in 'Before the match, we ate.' is a:", "Preposition", ["Conjunction", "Adverb", "Adjective"],
     "'Before' is followed by the noun 'the match', so it is a preposition.",
     ["Correct: 'before' is followed by a noun.", "Wrong: no clause follows 'before' here.", "Wrong: it does not stand alone.", "Wrong: it does not describe a noun."]),
    ("'After' in 'He came after.' is a:", "Adverb", ["Conjunction", "Preposition", "Adjective"],
     "'After' stands alone, so it is an adverb.",
     ["Correct: 'after' stands alone.", "Wrong: a conjunction needs a clause after it.", "Wrong: a preposition needs a noun after it.", "Wrong: it does not describe a noun."]),
    ("'But' in 'Nothing but love matters.' is a:", "Preposition", ["Conjunction", "Adverb", "Adjective"],
     "'But' means 'except' and is followed by the noun 'love', so it is a preposition.",
     ["Correct: 'but' means 'except' and takes a noun.", "Wrong: 'but' here does not join clauses.", "Wrong: it does not stand alone.", "Wrong: it does not describe a noun."]),
    ("'Yet' in 'He is poor, yet honest.' is a:", "Conjunction", ["Preposition", "Adverb", "Adjective"],
     "'Yet' joins the two contrasting adjectives in the sentence, so it is a conjunction.",
     ["Correct: 'yet' joins two parts with contrast.", "Wrong: a preposition takes a noun after it.", "Wrong: it does not describe the verb.", "Wrong: it does not describe a noun."]),
    ("'Lest' in 'Work hard lest you fail.' is a:", "Conjunction", ["Preposition", "Adverb", "Adjective"],
     "'Lest' joins the clause 'you fail' to the main clause.",
     ["Correct: 'lest' joins two clauses.", "Wrong: a preposition takes a noun after it.", "Wrong: an adverb does not join clauses.", "Wrong: it does not describe a noun."]),
    ("'Until' in 'I will wait until you come.' is a:", "Conjunction", ["Preposition", "Adverb", "Adjective"],
     "'Until' joins the clause 'you come' to the main clause.",
     ["Correct: 'until' joins two clauses.", "Wrong: a preposition takes a noun after it, not a clause.", "Wrong: an adverb does not join clauses.", "Wrong: it does not describe a noun."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex99_questions():
    out = []
    for n, (item, sentence, word, part) in enumerate(EX99):
        others = [p for p in PARTS if p != part]
        pos = n % 4
        options = [part] + others[:3]
        reasons = [f"Correct: '{word}' is a {part.lower()} here."] + \
                  [f"Wrong: '{word}' is not a {o.lower()} here." for o in others[:3]]
        out.append({"chapter": 41, "source": "Book", "exercise": f"Exercise in Grammar 99, item {item}",
                    "stem": f'In "{sentence}", what part of speech is "{word}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is a {part.lower()} here.", "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 41, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Composition 100 (printed as Composition, but it is a conjunction fill-in): key page 38
# (keyimg p-041). Only items where the key answer clearly fits a single blank are used. Two-blank items,
# items with alternatives on the key, and items where the key looks misaligned are skipped.
EX100 = [
    (1, "I am in the right, ____ you are in the wrong.", "but"),
    (2, "The most exquisite work of literary art exhibits a certain crudeness, ____ we turn to it from nature.", "yet"),
    (3, "____ he had not paid his bill, his electricity was cut off.", "As"),
    (4, "There never can be prosperity in any country ____ all the cultivators of the soil are depressed.", "where"),
    (5, "Giving up wrong pleasure is not self-sacrifice, ____ self-culture.", "but"),
    (6, "Conform thyself then to thy present fortune ____ cut thy coat according to thy cloth.", "and"),
    (7, "Inconsistency consists in a change of conduct ____ there is no change of circumstances which justify it.", "when"),
    (10, "His ambition was inordinate, ____ he was jealous of every man of ability.", "so"),
    (11, "Just laws are no restraint upon the freedom of the good, ____ the good man desires nothing which a just law will interfere with.", "for"),
    (12, "We judge ourselves by what we feel capable of doing, ____ others judge us by what we have already done.", "while"),
    (14, "The fleets of the enemy were not merely defeated, ____ destroyed.", "but"),
    (15, "As long as he lived, he was the guiding-star of a brave nation; ____ he died the little children cried in the street.", "when"),
    (17, "It is “the finest exercise for the body ____ best relaxation for the mind.”", "and"),
    (18, "He abhorred hypocrisy, ____ he was not too stern with the hypocrite.", "but"),
    (19, "Our proudest title is not that we are the contemporaries of Darwin, ____ that we are the descendants of Shakespeare.", "but"),
    (20, "He knew more about printed books ____ any man living.", "than"),
    (21, "Are you impatient with the lark ____ he sings rather than talks?", "that"),
    (22, "Trust the man who hesitates in his speech and is quick and steady in action, ____ beware of long arguments and long beards.", "but"),
    (23, "Religion does not banish mirth ____ only moderates and sets rules to it.", "but"),
    (24, "A man's real character will always be more visible in his household ____ anywhere else.", "than"),
    (26, "He that is slow to anger is better ____ the mighty.", "than"),
    (27, "____ we approached the house, we heard the sound of music.", "When"),
    (28, "The ravine was full of sand now, ____ it had once been full of water.", "but"),
    (31, "Give every man thy ear, ____ few thy voice.", "but"),
    (32, "Virtue ____ wise action lies in the mean between the two extremes of too little and too much.", "or"),
    (33, "And God called the light Day, ____ the darkness He called Night.", "and"),
    (34, "That is a good book which is opened with expectation, ____ closed with profit.", "and"),
    (35, "____ I was in Sri Lanka, I was particularly fascinated by the Coral Gardens of Hikkaduwa.", "When"),
    (36, "The restoration crushed for a time the Puritan party, ____ placed supreme power in the hands of a libertine.", "and"),
    (37, "Of his voyage little is known, ____ that he amused himself with books and with his pen.", "except"),
    (39, "____ Addison was in Ireland, an event occurred to which he owes his high and permanent rank among British writers.", "When"),
    (44, "The right of self-defence is founded in the law of nature, ____ is not and cannot be superseded by the law of society.", "and"),
    (45, "Let the superstructure of life be enjoyment, ____ let its foundation be in solid work.", "but"),
    (48, "A gentleman made it a rule in reading to skip over all sentences ____ he spied a note of admiration at the end.", "unless"),
    (50, "____ I were personally your enemy, I might pity and forgive you.", "If"),
]

EX100_POOL = ["but", "and", "or", "yet", "so", "for", "as", "when", "while", "than", "that", "where",
              "unless", "if", "though", "since", "because", "till", "until", "except"]


def ex100_questions():
    out = []
    for n, (item, sentence, correct) in enumerate(EX100):
        dis = []
        for c in EX100_POOL:
            if c.lower() != correct.lower() and c.lower() not in [d.lower() for d in dis]:
                dis.append(c)
            if len(dis) == 3:
                break
        pos = n % 4
        options = [correct] + dis
        reasons = [f"Correct: '{correct}' joins the two parts of the sentence correctly."] + \
                  [f"Wrong: '{d}' does not fit the meaning of this sentence." for d in dis]
        out.append({"chapter": 41, "source": "Book", "exercise": f"Exercise in Composition 100, item {item}",
                    "stem": f"Fill in the blank with the right conjunction: {sentence}",
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"The right conjunction is '{correct}'.", "reasons": _rotate(reasons, pos)})
    return out
