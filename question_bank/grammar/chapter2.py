"""Chapter 2 (Subject and Predicate): generated questions plus Exercise in Grammar 1 (book items 1-27).

Book items: the sentence and its subject/predicate come from the printed exercise; the subject and
predicate pairs come from the answer key. Distractors are the sentence's own predicate and subjects
from other sentences in the same exercise.
"""

EX1_SENTENCES = [
    ("The cackling of geese saved Rome.", "The cackling of geese", "saved Rome"),
    ("The boy stood on the burning deck.", "The boy", "stood on the burning deck"),
    ("Tubal Cain was a man of might.", "Tubal Cain", "was a man of might"),
    ("Stone walls do not make a prison.", "Stone walls", "do not make a prison"),
    ("The singing of the birds delights us.", "The singing of the birds", "delights us"),
    ("Miss Kitty was rude at the table one day.", "Miss Kitty", "was rude at the table one day"),
    ("He has a good memory.", "He", "has a good memory"),
    ("Bad habits grow unconsciously.", "Bad habits", "grow unconsciously"),
    ("The earth revolves round the sun.", "The earth", "revolves round the sun"),
    ("Nature is the best physician.", "Nature", "is the best physician"),
    ("Edison invented the phonograph.", "Edison", "invented the phonograph"),
    ("The sea hath many thousand sands.", "The sea", "hath many thousand sands"),
    ("We cannot pump the ocean dry.", "We", "cannot pump the ocean dry"),
    ("Borrowed garments never fit well.", "Borrowed garments", "never fit well"),
    ("The early bird catches the worm.", "The early bird", "catches the worm"),
    ("All matter is indestructible.", "All matter", "is indestructible"),
    ("Islamabad is the capital of Pakistan.", "Islamabad", "is the capital of Pakistan"),
    ("We should profit by experience.", "We", "should profit by experience"),
    ("All roads lead to Rome.", "All roads", "lead to Rome"),
    ("A guilty conscience needs no excuse.", "A guilty conscience", "needs no excuse"),
    ("The beautiful rainbow soon faded away.", "The beautiful rainbow", "soon faded away"),
    ("No man can serve two masters.", "No man", "can serve two masters"),
    ("A sick room should be well aired.", "A sick room", "should be well aired"),
    ("The dewdrops glitter in the sunshine.", "The dewdrops", "glitter in the sunshine"),
    ("I shot an arrow into the air.", "I", "shot an arrow into the air"),
    ("A barking sound the shepherd hears.", "The shepherd", "hears a barking sound"),
    ("On the top of the hill lives a hermit.", "A hermit", "lives on the top of the hill"),
]

