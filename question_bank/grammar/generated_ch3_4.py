"""Generated questions for Chapter 3 (Phrase and Clause) and Chapter 4 (Parts of Speech).

Each entry: (chapter, stem, [correct, wrong, wrong, wrong], explanation, reasons for the correct
option first then the three wrong options). Correct letters are rotated when the file is built.
"""

LETTERS = "ABCD"

ITEMS = [
    (3, "In \"The sun rises in the east.\", the group 'in the east' is a:",
     ["phrase", "clause", "sentence", "word"],
     "'In the east' makes sense but not complete sense, so it is a phrase.",
     ["Correct: it makes sense but not complete sense.", "Wrong: a clause has its own subject and predicate.",
      "Wrong: a sentence makes complete sense.", "Wrong: it is more than one word."]),
    (3, "Which group of words is a clause?",
     ["of great beauty", "which is made of gold", "on a wall", "the tops of the mountains"],
     "A clause has a subject and a predicate. 'Which is made of gold' has both.",
     ["Correct: it contains a subject (which) and a predicate (is made of gold).", "Wrong: this is a phrase with no subject and predicate.",
      "Wrong: this is a phrase.", "Wrong: this is a phrase."]),
    (3, "A phrase is a group of words that:",
     ["makes complete sense", "has a subject and a predicate", "makes sense but not complete sense", "is one word"],
     "A phrase makes sense but not complete sense.",
     ["Correct: a phrase makes sense but not complete sense.", "Wrong: that describes a clause.",
      "Wrong: that describes a sentence.", "Wrong: a phrase has more than one word."]),
    (3, "A clause differs from a phrase because a clause:",
     ["has no verb", "contains a subject and a predicate", "is always a question", "is a single word"],
     "A clause has a subject and a predicate; a phrase does not.",
     ["Wrong: a clause has a verb in its predicate.", "Correct: a clause has its own subject and predicate.",
      "Wrong: clauses can be statements, questions or other kinds.", "Wrong: a clause has several words."]),
    (3, "In \"I think that you have made a mistake.\", the group 'that you have made a mistake' is a:",
     ["phrase", "clause", "word", "question"],
     "It has a subject ('you') and a predicate ('have made a mistake'), so it is a clause.",
     ["Wrong: a phrase has no subject and predicate.", "Correct: it has a subject and a predicate.",
      "Wrong: it is more than one word.", "Wrong: it is a group of words that is not a question."]),
    (3, "In \"He has a chain of gold.\", the group 'of gold' is a:",
     ["phrase", "clause", "sentence", "subject"],
     "'Of gold' makes sense but has no subject and predicate, so it is a phrase.",
     ["Correct: it makes sense but not complete sense.", "Wrong: it has no subject and predicate.",
      "Wrong: it is part of a sentence, not a whole sentence.", "Wrong: a subject is a noun or noun phrase, not this group."]),
    (3, "The phrase 'in a corner' makes:",
     ["complete sense", "sense but not complete sense", "no sense at all", "a full sentence"],
     "Phrases make sense but not complete sense.",
     ["Wrong: a sentence makes complete sense; a phrase does not.", "Correct: a phrase makes sense but not complete sense.",
      "Wrong: the phrase does make sense.", "Wrong: it is not a sentence."]),
    (3, "Which group of words contains a subject and a predicate?",
     ["of great beauty", "the tops of the mountains", "while it is raining", "a sunset"],
     "'While it is raining' has a subject (it) and a predicate (is raining).",
     ["Wrong: this is a phrase.", "Wrong: this is a phrase.",
      "Correct: it has a subject (it) and a predicate (is raining).", "Wrong: a single noun is not a clause."]),
    (4, "How many parts of speech are there in English, according to this book?",
     ["six", "eight", "ten", "twelve"],
     "The book lists eight parts of speech.",
     ["Correct: the book lists eight parts of speech.", "Wrong: there are eight, not six.",
      "Wrong: there are eight, not ten.", "Wrong: there are eight, not twelve."]),
    (4, "A noun is a word used as:",
     ["the name of a person, place, or thing", "an action", "a joining word", "a feeling"],
     "A noun names a person, place or thing.",
     ["Correct: a noun is the name of a person, place or thing.", "Wrong: an action is a verb.",
      "Wrong: a joining word is a conjunction.", "Wrong: a feeling is shown by an interjection."]),
    (4, "An adjective is a word that:",
     ["adds something to the meaning of a noun", "takes the place of a noun", "joins words or sentences", "expresses a sudden feeling"],
     "An adjective adds to the meaning of a noun, as in 'a brave boy'.",
     ["Correct: an adjective adds to the meaning of a noun.", "Wrong: that describes a pronoun.",
      "Wrong: that describes a conjunction.", "Wrong: that describes an interjection."]),
    (4, "A pronoun is a word used:",
     ["instead of a noun", "to show time", "to join words", "to express a feeling"],
     "A pronoun takes the place of a noun, as in 'John is absent, because he is ill.'",
     ["Correct: a pronoun is used instead of a noun.", "Wrong: showing time is done by adverbs or tenses.",
      "Wrong: joining words is the job of a conjunction.", "Wrong: expressing feeling is the job of an interjection."]),
    (4, "In \"He worked the sum quickly.\", the word 'quickly' is a:",
     ["noun", "verb", "adverb", "adjective"],
     "'Quickly' adds to the meaning of the verb 'worked', so it is an adverb.",
     ["Wrong: a noun names a person, place or thing.", "Wrong: 'worked' is the verb.",
      "Correct: it adds to the meaning of a verb.", "Wrong: an adjective adds to a noun, not a verb."]),
    (4, "A preposition is a word that:",
     ["shows how a noun or pronoun stands in relation to something else", "expresses a sudden feeling", "joins two sentences", "names a person"],
     "In 'There is a cow in the garden', 'in' shows the relation of the cow to the garden.",
     ["Correct: it shows relation between a noun or pronoun and something else.", "Wrong: that describes an interjection.",
      "Wrong: that describes a conjunction.", "Wrong: that describes a noun."]),
    (4, "In \"Rama and Hari are cousins.\", the word 'and' is a:",
     ["preposition", "conjunction", "adverb", "interjection"],
     "A conjunction joins words or sentences; 'and' joins 'Rama' and 'Hari'.",
     ["Wrong: a preposition shows relation to a noun.", "Correct: it joins two words.",
      "Wrong: an adverb adds to a verb, adjective or adverb.", "Wrong: an interjection expresses sudden feeling."]),
    (4, "Which sentence contains an interjection?",
     ["Two and two make four.", "Hurrah! We have won the game.", "Rama and Hari are cousins.", "She pronounced the word quite correctly."],
     "'Hurrah!' expresses a sudden feeling, so it is an interjection.",
     ["Wrong: 'and' is a conjunction.", "Correct: 'Hurrah!' expresses a sudden feeling.",
      "Wrong: 'and' is a conjunction.", "Wrong: 'quite' is an adverb."]),
    (4, "In \"They arrived after us.\", the word 'after' is a:",
     ["adverb", "preposition", "conjunction", "pronoun"],
     "'After' shows the relation between 'us' and the arriving. The book gives this as a preposition.",
     ["Wrong: here 'after' is not used alone to add to a verb.", "Correct: 'after' is used with the pronoun 'us' to show relation.",
      "Wrong: a conjunction joins two clauses; 'after us' does not.", "Wrong: 'after' is not a pronoun."]),
    (4, "Which of these is an article?",
     ["the", "this", "my", "some"],
     "The articles are 'a', 'an' and 'the'.",
     ["Correct: 'the' is an article.", "Wrong: 'this' is a determiner classed as an adjective here.",
      "Wrong: 'my' is a determiner classed as an adjective here.", "Wrong: 'some' is a determiner classed as an adjective here."]),
]


def questions():
    out = []
    for n, (ch, stem, options, expl, reasons) in enumerate(ITEMS):
        pos = n % 4
        rest = options[1:]
        opts = rest[:pos] + [options[0]] + rest[pos:]
        rs = reasons[1:]
        reasons_out = rs[:pos] + [reasons[0]] + rs[pos:]
        out.append({"chapter": ch, "source": "Generated", "exercise": "", "stem": stem,
                    "options": opts, "correct": LETTERS[pos], "explanation": expl, "reasons": reasons_out})
    return out
