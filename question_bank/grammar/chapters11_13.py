"""Chapters 11 to 13 (Adjectives used as nouns, Position of adjectives, Correct use of some adjectives).

The book has no grammar exercise for these chapters, so every question here is generated.
Chapter 13's exercises are composition writing tasks and are handled separately.
"""

LETTERS = "ABCD"

GEN = [
    (11, "In 'The poor are often neglected.', the word 'poor' is:", "an adjective used as a noun",
     ["a verb", "an adverb", "a pronoun"],
     "'The poor' refers to people, so an adjective is used as a noun.",
     ["Wrong: 'poor' does not show an action.", "Wrong: 'poor' is not describing a verb.", "Wrong: 'poor' does not replace a noun."]),
    (11, "Which phrase uses an adjective as a noun?", "the wise",
     ["very wise", "wisdom", "wiser"],
     "'The wise' refers to wise people, so it is an adjective used as a noun.",
     ["Wrong: 'very wise' describes something.", "Wrong: 'wisdom' is an abstract noun.", "Wrong: 'wiser' is a comparative adjective."]),
    (11, "In 'We pray for the dead.', 'the dead' is:", "an adjective used as a noun",
     ["a verb", "an adverb", "a preposition"],
     "'The dead' means dead people, used as a noun.",
     ["Wrong: it is not a verb.", "Wrong: it does not modify a verb.", "Wrong: 'for' is the preposition, not 'the dead'."]),
    (11, "In 'Care for the sick.', the word 'sick' functions as:", "a noun",
     ["an adverb", "a verb", "a pronoun"],
     "'The sick' means sick people, so it works as a noun.",
     ["Wrong: it does not modify a verb.", "Wrong: it is not an action word.", "Wrong: it does not replace a noun."]),
    (11, "In 'The brave deserve praise.', 'brave' is used as:", "a noun",
     ["a verb", "an adverb", "a preposition"],
     "'The brave' refers to brave people, so it is used as a noun.",
     ["Wrong: it is not an action word.", "Wrong: it does not modify a verb.", "Wrong: 'the' and 'brave' do not form a preposition."]),
    (12, "Adjectives used before the noun they describe are called:", "attributive adjectives",
     ["predicative adjectives", "possessive adjectives", "numeral adjectives"],
     "A 'brave boy' uses an attributive adjective, placed before the noun.",
     ["Correct: they come before the noun.", "Wrong: predicative adjectives follow a linking verb.", "Wrong: possessive adjectives show ownership.", "Wrong: numeral adjectives show number."]),
    (12, "Which sentence uses 'brave' as a predicative adjective?", "The boy is brave.",
     ["a brave boy", "the brave man", "brave is a word"],
     "In 'The boy is brave', 'brave' comes after the linking verb 'is' and describes the subject.",
     ["Correct: the adjective follows the verb 'is'.", "Wrong: here 'brave' comes before the noun.", "Wrong: here 'brave' comes before the noun.", "Wrong: this does not use 'brave' to describe a noun."]),
    (12, "Adjectives after 'something', 'nothing' and 'anything' come:", "after the word",
     ["before the word", "never", "between subject and verb"],
     "In 'something new', the adjective follows the word it describes.",
     ["Correct: they follow the word they describe.", "Wrong: they come after, not before.", "Wrong: they can come after.", "Wrong: they do not sit between subject and verb."]),
    (12, "In 'the Lord Almighty', the adjective 'Almighty' comes:", "after the noun",
     ["before the noun", "at the start of the sentence", "nowhere"],
     "Some adjectives follow the noun, as in 'the Lord Almighty'.",
     ["Correct: it follows the noun.", "Wrong: it does not come before the noun here.", "Wrong: it does not start the sentence.", "Wrong: it does appear in the phrase."]),
    (12, "Which is an attributive adjective?", "brave in 'a brave boy'",
     ["brave in 'The boy is brave'", "brave as a noun", "brave as a verb"],
     "'Brave' is placed before the noun 'boy', so it is attributive.",
     ["Correct: it comes before the noun 'boy'.", "Wrong: here it follows 'is', so it is predicative.", "Wrong: here it is not a noun.", "Wrong: here it is not a verb."]),
    (13, "Use 'fewer' with:", "countable nouns",
     ["uncountable nouns", "both kinds of noun", "neither kind of noun"],
     "'Fewer' is used with countable nouns, such as 'fewer books'.",
     ["Correct: 'fewer' goes with countable nouns.", "Wrong: uncountable nouns take 'less'.", "Wrong: 'fewer' does not go with uncountable nouns.", "Wrong: 'fewer' does go with countable nouns."]),
    (13, "Use 'less' with:", "uncountable nouns",
     ["countable nouns", "plural nouns", "people"],
     "'Less' is used with uncountable nouns, such as 'less water'.",
     ["Correct: 'less' goes with uncountable nouns.", "Wrong: countable nouns take 'fewer'.", "Wrong: plural nouns take 'fewer'.", "Wrong: people are countable, so 'fewer' is used."]),
    (13, "'Elder' is used of:", "persons only",
     ["animals and things", "places", "time"],
     "'Elder' and 'eldest' are used only of persons, as in 'my elder brother'.",
     ["Correct: 'elder' is used of persons only.", "Wrong: 'older' is used for animals and things.", "Wrong: 'elder' is not used for places.", "Wrong: 'latest' refers to time."]),
    (13, "'Latter' refers to:", "the second of two",
     ["the last of many", "the first of many", "all of them"],
     "'Latter' means the second of two things.",
     ["Correct: 'latter' means the second of two.", "Wrong: 'last' is used for the final one of many.", "Wrong: 'first' is not what 'latter' means.", "Wrong: 'all' is not what 'latter' means."]),
    (13, "'Further' means:", "additional",
     ["nearest in distance", "first", "farther only in distance"],
     "'Further' means 'additional', as in 'further delay'.",
     ["Correct: 'further' means additional.", "Wrong: 'nearest' is a different word.", "Wrong: 'first' is not the meaning.", "Wrong: 'farther' is used for distance, but 'further' can mean additional."]),
    (13, "'Latest' refers to:", "time",
     ["position in a series", "distance", "quantity"],
     "'Latest' refers to time, as in 'the latest news'.",
     ["Correct: 'latest' refers to time.", "Wrong: 'last' or 'next' refers to position.", "Wrong: 'farther' refers to distance.", "Wrong: 'more' refers to quantity."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def generated_questions():
    out = []
    for n, (ch, stem, correct, wrong, expl, reasons) in enumerate(GEN):
        if len(reasons) == 3:  # the correct reason was left out; it is the explanation
            reasons = [f"Correct: {expl}"] + reasons
        pos = n % 4
        options = [correct] + wrong
        out.append({"chapter": ch, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
