"""Chapter 5 (Kinds of Nouns): Exercise in Grammar 3 (book items 1-25) plus generated questions.

Book items: each noun in the printed sentences is asked for its kind. The correct kind comes from the
answer key (page 5). Items 10 and 12 in the key name different nouns from the printed sentences
(Nile for Godavari, Nelson for Nehru); there the kind is classed from the printed noun and flagged.
Distractors are the other three kinds of noun.
"""

KINDS = ["Common noun", "Proper noun", "Collective noun", "Abstract noun"]
KIND_REASON = {
    "Common noun": "a name shared by every person or thing of the same kind",
    "Proper noun": "the name of a particular person or place",
    "Collective noun": "the name of a group taken together as one whole",
    "Abstract noun": "the name of a quality, action or state",
}
LETTERS = "ABCD"

# (book item, sentence, noun, kind)
EX3 = [
    (1, "The crowd was very big.", "crowd", "Collective noun"),
    (2, "Always speak the truth.", "truth", "Abstract noun"),
    (3, "We all love honesty.", "honesty", "Abstract noun"),
    (4, "Our class consists of twenty pupils.", "class", "Collective noun"),
    (4, "Our class consists of twenty pupils.", "pupils", "Common noun"),
    (5, "The elephant has great strength.", "elephant", "Common noun"),
    (5, "The elephant has great strength.", "strength", "Abstract noun"),
    (6, "Solomon was famous for his wisdom.", "Solomon", "Proper noun"),
    (6, "Solomon was famous for his wisdom.", "wisdom", "Abstract noun"),
    (7, "Cleanliness is next to godliness.", "Cleanliness", "Abstract noun"),
    (7, "Cleanliness is next to godliness.", "godliness", "Abstract noun"),
    (8, "We saw a fleet of ships in the harbour.", "fleet", "Collective noun"),
    (8, "We saw a fleet of ships in the harbour.", "ships", "Common noun"),
    (8, "We saw a fleet of ships in the harbour.", "harbour", "Common noun"),
    (9, "The class is studying grammar.", "class", "Collective noun"),
    (9, "The class is studying grammar.", "grammar", "Abstract noun"),
    (10, "The Godavari overflows its banks every year.", "Godavari", "Proper noun"),
    (10, "The Godavari overflows its banks every year.", "banks", "Common noun"),
    (10, "The Godavari overflows its banks every year.", "year", "Common noun"),
    (11, "A committee of five was appointed.", "committee", "Collective noun"),
    (12, "Jawaharlal Nehru was the first Prime Minister of India.", "Jawaharlal Nehru", "Proper noun"),
    (12, "Jawaharlal Nehru was the first Prime Minister of India.", "Prime Minister", "Common noun"),
    (12, "Jawaharlal Nehru was the first Prime Minister of India.", "India", "Proper noun"),
    (13, "The soldiers were rewarded for their bravery.", "soldiers", "Common noun"),
    (13, "The soldiers were rewarded for their bravery.", "bravery", "Abstract noun"),
    (14, "Without health there is no happiness.", "health", "Abstract noun"),
    (14, "Without health there is no happiness.", "happiness", "Abstract noun"),
    (15, "He gave me a bunch of grapes.", "bunch", "Collective noun"),
    (15, "He gave me a bunch of grapes.", "grapes", "Common noun"),
    (16, "I recognized your voice at once.", "voice", "Common noun"),
    (17, "Our team is better than theirs.", "team", "Collective noun"),
    (18, "Never tell a lie.", "lie", "Abstract noun"),
    (19, "Wisdom is better than strength.", "Wisdom", "Abstract noun"),
    (19, "Wisdom is better than strength.", "strength", "Abstract noun"),
    (20, "He sets a high value on his time.", "value", "Abstract noun"),
    (20, "He sets a high value on his time.", "time", "Abstract noun"),
    (21, "I believe in his innocence.", "innocence", "Abstract noun"),
    (22, "This room is thirty feet in length.", "room", "Common noun"),
    (22, "This room is thirty feet in length.", "feet", "Common noun"),
    (22, "This room is thirty feet in length.", "length", "Abstract noun"),
    (23, "I often think of the happy days of childhood.", "days", "Common noun"),
    (23, "I often think of the happy days of childhood.", "childhood", "Abstract noun"),
    (24, "The streets of some of our cities are noted for their crookedness.", "streets", "Common noun"),
    (24, "The streets of some of our cities are noted for their crookedness.", "cities", "Common noun"),
    (24, "The streets of some of our cities are noted for their crookedness.", "crookedness", "Abstract noun"),
    (25, "What is your verdict, gentlemen of the jury?", "verdict", "Abstract noun"),
    (25, "What is your verdict, gentlemen of the jury?", "gentlemen", "Common noun"),
    (25, "What is your verdict, gentlemen of the jury?", "jury", "Collective noun"),
]
FLAGGED_ITEMS = {10, 12}

