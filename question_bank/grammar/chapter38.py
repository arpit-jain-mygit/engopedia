"""Chapter 38 (The Preposition): Exercises 64 and 65 plus generated questions.

Answers: key page 26 (keyimg p-029). Exercise 64: which word each preposition governs.
Exercise 65: whether each word is an adverb or a preposition.
"""

LETTERS = "ABCD"

# Exercise in Grammar 64: (item, sentence, preposition, governed word) from key page 26.
EX64 = [
    (1, "Little Jack Horner sat in a corner.", "in", "corner"),
    (2, "Old Mother Hubbard, she went to the cupboard.", "to", "cupboard"),
    (3, "The lion and the unicorn fought for the crown.", "for", "crown"),
    (4, "Humpty Dumpty sat on a wall.", "on", "wall"),
    (5, "Wee Willie Winkie runs through the town.", "through", "town"),
    (6, "She sat by the fire, and told me a tale.", "by", "fire"),
    (7, "Rain, rain, go to Spain, and never come back again.", "to", "Spain"),
    (8, "A fair little girl sat under a tree.", "under", "tree"),
    (9, "Such a number of rocks came over her head.", "of", "rocks"),
    (9, "Such a number of rocks came over her head.", "over", "head"),
    (10, "John Gilpin was a citizen of credit and renown.", "of", "credit"),
    (11, "Will you walk into my parlour? said the spider to the fly.", "into", "parlour"),
    (11, "Will you walk into my parlour? said the spider to the fly.", "to", "fly"),
    (12, "Into the street the Piper stepped.", "into", "street"),
    (13, "I can never return with my poor dog Tray.", "with", "dog"),
    (14, "He worked and sang from morn till night.", "from", "morn"),
    (14, "He worked and sang from morn till night.", "till", "night"),
    (15, "They all ran after the farmer's wife, who cut off their tails with a carving knife.", "after", "wife"),
    (15, "They all ran after the farmer's wife, who cut off their tails with a carving knife.", "with", "knife"),
    (16, "The boy ate his breakfast by a purling brook which through his mother's orchard ran.", "by", "brook"),
    (16, "The boy ate his breakfast by a purling brook which through his mother's orchard ran.", "through", "orchard"),
    (17, "Old John with white hair, does laugh away care, sitting under the oak, among the old folk.", "with", "hair"),
    (17, "Old John with white hair, does laugh away care, sitting under the oak, among the old folk.", "under", "oak"),
    (17, "Old John with white hair, does laugh away care, sitting under the oak, among the old folk.", "among", "folk"),
    (18, "They rise with the morning lark, and labour till almost dark.", "with", "lark"),
    (18, "They rise with the morning lark, and labour till almost dark.", "till", "dark"),
    (19, "By the Nine Gods he swore.", "By", "gods"),
    (20, "Under a spreading chestnut-tree the village smithy stands.", "Under", "chestnut-tree"),
    (21, "He goes on Sunday to church, and sits among his boys.", "on", "Sunday"),
    (21, "He goes on Sunday to church, and sits among his boys.", "to", "church"),
    (21, "He goes on Sunday to church, and sits among his boys.", "among", "boys"),
    (22, "I bring fresh showers for the thirsting flowers, from the seas and the streams.", "for", "flowers"),
    (22, "I bring fresh showers for the thirsting flowers, from the seas and the streams.", "from", "seas"),
    (23, "Her arms across her breast she laid.", "across", "breast"),
    (24, "Mine be a cot beside the hill.", "beside", "hill"),
    (25, "Around my ivied porch shall spring each fragrant flower that drinks the dew.", "Around", "porch"),
    (26, "One crowded hour of glorious life is worth an age without a name.", "of", "life"),
    (26, "One crowded hour of glorious life is worth an age without a name.", "without", "name"),
    (27, "I tried to reason him out of his fears.", "out of", "fears"),
]

