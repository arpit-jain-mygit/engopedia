"""Chapter 25 (The Uses of the Present and Past Tenses): Exercises 46 and 47 plus generated questions.

Answers: key page 17 (keyimg p-020). The book prints Exercises 46 and 47 under "Composition", but they are
tense-choice exercises. Each blank gets a question; the correct form comes from the key.
"""

LETTERS = "ABCD"

# (exercise, sentence with blank, choices from the book, correct form from the key, extra distractor or None)
EX = [
    (46, "The earth ____ round the sun.", ["move", "moves", "moved"], "moves", None),
    (46, "My friends ____ the Prime Minister yesterday.", ["see", "have seen", "saw"], "saw", None),
    (46, "I ____ him only one letter up to now.", ["sent", "have sent", "send"], "have sent", None),
    (46, "She ____ worried about something.", ["looks", "looking", "is looking"], "looks", None),
    (46, "It started to rain while we ____ tennis.", ["are playing", "were playing", "had played"], "were playing", None),
    (46, "He ____ fast when the accident happened.", ["is driving", "was driving", "drove"], "was driving", None),
    (46, "He ____ asleep while he was driving.", ["falls", "fell", "has fallen"], "fell", None),
    (46, "I'm sure I ____ him at the party last night.", ["saw", "have seen", "had seen"], "saw", None),
    (46, "He ____ a mill in this town.", ["have", "has", "is having"], "has", None),
    (46, "He ____ here for the last five years.", ["worked", "is working", "has been working"], "has been working", None),
    (46, "He thanked me for what I ____.", ["have done", "had done", "have been doing"], "had done", None),
    (46, "I ____ a strange noise.", ["hear", "am hearing", "have been hearing"], "hear", None),
    (46, "I ____ him for a long time.", ["know", "have known", "am knowing"], "have known", None),
    (46, "I ____ English for five years.", ["study", "am studying", "have been studying"], "have been studying", None),
    (46, "Don't disturb me. I ____ my homework.", ["do", "did", "am doing"], "am doing", None),
    (46, "Abdul ____ to be a doctor.", ["wants", "wanting", "is wanting"], "wants", None),
    (46, "The soup ____ good.", ["taste", "tastes", "is tasting"], "tastes", None),
    (46, "He ____ TV most evenings.", ["watches", "is watch", "is watching"], "watches", None),
    (46, "He ____ out five minutes ago.", ["has gone", "had gone", "went"], "went", None),
    (46, "When he lived in Hyderabad, he ____ to the cinema once a week.", ["goes", "went", "was going"], "went", None),
    (46, "The baby ____ all morning.", ["cries", "has been crying"], "has been crying", "has cried"),
    (46, "I ____ Rahim at the zoo.", ["saw", "have seen", "had seen"], "saw", None),
    (46, "I ____ Kumar this week.", ["haven't seen", "didn't see", "am not seeing"], "haven't seen", None),
    (46, "This paper ____ twice weekly.", ["is appearing", "appearing", "appears"], "appears", None),
    (46, "Ashok fell off the ladder when he ____ the roof.", ["is mending", "was mending", "mended"], "was mending", None),
    (47, "The Headmaster ____ to speak to you.", ["wants", "is wanting", "was wanting"], "wants", None),
    (47, "I ____ a new bicycle last week.", ["bought", "have bought", "had bought"], "bought", None),
    (47, "Here are your shoes; I ____ them.", ["just clean", "just cleaned", "have just cleaned"], "have just cleaned", None),
    (47, "It ____ since early morning.", ["rained", "is raining", "has been raining"], "has been raining", None),
    (47, "I ____ a lot of work today.", ["did", "have done", "had done"], "have done", None),
    (47, "I ____ something burning.", ["smell", "am smelling", "have been smelling"], "smell", None),
    (47, "Look! The sun ____ over the hills.", ["rises", "is rise", "is rising"], "is rising", None),
    (47, "She ____ unconscious since four o'clock.", ["is", "was", "has been"], "has been", None),
    (47, "He used to visit us every week, but he ____ now.", ["rarely comes", "is rarely coming", "has rarely come"], "rarely comes", None),
    (47, "We ____ for his call since 4.20.", ["are waiting", "have been waiting", "were waiting"], "have been waiting", None),
    (47, "Everyday last week my aunt ____ a plate.", ["breaks", "broke", "was breaking"], "broke", None),
    (47, "I know all about that film because I ____ it twice.", ["saw", "have seen", "had seen"], "have seen", None),
    (47, "Our guests ____; they are sitting in the garden.", ["arrived", "have arrived", "had arrived"], "have arrived", None),
    (47, "I ____ him since we met a year ago.", ["didn't see", "haven't seen", "hadn't seen"], "haven't seen", None),
    (47, "We ____ our breakfast half an hour ago.", ["finished", "have finished", "had finished"], "finished", None),
    (47, "She jumped off the bus while it ____.", ["moved", "had moved", "was moving"], "was moving", None),
    (47, "When we went to the cinema, the film ____.", ["already started", "had already started", "would already start"], "had already started", None),
    (47, "I ____ for half an hour when it suddenly started to rain.", ["have walked", "have been walking", "had been walking"], "had been walking", None),
    (47, "Did you think you ____ me somewhere before?", ["have seen", "had seen", "were seeing"], "had seen", None),
    (47, "The town ____ its appearance completely since 1980.", ["is changing", "changed", "has changed"], "has changed", None),
    (47, "Sheila ____ her case, look.", ["packed", "has packed", "had packed"], "has packed", None),
    (47, "When I was in Sri Lanka, I ____ Negombo, Beruwela and Nilaveli.", ["visited", "was visited", "have visited"], "visited", None),
    (47, "I meant to repair the radio, but ____ time to do it today.", ["am not having", "haven't had", "hadn't"], "haven't had", None),
    (47, "When I ____ my dinner I went to bed.", ["had", "have had", "had had"], "had had", None),
    (47, "Men ____ to abolish wars up to now, but maybe they will find a way in the future.", ["never managed", "have never managed", "will have never managed"], "have never managed", None),
]

