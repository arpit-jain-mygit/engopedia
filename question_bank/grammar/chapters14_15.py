"""Chapter 14 (Articles, generated only) and Chapter 15 (Personal Pronouns: Exercise in Grammar 25 plus generated).

Exercise in Grammar 25 answers come from the key on page 12 (items 1-17). Exercise 25's
distractors are other antecedents from the same exercise.
"""

LETTERS = "ABCD"

# (item, sentence, pronoun, what it stands for) from the answer key.
EX25 = [
    (1, "Alice was not a bit hurt, and she jumped up on to her feet in a moment.", "she", "Alice"),
    (2, "There were doors all round the hall, but they were all locked.", "they", "doors"),
    (3, "Alice opened the door and found that it led into a small passage.", "it", "door"),
    (4, "“I wish I hadn’t cried so much,” said Alice.", "I", "Alice"),
    (5, "“You are not attending”, said the Mouse to Alice severely.", "You", "Alice"),
    (6, "“Come back!” the Caterpillar called after her.", "her", "Alice"),
    (7, "Hari brought his book and laid it on the table.", "his", "Hari"),
    (8, "Karim has lost his dog and cannot find it.", "his", "Karim"),
    (9, "Suresh is at the head of his class, for he studies hard.", "his", "Suresh"),
    (10, "Rama, you are a lazy boy.", "you", "Rama"),
    (11, "The camel is a beast of burden. It is used to carry goods across the desert.", "It", "camel"),
    (12, "The female lion is called a lioness. She has no mane.", "She", "lioness"),
    (13, "The horse fell down and broke its leg.", "its", "horse"),
    (14, "Birds build their nests in trees.", "their", "birds"),
    (15, "If the thief is caught, he will be punished.", "he", "thief"),
    (16, "Train up a child in the way he should go.", "he", "child"),
    (17, "And Nathan said to David, Thou art the man.", "Thou", "David"),
]
ANTECEDENTS = ["Alice", "doors", "door", "Hari", "Karim", "Suresh", "Rama", "camel", "lioness", "horse", "birds", "thief", "child", "David", "book", "dog"]

GEN14 = [
    ("The article 'a' is used before words that begin with:", "a consonant sound",
     ["a vowel sound", "a plural noun", "a proper noun"],
     "'A' is used before a consonant sound, as in 'a boy'.",
     ["Wrong: 'an' is used before a vowel sound.", "Wrong: plural nouns take no article here.", "Wrong: proper nouns usually take no article."]),
    ("Which article is correct before 'hour'?", "an",
     ["a", "the", "no article"],
     "'Hour' starts with a silent 'h', so it has a vowel sound: 'an hour'.",
     ["Wrong: 'a' is used before a consonant sound.", "Wrong: 'the' is used for a particular thing.", "Wrong: an article is needed here."]),
    ("In 'The sun rises in the east.', 'the' is used because:", "the thing is unique",
     ["the thing is plural", "the thing is a proper noun", "the thing is uncountable"],
     "'The sun' and 'the east' refer to things that are unique in our experience.",
     ["Wrong: 'sun' is singular.", "Wrong: 'sun' is a common noun here.", "Wrong: 'sun' is countable."]),
    ("'A', 'an' and 'the' are together called:", "articles",
     ["pronouns", "verbs", "adverbs"],
     "Articles are the words 'a', 'an' and 'the'.",
     ["Wrong: pronouns stand in for nouns.", "Wrong: verbs express action or state.", "Wrong: adverbs modify verbs, adjectives or adverbs."]),
    ("In 'He is an honest man.', 'an' is used because:", "'honest' begins with a vowel sound",
     ["'honest' begins with a consonant sound", "'honest' is plural", "'honest' is a proper noun"],
     "The 'h' in 'honest' is silent, so the word starts with a vowel sound.",
     ["Wrong: 'honest' does not start with a consonant sound.", "Wrong: 'honest' is an adjective here, not a plural noun.", "Wrong: 'honest' is not a proper noun."]),
]

