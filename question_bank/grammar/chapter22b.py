"""Chapter 22 (Active and Passive Voice), continued: Exercise in Grammar 40 and Exercise 41 (passive conversion).

Answers: key page 15 (keyimg p-018). Each question asks for the passive form of an active sentence.
Distractors are passive forms from neighbouring items. Where the key is unreadable, the book's active
sentence is used as the source and the passive is built from it.
"""

LETTERS = "ABCD"

# Exercise in Grammar 40: (item, active sentence, passive sentence from key)
EX40 = [
    (1, "The cat killed the mouse.", "The mouse was killed by the cat."),
    (2, "The man cut down the tree.", "The tree was cut down by the man."),
    (3, "Columbus discovered America.", "America was discovered by Columbus."),
    (4, "His teacher praised him.", "He was praised by his teacher."),
    (5, "The boy teased the dog.", "The dog was teased by the boy."),
    (6, "The syce feeds the horse every day.", "The horse is fed by the syce every day."),
    (7, "The police arrested him.", "He was arrested."),
    (8, "Rama was making a kite.", "A kite was being made by Rama."),
    (9, "The boy caught the ball.", "The ball was caught by the boy."),
    (10, "My father will write a letter.", "A letter will be written by my father."),
    (11, "I will conquer him.", "He will be conquered by me."),
    (12, "He kept me waiting.", "I was kept waiting."),
    (13, "The hunter shot the lion.", "The lion was shot by the hunter."),
    (14, "Hari opened the door.", "The door was opened by Hari."),
    (15, "A policeman caught the thief.", "The thief was caught by a policeman."),
    (16, "Sohrab threw the ball.", "The ball was thrown by Sohrab."),
    (17, "He scored twenty runs.", "Twenty runs were scored by him."),
    (18, "Your behaviour vexes me.", "I am vexed by your behaviour."),
    (19, "Manners reveal character.", "Character is revealed by manners."),
    (20, "He made a very remarkable discovery.", "A very remarkable discovery was made by him."),
    (21, "Little strokes fell great oaks.", "Great oaks are felled by little strokes."),
    (22, "Dhondu will bring the pony.", "The pony will be brought by Dhondu."),
    (23, "Everyone loves him.", "He is loved by everyone."),
    (24, "My cousin has drawn this picture.", "This picture has been drawn by my cousin."),
    (25, "We expect good news.", "Good news is expected."),
    (26, "The farmer gathers the harvest.", "The harvest is gathered by the farmer."),
    (27, "His own brother swindled him.", "He was swindled by his own brother."),
    (28, "The recitation pleased the inspector.", "The inspector was pleased by the recitation."),
    (29, "Somebody has put out the light.", "The light has been put out."),
    (30, "The enemy have defeated our army.", "Our army had been defeated."),
    (31, "They sell TVs here.", "TVs are sold here."),
    (32, "I have sold my bicycle.", "My bicycle has been sold."),
    (33, "People will soon forget it.", "It will soon be forgotten."),
    (34, "They opened the theatre only last month.", "The theatre was opened only last month."),
    (35, "We prohibit smoking.", "Smoking is prohibited."),
]

# Exercise 41: (item, active sentence, passive sentence from key). Key items 2, 6, 7 and 12 are not
# read cleanly on the key page and are left out.
EX41 = [
    (1, "We saw you and him.", "You and he were seen by us."),
    (3, "We refused them admission.", "They were refused admission."),
    (4, "I bought the baby a doll.", "A doll was bought for the baby."),
    (5, "They found him guilty of murder.", "He was found guilty of murder."),
    (8, "They saw the storm approaching.", "The storm was seen approaching."),
    (9, "He keeps me waiting.", "I am kept waiting."),
    (10, "They painted the house red.", "The house was painted red."),
    (11, "He told me to leave the room.", "I was told to leave the room."),
    (13, "I shall order the carriage.", "The carriage will be ordered."),
    (14, "The boy is climbing the cliff.", "The cliff is being climbed by the boy."),
    (15, "One may accomplish many things by a little effort.", "Many things can be accomplished by a little effort."),
    (16, "I am watching you very carefully.", "You are being watched carefully."),
]


def _rotate(items, pos):
    rest = items[1:]
    return rest[:pos] + [items[0]] + rest[pos:]


def _questions(rows, exercise, chapter_offset):
    out = []
    for n, (item, active, passive) in enumerate(rows):
        # Build four options: correct passive first, then passives from neighbouring items.
        options = [passive]
        j = 1
        while len(options) < 4:
            cand = rows[(n + j) % len(rows)][2]
            if cand not in options:
                options.append(cand)
            j += 1
        pos = (n + chapter_offset) % 4
        reasons = [f"Correct: this keeps the meaning and makes the object the subject."] + \
                  [f"Wrong: this does not match the active sentence '{active}'." for _ in options[1:]]
        out.append({"chapter": 22, "source": "Book", "exercise": f"Exercise in {exercise}, item {item}",
                    "stem": f'Which is the passive form of "{active}"?',
                    "options": _rotate(options, pos), "correct": LETTERS[pos],
                    "explanation": f"The passive form is '{passive}'.", "reasons": _rotate(reasons, pos)})
    return out


def ex40_questions():
    return _questions(EX40, "Grammar 40", 0)


def ex41_questions():
    return _questions(EX41, "Composition 41", 1)
