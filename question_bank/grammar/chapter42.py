"""Chapter 42 (The Interjection): no printed grammar exercise in the book, so this chapter has generated
questions only. Based on sections 418-419 (examples: Hello, Alas, Hurrah, Ah, Oh, Hush, Ah me, For shame).
"""

LETTERS = "ABCD"

GEN = [
    ("In 'Alas! He is dead.', the word 'Alas' expresses:", "grief", ["approval", "joy", "surprise"],
     "'Alas' expresses grief, as in the book's example.",
     ["Correct: 'alas' expresses grief.", "Wrong: approval is shown by words like 'bravo'.", "Wrong: joy is shown by words like 'hurrah'.", "Wrong: surprise is shown by words like 'ha'."]),
    ("In 'Hurrah! We have won the game.', the word 'Hurrah' expresses:", "joy", ["grief", "approval", "fear"],
     "'Hurrah' expresses joy or triumph.",
     ["Correct: 'hurrah' expresses joy.", "Wrong: 'alas' is the grief word.", "Wrong: 'bravo' is the approval word.", "Wrong: fear is not one of the book's listed emotions here."]),
    ("'Bravo!' used to praise a performance expresses:", "approval", ["grief", "joy", "surprise"],
     "'Bravo' shows approval, as listed in the book.",
     ["Correct: 'bravo' shows approval.", "Wrong: grief is shown by 'alas'.", "Wrong: joy is shown by 'hurrah'.", "Wrong: surprise is shown by 'ha'."]),
    ("In 'Hush! Don't make a noise.', the word 'Hush' is:", "an interjection", ["a conjunction", "a preposition", "an adverb"],
     "'Hush' expresses a sudden command or feeling and is grammatically unrelated to the rest of the sentence.",
     ["Correct: it is an interjection.", "Wrong: a conjunction joins words or clauses.", "Wrong: a preposition is followed by a noun.", "Wrong: an adverb modifies a verb or adjective."]),
    ("'Ah me!' is an example of:", "a group of words used as an interjection", ["a single-word adverb", "a preposition phrase", "a noun clause"],
     "Section 419 notes that groups of words such as 'Ah me!' also act as interjections.",
     ["Correct: a group of words can act as an interjection.", "Wrong: it is not a single adverb.", "Wrong: it has no noun or preposition.", "Wrong: it is not a clause."]),
    ("'For shame!' is an example of:", "a group of words used as an interjection", ["a noun clause", "an adverb phrase", "a relative pronoun"],
     "'For shame!' expresses a sudden feeling, so it is an interjection.",
     ["Correct: it expresses a sudden feeling.", "Wrong: it has no subject and verb, so it is not a clause.", "Wrong: it does not modify a verb.", "Wrong: it does not refer back to a noun."]),
    ("Which word is an interjection?", "Oh!", ["Oh, dear, I forgot that.", "Oh, the tea is hot now.", "Oh-oh, the sea is calm."],
     "Only 'Oh!' stands alone to express a sudden feeling; the others are sentences or phrases with other parts.",
     ["Correct: it stands alone as a burst of feeling.", "Wrong: this is a full sentence, not an interjection alone.", "Wrong: this is a sentence, not just an interjection.", "Wrong: this is a sentence with a verb."]),
    ("An interjection is best defined as:", "a word that expresses a sudden feeling or emotion", ["a word that joins two clauses", "a word that names a person or thing", "a word that describes a noun"],
     "Section 418 defines an interjection as a word that expresses a sudden feeling or emotion.",
     ["Correct: this is the book's definition.", "Wrong: that describes a conjunction.", "Wrong: that describes a noun.", "Wrong: that describes an adjective."]),
    ("'Good gracious!' is an example of:", "a group of words used as an interjection", ["a finite verb", "a noun phrase", "a conditional clause"],
     "Section 419 lists 'Good gracious!' among groups of words that act as interjections.",
     ["Correct: it is a group of words used as an interjection.", "Wrong: it has no finite verb.", "Wrong: it does not name a thing.", "Wrong: it is not a clause with 'if'."]),
    ("In 'Hello! What are you doing there?', the word 'Hello' is:", "an interjection", ["a noun", "an adverb", "a verb"],
     "'Hello' is a greeting that expresses a sudden feeling, used as an interjection.",
     ["Correct: it is a greeting used as an interjection.", "Wrong: it does not name a person or thing.", "Wrong: it does not describe an action or manner.", "Wrong: it is not a verb in this sentence."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 42, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
