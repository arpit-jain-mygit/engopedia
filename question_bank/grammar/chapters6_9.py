"""Chapters 6 to 9 (Gender, Number, Case, Adjective).

Book: Chapters 6, 7 and 8 have no grammar exercise, so they get generated questions only.
Chapter 9 has Exercise in Grammar 6 (classify each adjective); answers come from the key on page 6.
"""

LETTERS = "ABCD"

# ---- Exercise in Grammar 6: (item, sentence, adjective, class from key) ----
EX6 = [
    (1, "The ship sustained heavy damage.", "heavy", "Adjective of Quality"),
    (2, "I have called several times.", "several", "Indefinite Numeral Adjective"),
    (3, "Every dog has his day.", "Every", "Distributive Numeral Adjective"),
    (4, "A live ass is better than a dead lion.", "live", "Adjective of Quality"),
    (4, "A live ass is better than a dead lion.", "better", "Adjective of Quality"),
    (4, "A live ass is better than a dead lion.", "dead", "Adjective of Quality"),
    (5, "Every man has his duties.", "Every", "Distributive Numeral Adjective"),
    (6, "Say the same thing twice over.", "same", "Demonstrative Adjective"),
    (7, "Several persons were present at the time.", "Several", "Indefinite Numeral Adjective"),
    (7, "Several persons were present at the time.", "present", "Descriptive Adjective"),
    (8, "He is a man of few words.", "few", "Indefinite Numeral Adjective"),
    (9, "Neither party is quite in the right.", "Neither", "Distributive Numeral Adjective"),
    (10, "What time is it?", "What", "Interrogative Adjective"),
    (11, "Which pen do you prefer?", "Which", "Interrogative Adjective"),
    (12, "The way was long, the wind was cold, the minstrel was infirm and old.", "long", "Adjective of Quality"),
    (12, "The way was long, the wind was cold, the minstrel was infirm and old.", "cold", "Adjective of Quality"),
    (12, "The way was long, the wind was cold, the minstrel was infirm and old.", "infirm", "Adjective of Quality"),
    (12, "The way was long, the wind was cold, the minstrel was infirm and old.", "old", "Adjective of Quality"),
    (13, "He comes here every day.", "every", "Distributive Numeral Adjective"),
    (14, "I have not seen him for several days.", "several", "Indefinite Numeral Adjective"),
    (15, "There should not be much talk and little work.", "much", "Adjective of Quantity"),
    (15, "There should not be much talk and little work.", "little", "Adjective of Quantity"),
    (16, "Abdul won the second prize.", "second", "Definite Numeral Adjective"),
    (17, "The child fell down from the great height.", "great", "Descriptive Adjective"),
    (18, "He was absent last week.", "absent", "Descriptive Adjective"),
    (19, "He died a glorious death.", "glorious", "Descriptive Adjective"),
    (20, "A small leak may sink a great ship.", "small", "Descriptive Adjective"),
    (20, "A small leak may sink a great ship.", "great", "Descriptive Adjective"),
    (21, "Good wine needs no bush.", "Good", "Descriptive Adjective"),
    (22, "I like the little pedlar who has a crooked nose.", "little", "Adjective of Quantity"),
    (22, "I like the little pedlar who has a crooked nose.", "crooked", "Adjective of Quality"),
    (23, "King Francis was a hearty King, and loved a royal sport.", "hearty", "Adjective of Quality"),
    (23, "King Francis was a hearty King, and loved a royal sport.", "royal", "Adjective of Quality"),
    (24, "In the furrowed land the toilsome and patient oxen stand.", "furrowed", "Adjective of Quality"),
    (24, "In the furrowed land the toilsome and patient oxen stand.", "toilsome", "Adjective of Quality"),
    (25, "My uncle lives in the next house.", "next", "Descriptive Adjective"),
    (26, "Some dreams are like reality.", "Some", "Indefinite Numeral Adjective"),
    (27, "A cross child is not liked.", "cross", "Descriptive Adjective"),
    (28, "It is an ill wind that blows nobody any good.", "ill", "Descriptive Adjective"),
    (28, "It is an ill wind that blows nobody any good.", "any", "Adjective of Quantity"),
]