# Exercise in Grammar 65: (item, sentence, word, part of speech) from key page 26.
EX65 = [
    (1, "Come down.", "down", "Adverb"),
    (2, "We sailed down the river.", "down", "Preposition"),
    (3, "The man walked round the house.", "round", "Preposition"),
    (4, "He sat on a stool.", "on", "Preposition"),
    (5, "The carriage moved on.", "on", "Adverb"),
    (6, "The soldiers passed by.", "by", "Adverb"),
    (7, "The man turned round.", "round", "Adverb"),
    (8, "We all went in.", "in", "Adverb"),
    (9, "He is in the room.", "in", "Preposition"),
    (10, "He hid behind the door.", "behind", "Preposition"),
    (11, "I left him behind.", "behind", "Adverb"),
    (12, "She sat by the cottage door.", "by", "Preposition"),
    (13, "The path leads through the woods.", "through", "Preposition"),
    (14, "I have read the book through.", "through", "Adverb"),
    (15, "The storm is raging without.", "without", "Adverb"),
    (16, "We cannot live without water.", "without", "Preposition"),
]

GOVERNED = [g for _, _, _, g in EX64]


def _art(word):
    return ("an " if word[0].lower() in "aeiou" else "a ") + word.lower()


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex64_questions():
    out = []
    for n, (item, sentence, prep, gov) in enumerate(EX64):
        others = [g for g in GOVERNED if g != gov]
        distractors = []
        for g in others:
            if g not in distractors:
                distractors.append(g)
            if len(distractors) == 3:
                break
        options = [gov] + distractors
        pos = n % 4
        reasons = [f"Correct: '{gov}' is the word the preposition '{prep}' governs."] + \
                  [f"Wrong: '{d}' is not the word '{prep}' governs here." for d in distractors]
        out.append({"chapter": 38, "source": "Book", "exercise": f"Exercise in Grammar 64, item {item}",
                    "stem": f'In "{sentence}", which word does the preposition "{prep}" govern?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{prep}' governs '{gov}'.", "reasons": _rotate(reasons, pos)})
    return out


def ex65_questions():
    out = []
    for n, (item, sentence, word, pos_name) in enumerate(EX65):
        other = "Preposition" if pos_name == "Adverb" else "Adverb"
        options = [pos_name, other, "Adjective", "Conjunction"]
        pos = n % 4
        reasons = [f"Correct: '{word}' is used as {_art(pos_name)} here." if o == pos_name
                   else f"Wrong: '{word}' is not used as {_art(o)} here." for o in options]
        out.append({"chapter": 38, "source": "Book", "exercise": f"Exercise in Grammar 65, item {item}",
                    "stem": f'In "{sentence}", is "{word}" an adverb or a preposition?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is an {pos_name.lower()} here." if pos_name == "Adverb"
                                   else f"'{word}' is a {pos_name.lower()} here.",
                    "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Grammar 68: force of the preposition (key page 27, keyimg p-030).
# (item, sentence, preposition, force)
EX68 = [
    (1, "I will do it for all you may say.", "for", "concession"),
    (2, "This work is beyond his capacity.", "beyond", "excess"),
    (3, "I would do anything before that.", "before", "time"),
    (4, "After this I wash my hands of you.", "After", "time"),
    (5, "It is cool for May.", "for", "contrast"),
    (6, "She made grand preparations against his coming.", "against", "anticipation"),
    (7, "It was all through you that we failed.", "through", "cause"),
    (8, "He was left for dead on the field.", "for", "supposition"),
    (9, "All that they did was piety to this.", "to", "reference"),
    (10, "The lifeboat made straight for the sinking ship.", "for", "direction"),
    (11, "I shall do my duty by him.", "by", "direction"),
    (12, "He married for money.", "for", "purpose"),
    (13, "A man is a man for all that.", "for", "contrast"),
    (14, "Nothing will come of nothing.", "of", "origin"),
    (15, "With all his faults I still like him.", "With", "concession"),
]
FORCES = [f for _, _, _, f in EX68]

# Generated questions for Chapter 38.
GEN38 = [
    ("Which preposition is correct: 'She is good ____ mathematics.'", "at", ["in", "on", "to"],
     "'Good at' is the fixed phrase for skill in a subject.",
     ["Correct: 'good at' is the fixed phrase.", "Wrong: 'good in' is not idiomatic here.", "Wrong: 'good on' is not idiomatic here.", "Wrong: 'good to' does not fit a skill."]),
    ("Which preposition is correct: 'He arrived ____ the station at noon.'", "at", ["in", "on", "into"],
     "'At' is used for a point of place, such as a station.",
     ["Correct: 'at' is used for a point of place.", "Wrong: 'in' suggests an enclosed area.", "Wrong: 'on' suggests a surface.", "Wrong: 'into' shows movement inside."]),
    ("Which preposition is correct: 'The book is ____ the table.'", "on", ["in", "at", "over"],
     "'On' shows a surface, which is the table top.",
     ["Correct: 'on' shows a surface.", "Wrong: 'in' suggests an enclosed space.", "Wrong: 'at' shows a point.", "Wrong: 'over' suggests above without touching."]),
    ("Which preposition is correct: 'I will meet you ____ Monday.'", "on", ["in", "at", "for"],
     "Days of the week take 'on'.",
     ["Correct: days of the week take 'on'.", "Wrong: 'in' is used for months and years.", "Wrong: 'at' is used for times of the day.", "Wrong: 'for' shows duration or purpose."]),
    ("Which preposition is correct: 'She has lived here ____ 2010.'", "since", ["for", "from", "by"],
     "'Since' points to a starting point in time.",
     ["Correct: 'since' points to a starting point.", "Wrong: 'for' is used with a period of time.", "Wrong: 'from' marks a starting place or source.", "Wrong: 'by' means no later than."]),
    ("Which preposition is correct: 'He is afraid ____ dogs.'", "of", ["from", "to", "by"],
     "'Afraid of' is the fixed phrase.",
     ["Correct: 'afraid of' is the fixed phrase.", "Wrong: 'afraid from' is not idiomatic.", "Wrong: 'afraid to' takes an infinitive, not a noun.", "Wrong: 'afraid by' is not idiomatic."]),
    ("Which preposition is correct: 'The letter was written ____ pen.'", "with", ["by", "in", "from"],
     "'With' shows the instrument used to write.",
     ["Correct: 'with' shows the instrument.", "Wrong: 'by' shows the doer of an action.", "Wrong: 'in' shows a manner or medium.", "Wrong: 'from' shows origin."]),
    ("Which preposition is correct: 'He walked ____ the bridge.'", "across", ["through", "beside", "upon"],
     "'Across' shows movement from one side to the other.",
     ["Correct: 'across' shows movement from one side to the other.", "Wrong: 'through' suggests passing inside something.", "Wrong: 'beside' means next to.", "Wrong: 'upon' shows position on a surface."]),
    ("Which preposition is correct: 'She is interested ____ music.'", "in", ["on", "for", "at"],
     "'Interested in' is the fixed phrase.",
     ["Correct: 'interested in' is the fixed phrase.", "Wrong: 'interested on' is not idiomatic.", "Wrong: 'interested for' is not idiomatic.", "Wrong: 'interested at' is not idiomatic."]),
    ("Which preposition is correct: 'We waited ____ an hour for the bus.'", "for", ["since", "during", "from"],
     "'For' is used with a length of time.",
     ["Correct: 'for' is used with a length of time.", "Wrong: 'since' points to a starting time.", "Wrong: 'during' is used with an event.", "Wrong: 'from' marks a starting point."]),
]


def ex68_questions():
    out = []
    for n, (item, sentence, prep, force) in enumerate(EX68):
        others = [f for f in FORCES if f != force]
        distractors = []
        for f in others:
            if f not in distractors:
                distractors.append(f)
            if len(distractors) == 3:
                break
        options = [force] + distractors
        pos = n % 4
        reasons = [f"Correct: '{prep}' shows {force} here."] + \
                  [f"Wrong: '{prep}' does not show {d} here." for d in distractors]
        out.append({"chapter": 38, "source": "Book", "exercise": f"Exercise in Grammar 68, item {item}",
                    "stem": f'In "{sentence}", what is the force of the preposition "{prep}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{prep}' shows {force} here.", "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN38):
        pos = n % 4
        out.append({"chapter": 38, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Grammar 69: fill in the blanks with prepositions (key page 27, keyimg p-030).
# Items 8, 21 and 22 list alternatives on the key and are skipped.
# (item, sentence with blanks, answer as one string, number of blanks)
EX69 = [
    (1, "He lives ____ Hyderabad. He lives ____ 48 Tilak Street.", "in, at"),
    (2, "He started ____ six ____ the morning.", "at, in"),
    (3, "He hanged himself ____ a piece of cloth.", "with"),
    (4, "The portrait was painted ____ a famous artist who flourished ____ the sixteenth century.", "by, in"),
    (5, "I must start ____ dawn to reach the station in time.", "at"),
    (6, "I hope to reach the station ____ an hour at the outside.", "in"),
    (7, "The child has been missing ____ yesterday.", "since"),
    (9, "The mail train is due ____ 3 P.M.", "at"),
    (10, "He travelled thirty kilometres ____ two hours.", "in"),
    (11, "He rushed ____ my room, panting for breath.", "into"),
    (12, "He does not leave his house ____ 9 o'clock.", "before"),
    (13, "The Express departs ____ 3 P.M. ____ Delhi.", "at, from"),
    (14, "Human sacrifices were practised ____ the Nagas.", "by"),
    (15, "I received his message ____ eight o'clock ____ the morning.", "at, in"),
    (16, "____ last month I have seen him but once.", "Since"),
    (17, "____ rice they had curry.", "Besides"),
    (18, "The fever has taken a turn for the better ____ yesterday.", "since"),
    (19, "He has spent his life ____ Kolkata.", "in"),
    (20, "I saw him felling a big tree ____ a hatchet.", "with"),
    (23, "While I was ____ Delhi he was ____ Mumbai.", "in, in"),
    (24, "He was killed ____ the robber ____ a hatchet.", "by, with"),
    (25, "We shall stay three months ____ America.", "in"),
    (26, "____ Rustam and Sohrab, there were three other boys present.", "Besides"),
]
EX69_SINGLE_POOL = ["in", "at", "with", "by", "since", "into", "before", "from", "besides", "among", "for", "of", "on"]
EX69_COMBOS = [c for _, _, c in EX69 if "," in c]


def ex69_questions():
    out = []
    for n, (item, sentence, answer) in enumerate(EX69):
        pos = n % 4
        if "," in answer:
            dis = [c for c in EX69_COMBOS if c != answer]
            dis = list(dict.fromkeys(dis))[:3]
            kind = "the preposition for each blank, in order"
        else:
            dis = [p for p in EX69_SINGLE_POOL if p != answer][:3]
            kind = "the preposition for the blank"
        options = [answer] + dis
        reasons = [f"Correct: '{answer}' is the right preposition(s) here."] + \
                  [f"Wrong: '{d}' does not fit this sentence." for d in dis]
        out.append({"chapter": 38, "source": "Book", "exercise": f"Exercise in Grammar 69, item {item}",
                    "stem": f"Fill in {kind}: {sentence}",
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"The answer is '{answer}'.", "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Grammar 90: prepositions. Key from key page 36 (keyimg p-039).
# Item 16 ("at/in") and item 45 ("from/against") have alternatives on the key, so they are skipped.
EX90 = [
    (1, "Silkworms feed ____ mulberry trees.", "on"),
    (2, "Pavlova excels ____ dancing.", "in"),
    (3, "The wild boar abounds ____ some parts of Europe.", "in"),
    (4, "He has no special liking ____ mathematics.", "for"),
    (5, "Ashoka is worthy ____ remembrance.", "of"),
    (6, "The godown is infested ____ rats.", "with"),
    (7, "There is no exception ____ this rule.", "to"),
    (8, "Nothing conduces ____ happiness so much as contentment.", "to"),
    (9, "Alcohol is injurious ____ health.", "to"),
    (10, "Oil is good ____ burns.", "for"),
    (11, "Invalids are not capable ____ continued exertion.", "of"),
    (12, "The British Parliament is composed ____ two Houses.", "of"),
    (13, "Do not confide your secrets ____ everyone.", "to"),
    (14, "He is abstemious ____ his habits.", "in"),
    (15, "He is ignorant ____ what he pretends to know.", "of"),
    (17, "He has conceived an aversion ____ all kinds of profitable labour.", "to"),
    (18, "Birbal is celebrated ____ his witty sayings.", "for"),
    (19, "The avaricious man is greedy ____ gain.", "for"),
    (20, "The Atlantic separates Europe ____ America.", "from"),
    (22, "Temperance and employment are conducive ____ health.", "to"),
    (23, "A brave boy rescued the child ____ danger.", "from"),
    (24, "Industry is the key ____ success.", "to"),
    (25, "The customs were searching ____ drugs at the airport.", "for"),
    (26, "Elizabeth knew how to inspire her soldiers ____ hope.", "with"),
    (27, "Long indulgence ____ vice impaired his once robust constitution.", "in"),
    (28, "Early rising is beneficial ____ health.", "to"),
    (29, "We should live in a style suited ____ our condition.", "to"),
    (30, "Examinations act as an incentive ____ diligence.", "to"),
    (31, "Hard work and perseverance are indispensable ____ success in life.", "to"),
    (32, "He is too miserly to part ____ his money.", "with"),
    (33, "He is a clever man, but unfortunately diffident ____ his powers.", "about"),
    (34, "Suddenly we were enveloped ____ dense fog.", "in"),
    (35, "Many aspire ____ greatness, but few attained.", "to"),
    (36, "His income is not adequate ____ his wants.", "to"),
    (37, "The soil of Pune is favourable ____ roses.", "to"),
    (38, "I am sick ____ the whole business.", "of"),
    (39, "A car will be a great convenience ____ a busy man like him.", "to"),
    (40, "Whoever acts contrary ____ nature does not go unpunished.", "to"),
    (41, "The accident resulted ____ the death of five people.", "in"),
    (42, "These derelict houses are reproach ____ the city.", "to"),
    (43, "The Germans were called baby-killers and their methods of warfare stigmatized as a reproach ____ civilization.", "to"),
    (44, "The mule was partially relieved ____ the load.", "of"),
    (46, "The facts point ____ a different conclusion.", "to"),
    (47, "Your wish is tantamount ____ a command.", "to"),
    (48, "This state is committed ____ the policy of total prohibition.", "to"),
    (49, "One is sure ____ what one sees.", "of"),
    (50, "He is indifferent alike ____ praise and blame.", "to"),
]

EX90_POOL = ["in", "for", "of", "with", "to", "from", "about", "on", "at"]


def ex90_questions():
    out = []
    for n, (item, sentence, correct) in enumerate(EX90):
        others = [c for c in EX90_POOL if c != correct]
        shift = n % len(others)
        dis = (others[shift:] + others[:shift])[:3]
        pos = n % 4
        options = [correct] + dis
        reasons = [f"Correct: '{correct}' is the preposition this word takes."] + \
                  [f"Wrong: '{d}' is not the preposition used with this word." for d in dis]
        out.append({"chapter": 38, "source": "Book", "exercise": f"Exercise in Grammar 90, item {item}",
                    "stem": f"Fill in the blank with the right preposition: {sentence}",
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"The right preposition is '{correct}'.", "reasons": _rotate(reasons, pos)})
    return out