GEN = [
    ("Which tense is used for a habit: 'She ____ tea every morning.'", "drinks", ["is drinking", "has drunk", "drank"],
     "The simple present expresses a habitual action.",
     ["Correct: 'drinks' expresses a habit.", "Wrong: the present continuous shows an action now.", "Wrong: present perfect links past to now.", "Wrong: simple past is for a finished past action."]),
    ("'I ____ him at the station yesterday.' The best form is:", "saw", ["have seen", "had seen", "am seeing"],
     "'Yesterday' is a finished past time, so the simple past is used.",
     ["Correct: 'yesterday' needs the simple past.", "Wrong: present perfect cannot take a finished time like 'yesterday'.", "Wrong: past perfect is for an earlier past action.", "Wrong: present continuous is for now."]),
    ("'We ____ here since 2010.' The best form is:", "have lived", ["lived", "live", "had lived"],
     "'Since 2010' points from a past time to now, so the present perfect is used.",
     ["Correct: 'since' with a point in time uses the present perfect.", "Wrong: simple past cannot take 'since' like this.", "Wrong: simple present does not show time from the past.", "Wrong: past perfect is for an earlier past event."]),
    ("'The train ____ at 7 o'clock tomorrow.' The best form is:", "leaves", ["is leaving", "left", "has left"],
     "A fixed timetable event is expressed by the simple present.",
     ["Correct: a fixed timetable uses the simple present.", "Wrong: the continuous form is for arrangements in progress.", "Wrong: simple past is for a finished past event.", "Wrong: present perfect does not fit a future timetable."]),
    ("'When I arrived, they ____ dinner.' The best form is:", "had finished", ["finished", "have finished", "finish"],
     "The first action was completed before the second past action, so the past perfect is used.",
     ["Correct: an earlier past action uses the past perfect.", "Wrong: simple past does not show the earlier action.", "Wrong: present perfect does not fit a past narrative.", "Wrong: simple present does not fit a past narrative."]),
    ("'He ____ asleep when the phone rang.' The best form is:", "was", ["is", "has been", "had been"],
     "A background past action in progress takes the past continuous or simple past.",
     ["Correct: the past tense fits the background past event.", "Wrong: 'is' is present.", "Wrong: 'has been' is present perfect.", "Wrong: 'had been' does not fit this simple past event."]),
    ("'She ____ for two hours when the rain began.' The best form is:", "had been waiting", ["waits", "has waited", "was waiting"],
     "An action that continued up to a past point uses the past perfect continuous.",
     ["Correct: an action continued up to a past point.", "Wrong: simple present is not past.", "Wrong: present perfect is not past.", "Wrong: simple past continuous does not show the continued earlier period."]),
    ("'I ____ my keys. Can you help me find them?' The best form is:", "have lost", ["lost", "had lost", "am losing"],
     "The present perfect links a past loss to the present situation.",
     ["Correct: the loss affects now.", "Wrong: simple past does not link to now.", "Wrong: past perfect is for an earlier past event.", "Wrong: present continuous describes an ongoing action."]),
    ("'Last week, we ____ a film at the cinema.' The best form is:", "watched", ["have watched", "had watched", "watch"],
     "'Last week' is a finished past time, so the simple past is used.",
     ["Correct: a finished past time takes the simple past.", "Wrong: present perfect cannot take 'last week' like this.", "Wrong: past perfect is for an earlier past event.", "Wrong: simple present is not for a finished past event."]),
    ("'I ____ to Mumbai three times.' The best form is:", "have been", ["was", "had been", "am"],
     "Experience up to now uses the present perfect.",
     ["Correct: experience up to now uses the present perfect.", "Wrong: simple past is for a single finished time.", "Wrong: past perfect is for an earlier past event.", "Wrong: 'am' is present, not a past experience."]),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def book_questions():
    out = []
    counter = {46: 0, 47: 0}
    for n, (ex, sentence, choices, correct, extra) in enumerate(EX):
        counter[ex] += 1
        pool = list(choices)
        if extra:
            pool.append(extra)
        # Pad to four options with a form from a neighbouring item, never a duplicate.
        j = 1
        while len(pool) < 4:
            for cand in EX[(n + j) % len(EX)][2]:
                if cand not in pool and cand != correct:
                    pool.append(cand)
                    break
            j += 1
        options = [correct] + [o for o in pool if o != correct][:3]
        pos = n % 4
        reasons = []
        for o in options:
            if o == correct:
                reasons.append(f"Correct: '{o}' fits the time and meaning of the sentence.")
            else:
                reasons.append(f"Wrong: '{o}' does not fit the time or meaning here.")
        out.append({"chapter": 25, "source": "Book", "exercise": f"Exercise in Grammar {ex}, item {counter[ex]}",
                    "stem": f"Choose the correct form: {sentence}", "options": _rotate(options, pos),
                    "correct": LETTERS[pos], "explanation": f"The correct form is '{correct}'.",
                    "reasons": _rotate(reasons, pos)})
    return out


def generated_questions():
    out = []
    for n, (stem, correct, wrong, expl, reasons) in enumerate(GEN):
        pos = n % 4
        out.append({"chapter": 25, "source": "Generated", "exercise": "", "stem": stem,
                    "options": _rotate([correct] + wrong, pos), "correct": LETTERS[pos],
                    "explanation": expl, "reasons": _rotate(reasons, pos)})
    return out
