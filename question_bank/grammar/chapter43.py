"""Chapter 43 (The Same Word Used as Different Parts of Speech): questions built from the book's word-list
examples (sections 420 onward). The book has no answer key for this list; each answer is the part of speech
the book gives for that example. Exercise in Composition 102 is not included here.
"""

LETTERS = "ABCD"
POS = ["Adjective", "Adverb", "Noun", "Verb", "Pronoun", "Preposition", "Conjunction", "Interjection"]

# (word, part of speech, example sentence) from the book's word list.
ENTRIES = [
    ("Even", "Adjective", "The chances are even."),
    ("Even", "Verb", "Let us even the ground."),
    ("Even", "Adverb", "Does he even suspect the danger?"),
    ("Except", "Preposition", "All the brethren were in Egypt except Benjamin."),
    ("Except", "Conjunction", "I will not let thee go except thou bless me."),
    ("For", "Preposition", "I can shift for myself."),
    ("For", "Conjunction", "Give thanks unto the Lord; for He is good."),
    ("Less", "Adjective", "You are paying less attention to your studies than you used to do."),
    ("Less", "Adverb", "The population of India is less than that of China."),
    ("Less", "Noun", "He won't be satisfied with less."),
    ("Like", "Adjective", "They are men of like build and stature."),
    ("Like", "Preposition", "Do not talk like that."),
    ("Like", "Verb", "Children like sweets."),
    ("Like", "Noun", "We shall not see his like again."),
    ("Little", "Adjective", "There is little danger in going there."),
    ("Little", "Noun", "Man wants but little here below."),
    ("Little", "Adverb", "He eats very little."),
    ("More", "Adjective", "We want more men like him."),
    ("More", "Pronoun", "More of us die in bed than out of it."),
    ("More", "Adverb", "You should talk less and work more."),
    ("Much", "Adjective", "There is much sense in what he says."),
    ("Much", "Pronoun", "Much of it is true."),
    ("Much", "Adverb", "He boasts too much."),
    ("Near", "Adverb", "Draw near and listen."),
    ("Near", "Preposition", "His house is near the temple."),
    ("Near", "Adjective", "He is a near relation."),
    ("Near", "Verb", "The time nears."),
    ("Needs", "Noun", "My needs are few."),
    ("Needs", "Verb", "It needs to be done with care."),
    ("Needs", "Adverb", "He needs must come."),
    ("Neither", "Conjunction", "Give me neither poverty nor riches."),
    ("Neither", "Adjective", "Neither accusation is true."),
    ("Neither", "Pronoun", "It is difficult to negotiate where neither will trust."),
    ("Next", "Adjective", "I shall see you next Monday."),
    ("Next", "Adverb", "What next?"),
    ("Next", "Preposition", "He was sitting next to her."),
    ("Next", "Noun", "I shall tell you more about it in my next."),
    ("No", "Adjective", "It is no joke."),
    ("No", "Adverb", "He is no more."),
    ("No", "Noun", "I will not take a no."),
    ("Once", "Adverb", "I was young once."),
    ("Once", "Conjunction", "Once he hesitates we have him."),
    ("Once", "Noun", "Please help me for once."),
    ("One", "Adjective", "One day I met him in the street."),
    ("One", "Noun", "One would think he was mad."),
    ("Only", "Adjective", "It was his only chance."),
    ("Only", "Adverb", "He was only foolish."),
    ("Only", "Conjunction", "Take what I have, only let me go."),
    ("Over", "Adverb", "Read it over carefully."),
    ("Over", "Noun", "In one over he took three wickets."),
    ("Over", "Preposition", "At thirty a change came over him."),
    ("Right", "Verb", "That is a fault that will right itself."),
    ("Right", "Adjective", "He is the right man for the position."),
    ("Right", "Noun", "I ask it as a right."),
    ("Right", "Adverb", "He stood right in my way."),
    ("Round", "Adjective", "A square peg in a round hole."),
    ("Round", "Noun", "The evening was a round of pleasures."),
    ("Round", "Adverb", "He came round to their belief."),
    ("Round", "Preposition", "The earth revolves round the sun."),
    ("Round", "Verb", "We shall round the cape in safety."),
    ("Since", "Preposition", "Since that day I have not seen him."),
    ("Since", "Conjunction", "Since there is no help, come, let us kiss and part."),
    ("Since", "Adverb", "I have not seen him since."),
    ("So", "Adverb", "I am so sorry."),
    ("So", "Conjunction", "He was poor, so they helped him."),
    ("Some", "Pronoun", "Some say one thing and others another."),
    ("Some", "Adjective", "We must find some way out of it."),
    ("Some", "Adverb", "Some thirty chiefs were present."),
    ("Still", "Adjective", "Still waters run deep."),
    ("Still", "Noun", "Her sobs could be heard in the still of night."),
    ("Still", "Adverb", "He is still in business."),
    ("Still", "Verb", "With his name the mothers still their babes."),
    ("Such", "Adjective", "Don't be in such a hurry."),
    ("Such", "Pronoun", "Such was not my intention."),
    ("The", "Adverb", "The wiser he is, the better."),
    ("Till", "Preposition", "Never put off till tomorrow what you can do today."),
    ("Till", "Conjunction", "Do not start till I give the word."),
    ("Up", "Adverb", "Prices are up."),
    ("Up", "Preposition", "Let us go up the hill."),
    ("Up", "Adjective", "The next up train will leave here at 12.30."),
    ("Up", "Noun", "They had their ups and downs of fortune."),
    ("Well", "Noun", "Let well alone."),
    ("Well", "Adjective", "I hope you are now well."),
    ("Well", "Adverb", "Well begun is half done."),
    ("Well", "Interjection", "Well, who would have thought it?"),
    ("What", "Adjective", "What evidence have you got?"),
    ("What", "Interjection", "What! you don't mean to say so?"),
    ("What", "Pronoun", "What does he want?"),
    ("While", "Noun", "Sit down and rest a while."),
    ("While", "Verb", "They while away their evenings with books and games."),
    ("While", "Conjunction", "While a great poet, he is a greater novelist."),
    ("Why", "Adverb", "Why did you do it?"),
    ("Why", "Interjection", "Why, it is surely Nanak!"),
    ("Why", "Noun", "This is not the time to go into the why and the wherefore of it."),
    ("Yet", "Adverb", "There is more evidence yet to be offered."),
    ("Yet", "Conjunction", "He is willing, yet unable."),
    ("Better", "Adjective", "I think yours is a better plan."),
    ("Better", "Adverb", "I know better."),
    ("Both", "Pronoun", "Both of them are dead."),
    ("Both", "Adjective", "You cannot have it both ways."),
    ("Both", "Conjunction", "Both the cashier and the accountant are Hindus."),
    ("Either", "Conjunction", "He must either work or starve."),
    ("Either", "Adjective", "Either bat is good enough."),
    ("Either", "Pronoun", "Ask either of them."),
    ("Else", "Conjunction", "Make haste, else you will miss the train."),
    ("Else", "Adjective", "I have something else for you."),
    ("Else", "Adverb", "Shall we look anywhere else?"),
    ("Down", "Adverb", "Down went the ship."),
    ("Down", "Preposition", "The fire engine came rushing down the hill."),
    ("Down", "Adjective", "The porter was killed by the down train."),
    ("Down", "Noun", "He has seen the ups and downs of life."),
    ("But", "Adverb", "It is but right to admit our faults."),
    ("But", "Preposition", "None but the brave deserves the fair."),
    ("But", "Conjunction", "We tried hard, but did not succeed."),
    ("After", "Adverb", "They arrived soon after."),
    ("After", "Preposition", "He takes after his father."),
    ("After", "Conjunction", "We went away after they had left."),
    ("After", "Adjective", "After ages shall sing his glory."),
    ("Before", "Adverb", "I have seen you before."),
    ("Before", "Preposition", "He came before the appointed time."),
    ("Before", "Conjunction", "He went away before I came."),
    ("Above", "Adverb", "The heavens are above."),
    ("Above", "Preposition", "The moral law is above the civil."),
    ("Above", "Adjective", "Analyse the above sentence."),
    ("Above", "Noun", "Our blessings come from above."),
    ("All", "Adjective", "All men are mortal."),
    ("All", "Adverb", "He was all alone when I saw him."),
    ("All", "Pronoun", "All spoke in his favour."),
    ("All", "Noun", "He lost his all in speculation."),
    ("About", "Adverb", "They wandered about in sheepskins and goatskins."),
    ("About", "Preposition", "There is something pleasing about him."),
    ("As", "Adverb", "We walked as fast as we could."),
    ("As", "Conjunction", "As he was poor I helped him."),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def word_questions():
    out = []
    for n, (word, part, sentence) in enumerate(ENTRIES):
        others = [p for p in POS if p != part][:3]
        pos = n % 4
        options = [part] + others
        reasons = [f"Correct: '{word}' is used as {part.lower()} in this sentence."] + \
                  [f"Wrong: '{word}' is not used as {o.lower()} in this sentence." for o in others]
        out.append({"chapter": 43, "source": "Book", "exercise": "Word list (section 420 onward)",
                    "stem": f'In "{sentence}", what part of speech is "{word}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is used as {part.lower()} in this sentence.",
                    "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Composition 102 (printed as Composition, but it is a parts-of-speech exercise): key page 39
# (keyimg p-042). Item 3 is skipped (two instances of "right" in one sentence). Item 42 is skipped: the key
# says conjunction, but "after" in "May comes after April" is a preposition, so the key looks wrong there.
# (item, sentence, italic word, part of speech)
EX102 = [
    (1, "He kept the fast for a week.", "fast", "Noun"),
    (2, "Mohammedans fast in the month of Ramzan.", "fast", "Verb"),
    (4, "God defend the right!", "right", "Noun"),
    (5, "There is much truth in what he says.", "much", "Adjective"),
    (6, "Much cry and little wool.", "Much", "Adjective"),
    (7, "Don't boast too much.", "much", "Adverb"),
    (8, "It is hard to understand.", "hard", "Adjective"),
    (9, "Men who work hard enjoy life fully.", "hard", "Adverb"),
    (10, "Little learning is a dangerous thing.", "Little", "Adjective"),
    (11, "He is little known here.", "little", "Adverb"),
    (12, "It matters little what he says.", "little", "Adverb"),
    (13, "I have long thought so.", "long", "Adverb"),
    (14, "It is long since we met.", "long", "Noun"),
    (15, "Still waters run deep.", "Still", "Adjective"),
    (16, "He still lives in that house.", "still", "Adverb"),
    (17, "That boy gives any amount of trouble.", "any", "Adjective"),
    (18, "Is that any better?", "any", "Adverb"),
    (19, "A better man than he never lived.", "better", "Adjective"),
    (20, "He knows better than to quarrel.", "better", "Adverb"),
    (21, "He spoke in a loud voice.", "loud", "Adjective"),
    (22, "Do not speak so loud.", "loud", "Adverb"),
    (23, "Most people think so.", "Most", "Adjective"),
    (24, "What most annoys me is his obstinacy.", "most", "Adverb"),
    (25, "Some twenty boys were absent.", "Some", "Adverb"),
    (26, "I will take some, but not all.", "some", "Pronoun"),
    (27, "Please call me early.", "early", "Adverb"),
    (28, "The early bird catches the worm.", "early", "Adjective"),
    (29, "That can stand over.", "over", "Adverb"),
    (30, "Take this parcel over to the post office.", "over", "Adverb"),
    (31, "He has no command over himself.", "over", "Preposition"),
    (32, "He was only a yard off me.", "off", "Preposition"),
    (33, "Suddenly one of the wheels came off.", "off", "Adverb"),
    (34, "I must be off.", "off", "Adverb"),
    (35, "He told us all about the battle.", "about", "Preposition"),
    (36, "He lives about two miles from here.", "about", "Adverb"),
    (37, "Several men were standing about.", "about", "Adverb"),
    (38, "After the storm comes the calm.", "After", "Preposition"),
    (39, "The after effects of potash bromide are bad.", "after", "Adjective"),
    (40, "He went after I came.", "after", "Conjunction"),
    (41, "The minstrels follow after.", "after", "Adverb"),
    (43, "All fish are not caught with flies.", "All", "Adjective"),
    (44, "All is fair in love and war.", "All", "Pronoun"),
    (45, "We shall lie all alike in our graves.", "all", "Adverb"),
    (46, "He that is warm thinks all so.", "all", "Pronoun"),
    (47, "What is all this noise?", "all", "Adjective"),
    (48, "All is not lost.", "All", "Pronoun"),
    (49, "He is all for amusement.", "all", "Adverb"),
    (50, "All is good in a famine.", "All", "Pronoun"),
]


def ex102_questions():
    out = []
    for n, (item, sentence, word, part) in enumerate(EX102):
        others = [p for p in POS if p != part][:3]
        pos = n % 4
        options = [part] + others
        reasons = [f"Correct: '{word}' is used as {part.lower()} in this sentence."] + \
                  [f"Wrong: '{word}' is not used as {o.lower()} in this sentence." for o in others]
        out.append({"chapter": 43, "source": "Book", "exercise": f"Exercise in Composition 102, item {item}",
                    "stem": f'In "{sentence}", what part of speech is "{word}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is used as {part.lower()} in this sentence.",
                    "reasons": _rotate(reasons, pos)})
    return out


# Exercise in Composition 103: parts of speech (key page 39, keyimg p-042). Skipped: items 4, 5, 8 (key looks
# inconsistent or the word is a relative pronoun), 16 (key says preposition, but "but that" joins clauses),
# 18, 28 (key says pronoun, sentence is an adverb), 40 (key says adjective, "set it right" is an adverb),
# 47 and 48 (relative pronouns).
# (item, sentence, italic word, part of speech)
EX103 = [
    (1, "He is not any the worse for it.", "any", "Adverb"),
    (2, "A thing you don't want is dear at any price.", "any", "Adjective"),
    (3, "I thought as much.", "as", "Adverb"),
    (6, "As he was ambitious, I slew him.", "As", "Conjunction"),
    (7, "Men fear death as children to go in the dark.", "as", "Conjunction"),
    (9, "He did his best.", "best", "Noun"),
    (10, "I like this best.", "best", "Adverb"),
    (11, "He is my best friend.", "best", "Adjective"),
    (12, "He is but a child.", "but", "Adverb"),
    (13, "Fear nought but sin.", "but", "Preposition"),
    (14, "But for his help, I could not have done it.", "But", "Preposition"),
    (15, "The paths of glory lead but to the grave.", "but", "Adverb"),
    (17, "I change, but I cannot die.", "but", "Conjunction"),
    (19, "The fool is busy in everyone's business but his own.", "but", "Preposition"),
    (20, "Enough of this!", "Enough", "Noun"),
    (21, "She sings well enough.", "enough", "Adverb"),
    (22, "Enough is as good as a feast.", "Enough", "Noun"),
    (23, "We have not men enough.", "enough", "Adjective"),
    (24, "He is like his father.", "like", "Preposition"),
    (25, "I like the offer.", "like", "Verb"),
    (26, "Did you ever hear the like of it?", "like", "Noun"),
    (27, "Do not talk like that.", "like", "Preposition"),
    (29, "This sum is more difficult.", "more", "Adverb"),
    (30, "More will be wanted.", "More", "Pronoun"),
    (31, "He stood next me in class.", "next", "Preposition"),
    (32, "The next moment he was dead.", "next", "Adjective"),
    (33, "What happened next?", "next", "Adverb"),
    (34, "We have no money.", "no", "Adjective"),
    (35, "He is no better, no worse.", "no", "Adverb"),
    (36, "His answer was a decided no.", "no", "Noun"),
    (37, "Right the wrong.", "Right", "Verb"),
    (38, "He is in the right.", "right", "Noun"),
    (39, "He is always right.", "right", "Adjective"),
    (41, "Use right words.", "right", "Adjective"),
    (42, "Since you say so, I believe it.", "Since", "Conjunction"),
    (43, "He has been ill since yesterday.", "since", "Preposition"),
    (44, "He has returned home long since.", "since", "Adverb"),
    (45, "What was that noise?", "What", "Adjective"),
    (46, "He died so that he might save his country.", "so", "Conjunction"),
    (49, "What nonsense is this!", "What", "Adjective"),
    (50, "What does it profit?", "What", "Pronoun"),
]


def ex103_questions():
    out = []
    for n, (item, sentence, word, part) in enumerate(EX103):
        others = [p for p in POS if p != part][:3]
        pos = n % 4
        options = [part] + others
        reasons = [f"Correct: '{word}' is used as {part.lower()} in this sentence."] + \
                  [f"Wrong: '{word}' is not used as {o.lower()} in this sentence." for o in others]
        out.append({"chapter": 43, "source": "Book", "exercise": f"Exercise in Composition 103, item {item}",
                    "stem": f'In "{sentence}", what part of speech is "{word}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"'{word}' is used as {part.lower()} in this sentence.",
                    "reasons": _rotate(reasons, pos)})
    return out