# Wrong options per class, drawn from the same family first.
WRONG = {
    "Adjective of Quality": ["Adjective of Quantity", "Indefinite Numeral Adjective", "Interrogative Adjective"],
    "Descriptive Adjective": ["Adjective of Quantity", "Indefinite Numeral Adjective", "Interrogative Adjective"],
    "Adjective of Quantity": ["Adjective of Quality", "Indefinite Numeral Adjective", "Distributive Numeral Adjective"],
    "Indefinite Numeral Adjective": ["Distributive Numeral Adjective", "Definite Numeral Adjective", "Adjective of Quantity"],
    "Distributive Numeral Adjective": ["Indefinite Numeral Adjective", "Definite Numeral Adjective", "Adjective of Quantity"],
    "Definite Numeral Adjective": ["Indefinite Numeral Adjective", "Distributive Numeral Adjective", "Adjective of Quantity"],
    "Demonstrative Adjective": ["Interrogative Adjective", "Indefinite Numeral Adjective", "Adjective of Quality"],
    "Interrogative Adjective": ["Demonstrative Adjective", "Indefinite Numeral Adjective", "Adjective of Quality"],
}


def _rotate(items, correct_index, pos):
    """Place the correct item at position pos; keep the other items in order."""
    others = [x for i, x in enumerate(items) if i != correct_index]
    return others[:pos] + [items[correct_index]] + others[pos:]


def book_questions():
    out = []
    for n, (item, sentence, word, label) in enumerate(EX6):
        pos = n % 4
        options = [label] + WRONG[label]
        opts = _rotate(options, 0, pos)
        reasons = _rotate(
            [f"Correct: '{word}' is {label.lower()}."] +
            [f"Wrong: '{word}' is {label.lower()}, not {o.lower()}." for o in WRONG[label]],
            0, pos)
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 6, item {item}",
                    "stem": f'In "{sentence}", what kind of adjective is "{word}"?',
                    "options": opts, "correct": LETTERS[pos],
                    "explanation": f"'{word}' is {label.lower()}.", "reasons": reasons})
    return out