GENERATED = [
    ("Every sentence has two parts. They are:", ["subject and predicate", "noun and verb", "phrase and clause", "subject and object"], "A",
     "The subject names the person or thing spoken about; the predicate says something about it.",
     ["Correct: these are the two parts of every sentence.", "Wrong: nouns and verbs are word classes, not sentence parts.",
      "Wrong: a phrase and a clause are word groups, not the two basic parts.", "Wrong: an object is part of the predicate, not a separate main part."]),
    ("The part of a sentence that names the person or thing spoken about is called the:", ["predicate", "subject", "object", "phrase"], "B",
     "This part is the subject.", ["Wrong: the predicate tells something about the subject.",
      "Correct: the subject names the person or thing.", "Wrong: an object receives the action, it does not name the topic.", "Wrong: a phrase is a group of words without a subject and predicate."]),
    ("In \"Sit down.\", the subject is left out. The understood subject is:", ["I", "You", "He", "They"], "B",
     "In imperative sentences the subject 'You' is understood.", ["Wrong: the command is addressed to the listener, not the speaker.",
      "Correct: 'You' is understood in commands.", "Wrong: 'He' names a third person not spoken to.", "Wrong: 'They' names more than one third person."]),
    ("Which sentence has its subject after the predicate?", ["The boy ran home.", "Sweet are the uses of adversity.", "Birds sing.", "Rain falls."], "B",
     "In 'Sweet are the uses of adversity', the subject 'the uses of adversity' comes after 'Sweet are'.",
     ["Wrong: the subject comes first.", "Correct: the subject comes after the predicate here.", "Wrong: the subject comes first.", "Wrong: the subject comes first."]),
    ("In \"Here comes the bus.\", the subject is:", ["Here", "comes", "the bus", "Here comes"], "C",
     "'The bus' is the thing spoken about, so it is the subject.", ["Wrong: 'Here' is an adverb.", "Wrong: 'comes' is part of the predicate.",
      "Correct: 'the bus' names what we are talking about.", "Wrong: 'Here comes' is the predicate."]),
    ("In \"Humpty Dumpty sat on a wall.\", the predicate is:", ["Humpty Dumpty", "sat on a wall", "Dumpty", "on a wall"], "B",
     "The predicate tells what Humpty Dumpty did.", ["Wrong: this names the subject.", "Correct: 'sat on a wall' tells something about the subject.",
      "Wrong: 'Dumpty' is part of the subject name.", "Wrong: 'on a wall' is only part of the predicate."]),
    ("In \"The sun rises in the east.\", the predicate is:", ["The sun", "rises in the east", "in the east", "The sun rises"], "B",
     "The predicate is everything that says something about 'the sun'.", ["Wrong: 'The sun' is the subject.", "Correct: it tells what the sun does.",
      "Wrong: this is only part of the predicate.", "Wrong: 'The sun' is the subject, not part of the predicate."]),
    ("In \"Mohan is an industrious boy.\", the subject is:", ["is an industrious boy", "Mohan", "industrious boy", "an industrious"], "B",
     "'Mohan' is the person spoken about.", ["Wrong: this is the predicate.", "Correct: 'Mohan' names the person.",
      "Wrong: this is part of the predicate.", "Wrong: this is part of the predicate."]),
    ("In \"Birds sing sweetly in spring.\", the predicate is:", ["Birds", "sing sweetly in spring", "sing", "spring"], "B",
     "The predicate is 'sing sweetly in spring'.", ["Wrong: 'Birds' is the subject.", "Correct: it tells what birds do.",
      "Wrong: 'sing' is only the verb, not the whole predicate.", "Wrong: 'spring' is only part of the predicate."]),
    ("In \"Gold glitters.\", the subject is:", ["glitters", "Gold", "Gold glitters", "gold"], "B",
     "'Gold' names what we are talking about.", ["Wrong: 'glitters' is the predicate.", "Correct: 'Gold' names the thing spoken about.",
      "Wrong: this is the whole sentence.", "Wrong: this is the same word, written in lower case; the subject is 'Gold'."]),
]

LETTERS = "ABCD"


def book_questions():
    """Exercise in Grammar 1, items 1-27: 'What is the subject?' with four options."""
    out = []
    for n, (sentence, subject, predicate) in enumerate(EX1_SENTENCES, start=1):
        # Distractors: the sentence's own predicate, plus subjects from two other sentences.
        others = [EX1_SENTENCES[(n - 1 + k) % len(EX1_SENTENCES)][1] for k in (3, 7)]
        options = [subject, predicate, others[0], others[1]]
        # Rotate the correct letter so answers are not always the same.
        pos = (n - 1) % 4
        rest = [o for o in options if o != subject]
        opts = rest[:pos] + [subject] + rest[pos:]
        reasons = []
        for o in opts:
            if o == subject:
                reasons.append("Correct: it names the person or thing spoken about (the subject).")
            elif o == predicate:
                reasons.append("Wrong: this tells something about the subject (the predicate).")
            else:
                reasons.append("Wrong: this is the subject of a different sentence in this exercise.")
        out.append({
            "source": "Book", "exercise": f"Exercise in Grammar 1, item {n}",
            "stem": f'In the sentence "{sentence}", which part is the SUBJECT?',
            "options": opts, "correct": LETTERS[pos],
            "explanation": f'Subject: {subject}. Predicate: {predicate}.',
            "reasons": reasons,
        })
    return out


def generated_questions():
    return [{"source": "Generated", "exercise": "", "stem": stem, "options": opts,
             "correct": LETTERS[LETTERS.index(c)], "explanation": expl, "reasons": reasons}
            for stem, opts, c, expl, reasons in GENERATED]