GEN15 = [
    ("The first person singular pronoun is:", "I", ["we", "you", "they"],
     "'I' is the first person singular pronoun.", ["Wrong: 'we' is first person plural.", "Wrong: 'you' is second person.", "Wrong: 'they' is third person plural."]),
    ("The objective case of 'she' is:", "her", ["hers", "she", "herself"],
     "'Her' is the objective form of 'she'.", ["Wrong: 'hers' is possessive.", "Wrong: 'she' is nominative.", "Wrong: 'herself' is reflexive."]),
    ("The possessive form of 'we' used before a noun is:", "our", ["ours", "us", "ourselves"],
     "'Our' is the possessive adjective form used before a noun.", ["Wrong: 'ours' stands alone without a noun.", "Wrong: 'us' is objective.", "Wrong: 'ourselves' is reflexive."]),
    ("Which pronoun is in the nominative case?", "he", ["him", "his", "himself"],
     "'He' is the nominative (subject) form.", ["Wrong: 'him' is objective.", "Wrong: 'his' is possessive.", "Wrong: 'himself' is reflexive."]),
    ("Which pronoun is used for animals and things?", "it", ["he", "she", "they"],
     "'It' is used for animals and things.", ["Wrong: 'he' is used for males.", "Wrong: 'she' is used for females.", "Wrong: 'they' is used for more than one."]),
    ("The objective form of 'they' is:", "them", ["their", "theirs", "they"],
     "'Them' is the objective form.", ["Wrong: 'their' is possessive before a noun.", "Wrong: 'theirs' is possessive alone.", "Wrong: 'they' is nominative."]),
    ("The possessive form of 'I' used after a verb is:", "mine", ["my", "me", "myself"],
     "'Mine' is possessive and stands alone, as in 'The book is mine.'", ["Wrong: 'my' is used before a noun.", "Wrong: 'me' is objective.", "Wrong: 'myself' is reflexive."]),
    ("The possessive of 'you' used before a noun is:", "your", ["yours", "you", "yourself"],
     "'Your' is the possessive adjective form before a noun.", ["Wrong: 'yours' stands alone.", "Wrong: 'you' is not possessive.", "Wrong: 'yourself' is reflexive."]),
    ("In 'Tell him the news.', 'him' is in the:", "objective case", ["nominative case", "possessive case", "vocative case"],
     "'Him' receives the action of telling, so it is objective.", ["Wrong: the subject would be nominative.", "Wrong: 'him' does not show ownership.", "Wrong: 'him' is not addressed."]),
    ("Which pronoun is in the possessive case?", "hers", ["her", "she", "herself"],
     "'Hers' shows ownership and stands alone.", ["Wrong: 'her' is objective.", "Wrong: 'she' is nominative.", "Wrong: 'herself' is reflexive."]),
]

LETTERS_ORDER = LETTERS


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def ex25_questions():
    out = []
    for n, (item, sentence, pron, ant) in enumerate(EX25):
        pos = n % 4
        distract = [a for a in ANTECEDENTS if a != ant][n % 5: n % 5 + 3]
        options = [ant] + distract
        reasons = [f"Correct: '{pron}' stands for '{ant}'."] + \
                  [f"Wrong: '{pron}' does not stand for '{d}' here." for d in distract]
        out.append({"source": "Book", "exercise": f"Exercise in Grammar 25, item {item}",
                    "stem": f'In "{sentence}", what does "{pron}" stand for?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{pron}' stands for '{ant}'.", "reasons": _rotate(reasons, pos)})
    return out


def generated_questions(chapter):
    data = GEN14 if chapter == 14 else GEN15
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(data):
        pos = n % 4
        out.append({"chapter": chapter, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate([f"Correct: {expl}"] + reasons, pos)})
    return out