GENERATED = [
    ("A common noun is the name given in common to:", ["one particular person", "every person or thing of the same kind", "a quality or state", "a group taken as one whole"], "B",
     "A common noun names every member of a class.", ["Wrong: a name for one particular person is a proper noun.", "Correct: a common noun is shared by every person or thing of the same kind.",
      "Wrong: a quality or state is an abstract noun.", "Wrong: a group taken as one whole is a collective noun."]),
    ("Which is a proper noun?", ["girl", "Sita", "city", "country"], "B",
     "'Sita' names one particular girl, so it is a proper noun.", ["Wrong: 'girl' is a common noun.", "Correct: 'Sita' is the name of a particular girl.",
      "Wrong: 'city' is a common noun.", "Wrong: 'country' is a common noun."]),
    ("Which is a collective noun?", ["happiness", "fleet", "brother", "Nile"], "B",
     "A fleet is a collection of ships spoken of as one whole.", ["Wrong: 'happiness' is an abstract noun.", "Correct: 'fleet' is a collection of ships.",
      "Wrong: 'brother' is a common noun.", "Wrong: 'Nile' is a proper noun."]),
    ("Which is an abstract noun?", ["table", "kindness", "river", "book"], "B",
     "'Kindness' names a quality, apart from any person.", ["Wrong: 'table' is a common noun.", "Correct: 'kindness' names a quality.",
      "Wrong: 'river' is a common noun.", "Wrong: 'book' is a common noun."]),
    ("'Kindness' is formed from which adjective?", ["kind", "kindle", "kin", "kindly"], "A",
     "Most abstract nouns are formed from adjectives: kindness from kind.", ["Correct: kindness is formed from kind.", "Wrong: 'kindle' is a different word.",
      "Wrong: 'kin' is a different word.", "Wrong: 'kindly' is an adverb, not the source adjective."]),
    ("Which is a countable noun?", ["milk", "book", "sugar", "honesty"], "B",
     "Countable nouns name things we can count and have plurals ('books').", ["Wrong: 'milk' is uncountable.", "Correct: 'book' can be counted.",
      "Wrong: 'sugar' is uncountable.", "Wrong: 'honesty' is uncountable."]),
    ("Which is an uncountable noun?", ["pen", "gold", "apple", "horse"], "B",
     "Uncountable nouns name substances and abstract things, which we cannot count.", ["Wrong: 'pen' can be counted.", "Correct: 'gold' is a substance, not counted.",
      "Wrong: 'apple' can be counted.", "Wrong: 'horse' can be counted."]),
    ("Proper nouns are always written with:", ["a small letter", "a capital letter", "italics", "brackets"], "B",
     "A proper noun begins with a capital letter.", ["Wrong: proper nouns begin with capitals.", "Correct: a proper noun begins with a capital letter.",
      "Wrong: italics are not required.", "Wrong: brackets are not used."]),
    ("'Obedience' is formed from which verb?", ["obey", "obedient", "obeys", "obeyed"], "A",
     "Abstract nouns can be formed from verbs: obedience from obey.", ["Correct: obedience is formed from obey.", "Wrong: 'obedient' is an adjective.",
      "Wrong: 'obeys' is a verb form, not the base verb.", "Wrong: 'obeyed' is a verb form, not the base verb."]),
    ("In 'Kolkata is a city.', the common noun is:", ["Kolkata", "city", "is", "a"], "B",
     "'City' is the name shared by every city; 'Kolkata' is a proper noun.", ["Wrong: 'Kolkata' is a proper noun.", "Correct: 'city' is a common noun.",
      "Wrong: 'is' is a verb.", "Wrong: 'a' is an article."]),
]


def book_questions():
    out = []
    for n, (item, sentence, noun, kind) in enumerate(EX3):
        pos = n % 4
        rest = [k for k in KINDS if k != kind]
        opts = rest[:pos] + [kind] + rest[pos:]
        reasons = []
        for o in opts:
            if o == kind:
                reasons.append(f"Correct: '{noun}' is a {kind.lower()}: {KIND_REASON[kind]}.")
            else:
                reasons.append(f"Wrong: '{noun}' is not a {o.lower()}; it is {KIND_REASON[kind]}.")
        note = " (Key and printed sentence differ here; classed from the printed noun.)" if item in FLAGGED_ITEMS else ""
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 3, item {item}",
                    "stem": f'In "{sentence}", what kind of noun is "{noun}"?',
                    "options": opts, "correct": LETTERS[pos],
                    "explanation": f"'{noun}' is a {kind.lower()}.{note}", "reasons": reasons})
    return out


def generated_questions():
    out = []
    for n, (stem, opts, c, expl, reasons) in enumerate(GENERATED):
        pos = n % 4
        correct_idx = LETTERS.index(c)
        correct_text, correct_reason = opts[correct_idx], reasons[correct_idx]
        other_opts = [o for i, o in enumerate(opts) if i != correct_idx]
        other_reasons = [r for i, r in enumerate(reasons) if i != correct_idx]
        out.append({"source": "Generated", "exercise": "", "stem": stem,
                    "options": other_opts[:pos] + [correct_text] + other_opts[pos:],
                    "correct": LETTERS[pos], "explanation": expl,
                    "reasons": other_reasons[:pos] + [correct_reason] + other_reasons[pos:]})
    return out
