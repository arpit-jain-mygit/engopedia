"""Chapter 26 (The Future): Exercise in Grammar 48 plus generated questions.

Answers: key page 17 (keyimg p-020). Each blank gets a question; the correct form comes from the key.
"""

LETTERS = "ABCD"

# (item, sentence with blank, book choices (two), correct form from the key)
EX48 = [
    (1, "The plane ____ at 3.30.", ["arrives", "will arrive"], "arrives"),
    (2, "I will phone you when he ____ back.", ["comes", "will come"], "comes"),
    (3, "When I get home, my dog ____ at the gate waiting for me.", ["sits", "will be sitting"], "will be sitting"),
    (4, "I ____ the Joshis this evening.", ["visit", "am visiting"], "am visiting"),
    (5, "Look at those black clouds. It ____.", ["will rain", "is going to rain"], "is going to rain"),
    (6, "The train ____ before we reach the station.", ["arrives", "will have arrived"], "will have arrived"),
    (7, "Perhaps we ____ Mahabaleshwar next month.", ["visit", "will visit"], "will visit"),
    (8, "Unless we ____ now we can't be on time.", ["start", "will start"], "start"),
    (9, "I ____ into town later on. Do you want a lift?", ["drive", "will be driving"], "will be driving"),
    (10, "The next term ____ on 16th November.", ["begins", "is beginning"], "begins"),
    (11, "Oh dear! I ____.", ["will sneeze", "am going to sneeze"], "am going to sneeze"),
    (12, "By 2020, robots ____ many of the jobs that people do today.", ["will be taking over", "will have taken over"], "will have taken over"),
    (13, "I'm sure she ____ the exam.", ["passes", "will pass"], "will pass"),
    (14, "I ____ home next Sunday.", ["go", "am going"], "am going"),
    (15, "I ____ you one of these days, I expect.", ["see", "will be seeing"], "will be seeing"),
    (16, "Help! I ____ fall.", ["will", "am going to"], "am going to"),
    (17, "She has bought some cloth; she ____ herself a blouse.", ["will make", "is going to make"], "is going to make"),
    (18, "I ____ your house this afternoon. It is on my way home from work.", ["will be passing", "am passing"], "am passing"),
    (19, "Hurry up! The programme ____.", ["will start", "is about to start"], "is about to start"),
    (20, "This book is not long. I ____ it by lunch time.", ["will be reading", "will have read"], "will have read"),
]

GEN = [
    ("'Look at the sky, it ____ soon.' The best form is:", "is going to rain", ["will rain", "rains", "rained"],
     "'Look at the sky' shows the rain is already expected from the evidence, so 'going to' fits.",
     ["Correct: the evidence now shows the rain is coming.", "Wrong: 'will rain' is possible but not based on present evidence.", "Wrong: simple present is not used for this future.", "Wrong: simple past is for the past."]),
    ("'The meeting ____ at 10 o'clock tomorrow.' The best form is:", "starts", ["will be starting", "is starting", "started"],
     "A fixed timetable event uses the simple present, even for the future.",
     ["Correct: a fixed timetable uses the simple present.", "Wrong: the continuous form suggests an arranged activity, not a timetable.", "Wrong: the form is not used here.", "Wrong: simple past is for the past."]),
    ("'I ____ you when I reach home.' The best form is:", "will call", ["am calling", "called", "call"],
     "A decision or promise made at the moment of speaking takes 'will'.",
     ["Correct: 'will' is used for a decision or promise.", "Wrong: continuous describes an arrangement.", "Wrong: simple past is for the past.", "Wrong: simple present does not fit this future."]),
    ("'By next year, I ____ my degree.' The best form is:", "will have finished", ["will finish", "am finishing", "finished"],
     "An action completed before a future time uses the future perfect.",
     ["Correct: an action completed before a future time.", "Wrong: simple future does not show completion before a point.", "Wrong: continuous is for an arrangement in progress.", "Wrong: simple past is for the past."]),
    ("'Tomorrow at this time, we ____ on the beach.' The best form is:", "will be lying", ["will lie", "lie", "lay"],
     "An action in progress at a future time uses the future continuous.",
     ["Correct: an action in progress at a future time.", "Wrong: simple future shows a completed or single future action.", "Wrong: simple present is not for this future.", "Wrong: simple past is for the past."]),
    ("'Hurry! The bus ____.' The best form is:", "is about to leave", ["will leave", "left", "leaves"],
     "'Is about to' shows the action is very near.",
     ["Correct: 'is about to' shows the action is very near.", "Wrong: 'will leave' is more general.", "Wrong: simple past is for the past.", "Wrong: simple present does not show nearness."]),
    ("'Do you think it ____ tomorrow?' The best form is:", "will rain", ["is going to rain", "rains", "rained"],
     "A prediction without present evidence takes 'will'.",
     ["Correct: a prediction without present evidence takes 'will'.", "Wrong: 'going to' shows evidence now.", "Wrong: simple present is not for this future.", "Wrong: simple past is for the past."]),
    ("'I ____ the film with my friends tonight.' The best form is:", "am seeing", ["will see", "saw", "see"],
     "A planned arrangement for the near future uses the present continuous.",
     ["Correct: a planned arrangement uses the present continuous.", "Wrong: 'will see' is more general, not an arrangement.", "Wrong: simple past is for the past.", "Wrong: simple present does not fit this planned future."]),
    ("'She ____ a doctor when she grows up.' The best form is:", "will be", ["is being", "was", "is"],
     "A simple future statement takes 'will be'.",
     ["Correct: a simple future statement takes 'will be'.", "Wrong: 'is being' is a present passive.", "Wrong: 'was' is past.", "Wrong: 'is' is present."]),
    ("'By the time you arrive, we ____ dinner.' The best form is:", "will have eaten", ["will eat", "are eating", "ate"],
     "An action finished before a future point uses the future perfect.",
     ["Correct: an action finished before a future point.", "Wrong: simple future does not show completion.", "Wrong: present continuous is for now.", "Wrong: simple past is for the past."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def book_questions():
    out = []
    for n, (item, sentence, choices, correct) in enumerate(EX48):
        options = [correct] + [c for c in choices if c != correct]
        j = 1
        while len(options) < 4:
            for cand in EX48[(n + j) % len(EX48)][2]:
                if cand not in options:
                    options.append(cand)
                    break
            j += 1
        options = options[:4]
        pos = n % 4
        reasons = [f"Correct: '{o}' fits the time and meaning of the sentence." if o == correct
                   else f"Wrong: '{o}' does not fit the time or meaning here." for o in options]
        out.append({"chapter": 26, "source": "Book", "exercise": f"Exercise in Grammar 48, item {item}",
                    "stem": f"Choose the correct form: {sentence}", "options": _rotate(options, pos),
                    "correct": LETTERS[pos], "explanation": f"The correct form is '{correct}'.",
                    "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 26, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