# ---- Generated questions: (chapter, stem, correct, wrong x3, explanation, correct reason, wrong reasons) ----
GEN = [
    (6, "The feminine of 'actor' is:", "actress", ["actor", "he-actor", "male actor"],
     "'Actress' is the feminine form.", ["Wrong: 'actor' is the masculine form.", "Wrong: 'he-actor' is not used.", "Wrong: 'male actor' is masculine."]),
    (6, "The feminine of 'king' is:", "queen", ["king", "kingess", "kingina"],
     "'Queen' is the feminine form.", ["Wrong: 'king' is masculine.", "Wrong: 'kingess' is not a word.", "Wrong: 'kingina' is not a word."]),
    (6, "The masculine of 'mare' is:", "stallion", ["bull", "cow", "hen"],
     "A stallion is the male horse.", ["Wrong: a bull is a male cattle.", "Wrong: a cow is female.", "Wrong: a hen is female."]),
    (6, "Which noun is of common gender?", "child", ["actress", "boy", "king"],
     "'Child' can be male or female.", ["Wrong: 'actress' is feminine.", "Wrong: 'boy' is masculine.", "Wrong: 'king' is masculine."]),
    (6, "The feminine of 'nephew' is:", "niece", ["aunt", "sister", "cousin"],
     "A niece is a daughter of a sibling.", ["Wrong: an aunt is a sister of a parent.", "Wrong: a sister is a female sibling, not a niece.", "Wrong: a cousin is a child of an uncle or aunt."]),
    (6, "Which noun is of neuter gender?", "table", ["mother", "girl", "boy"],
     "'Table' is a thing without sex, so it is neuter.", ["Wrong: 'mother' is feminine.", "Wrong: 'girl' is feminine.", "Wrong: 'boy' is masculine."]),
    (6, "Which noun is masculine?", "boy", ["girl", "cow", "queen"],
     "'Boy' is a male person.", ["Wrong: 'girl' is feminine.", "Wrong: 'cow' is feminine.", "Wrong: 'queen' is feminine."]),
    (6, "The feminine of 'duke' is:", "duchess", ["duke", "duck", "dukess"],
     "'Duchess' is the feminine form.", ["Wrong: 'duke' is masculine.", "Wrong: 'duck' is a bird.", "Wrong: 'dukess' is not a word."]),
    (6, "The feminine of 'tiger' is:", "tigress", ["tiger", "cub", "lion"],
     "'Tigress' is the female tiger.", ["Wrong: 'tiger' is masculine.", "Wrong: 'cub' is young, not female.", "Wrong: 'lion' is a different animal."]),
    (6, "The feminine of 'host' is:", "hostess", ["hostage", "hosting", "host"],
     "'Hostess' is the feminine form.", ["Wrong: a hostage is a captive.", "Wrong: 'hosting' is a verb form.", "Wrong: 'host' is masculine."]),
    (7, "The plural of 'child' is:", "children", ["childs", "childes", "child"],
     "'Children' is the irregular plural.", ["Wrong: 'childs' is not correct.", "Wrong: 'childes' is not correct.", "Wrong: 'child' is singular."]),
    (7, "The plural of 'knife' is:", "knives", ["knifes", "knifees", "knive"],
     "Words ending in -f or -fe change to -ves: knives.", ["Wrong: 'knifes' is not the standard plural.", "Wrong: 'knifees' is not a word.", "Wrong: 'knive' is not a word."]),
    (7, "The plural of 'sheep' is:", "sheep", ["sheeps", "sheepes", "sheepy"],
     "'Sheep' has the same singular and plural form.", ["Wrong: 'sheeps' is not used.", "Wrong: 'sheepes' is not a word.", "Wrong: 'sheepy' is an adjective."]),
    (7, "The plural of 'city' is:", "cities", ["citys", "citie", "cityes"],
     "A consonant plus -y changes to -ies: cities.", ["Wrong: 'citys' is not correct.", "Wrong: 'citie' is not correct.", "Wrong: 'cityes' is not correct."]),
    (7, "The plural of 'tooth' is:", "teeth", ["tooths", "toothes", "tooth"],
     "'Teeth' is the irregular plural.", ["Wrong: 'tooths' is not correct.", "Wrong: 'toothes' is not correct.", "Wrong: 'tooth' is singular."]),
    (7, "The plural of 'criterion' is:", "criteria", ["criterions", "criterias", "criterioni"],
     "'Criteria' is the Latin-based plural.", ["Wrong: 'criterions' is not standard.", "Wrong: 'criterias' is not correct.", "Wrong: 'criterioni' is not a word."]),
    (7, "The singular of 'mice' is:", "mouse", ["mouses", "mousse", "mic"],
     "'Mouse' is the singular of 'mice'.", ["Wrong: 'mouses' is not the plural form used.", "Wrong: 'mousse' is a dessert.", "Wrong: 'mic' is not a word."]),
    (7, "The plural of 'half' is:", "halves", ["halfs", "halfes", "halve"],
     "Words ending in -f change to -ves: halves.", ["Wrong: 'halfs' is not the standard plural.", "Wrong: 'halfes' is not a word.", "Wrong: 'halve' is a verb."]),
    (7, "The plural of 'wife' is:", "wives", ["wifes", "wifees", "wivens"],
     "Words ending in -fe change to -ves: wives.", ["Wrong: 'wifes' is not the standard plural.", "Wrong: 'wifees' is not a word.", "Wrong: 'wivens' is not a word."]),
    (7, "The plural of 'ox' is:", "oxen", ["oxes", "oxs", "oxies"],
     "'Oxen' is the irregular plural.", ["Wrong: 'oxes' is not the irregular plural.", "Wrong: 'oxs' is not correct.", "Wrong: 'oxies' is not correct."]),
    (8, "The possessive singular of 'boy' is:", "boy's", ["boys'", "boyes'", "boyes"],
     "Add 's to a singular noun.", ["Wrong: 'boys'' is the plural possessive.", "Wrong: 'boyes'' is not correct.", "Wrong: 'boyes' is not a word."]),
    (8, "The possessive plural of 'boys' is:", "boys'", ["boy's", "boys's", "boyes"],
     "Add an apostrophe after a plural ending in -s.", ["Wrong: 'boy's' is singular.", "Wrong: 'boys's' is not correct.", "Wrong: 'boyes' is not a word."]),
    (8, "In 'She gave me a book.', 'me' is in which case?", "objective", ["nominative", "possessive", "vocative"],
     "'Me' receives the action, so it is in the objective case.", ["Wrong: 'me' is not the doer of the action.", "Wrong: 'me' does not show ownership.", "Wrong: 'me' is not used to address someone."]),
    (8, "In 'Ram loves Sita.', 'Ram' is in which case?", "nominative", ["objective", "possessive", "vocative"],
     "'Ram' does the action, so it is the subject, in the nominative case.", ["Wrong: 'Ram' is not the receiver of the action.", "Wrong: 'Ram' does not show ownership.", "Wrong: 'Ram' is not being addressed."]),
    (8, "The vocative case is used:", "for addressing someone", ["to show ownership", "as the subject of a verb", "to receive the action"],
     "The vocative names the person spoken to, as in 'O Lord'.", ["Wrong: showing ownership is the possessive case.", "Wrong: the subject is in the nominative case.", "Wrong: receiving the action is the objective case."]),
    (8, "In 'the girl's bag', which word is in the possessive case?", "girl's", ["bag", "the", "girl"],
     "'Girl's' shows the bag belongs to the girl.", ["Wrong: 'bag' is the thing owned.", "Wrong: 'the' is an article.", "Wrong: 'girl' lacks the possessive ending."]),
    (8, "The subject of a verb is in which case?", "nominative", ["objective", "possessive", "vocative"],
     "The subject is in the nominative case.", ["Wrong: the objective case is for objects.", "Wrong: the possessive shows ownership.", "Wrong: the vocative is for addressing someone."]),
    (8, "The object of a verb is in which case?", "objective", ["nominative", "possessive", "vocative"],
     "The object receives the action and is in the objective case.", ["Wrong: the nominative is the subject's case.", "Wrong: the possessive shows ownership.", "Wrong: the vocative addresses someone."]),
    (8, "In 'O Lord, help us.', 'O Lord' is in which case?", "vocative", ["nominative", "objective", "possessive"],
     "'O Lord' is the person addressed, so it is vocative.", ["Wrong: it is not the subject.", "Wrong: it does not receive the action.", "Wrong: it does not show ownership."]),
    (8, "The possessive plural of 'children' is:", "children's", ["childrens'", "childrens", "children"],
     "'Children' is irregular, so add 's: children's.", ["Wrong: 'childrens'' is not correct.", "Wrong: 'childrens' is not the possessive form.", "Wrong: 'children' has no possessive ending."]),
    (9, "In 'a brave boy', the adjective is:", "brave", ["boy", "a", "boys"],
     "'Brave' describes the boy.", ["Wrong: 'boy' is a noun.", "Wrong: 'a' is an article.", "Wrong: 'boys' is a noun."]),
    (9, "Which group is the articles?", "a, an, the", ["this, that", "my, your", "some, any"],
     "The articles are 'a', 'an' and 'the'.", ["Wrong: 'this' and 'that' are demonstratives.", "Wrong: 'my' and 'your' are possessives.", "Wrong: 'some' and 'any' are quantity adjectives."]),
    (9, "In 'that man is tall', 'that' is a:", "demonstrative adjective", ["possessive adjective", "interrogative adjective", "quantity adjective"],
     "'That' points out a particular man.", ["Wrong: 'that' does not show ownership.", "Wrong: 'that' is not used to ask a question here.", "Wrong: 'that' is not a quantity word."]),
    (9, "In 'her book', 'her' is a:", "possessive adjective", ["subject pronoun", "reflexive pronoun", "object pronoun"],
     "'Her' shows ownership and describes the noun 'book'.", ["Wrong: 'her' does not act as a subject here.", "Wrong: 'her' is not reflexive here.", "Wrong: 'her' is not the object here."]),
    (9, "In 'a wooden leg', the adjective is:", "wooden", ["leg", "a", "fellow"],
     "'Wooden' describes the leg.", ["Wrong: 'leg' is a noun.", "Wrong: 'a' is an article.", "Wrong: 'fellow' is a noun."]),
    (9, "In 'I have some money', 'some' is a:", "quantity adjective", ["verb", "noun", "pronoun"],
     "'Some' tells the amount of money.", ["Wrong: 'some' is not a verb.", "Wrong: 'some' is not a noun.", "Wrong: here 'some' describes the noun, not stands for it."]),
    (9, "In 'The sun is hot', the adjective is:", "hot", ["sun", "is", "the"],
     "'Hot' describes the sun.", ["Wrong: 'sun' is a noun.", "Wrong: 'is' is a verb.", "Wrong: 'the' is an article."]),
    (9, "In 'Which book?', 'which' is a:", "interrogative adjective", ["demonstrative adjective", "relative pronoun", "quantity adjective"],
     "'Which' asks about the noun 'book'.", ["Wrong: 'which' does not point out a thing here.", "Wrong: 'which' is not a relative here.", "Wrong: 'which' is not a quantity word."]),
    (9, "In 'two boys came', 'two' is a:", "definite numeral adjective", ["noun", "verb", "article"],
     "'Two' is a numeral that counts exactly.", ["Wrong: 'two' is not a noun.", "Wrong: 'two' is not a verb.", "Wrong: 'two' is not an article."]),
    (9, "In 'every boy', 'every' is a:", "distributive numeral adjective", ["interrogative adjective", "demonstrative adjective", "quantity adjective"],
     "'Every' refers to each one of a group.", ["Wrong: 'every' does not ask a question.", "Wrong: 'every' does not point out a thing.", "Wrong: 'every' is not about an amount."]),
]


def generated_questions():
    out = []
    for n, (ch, stem, correct, wrong, expl, rs) in enumerate(GEN):
        pos = n % 4
        options = [correct] + wrong
        reasons = [f"Correct: {expl}"] + rs
        out.append({"chapter": ch, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate(options, 0, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, 0, pos)})
    return out
