"""Build the nine-format quiz from the QuestionBank sheet, offline, and save a review workbook.

Sources (all in question_bank/word_power_made_easy_with_QuestionBank.xlsx):
  QuestionBank  the question, four options, the correct letter, the explanation and a reason per option
  Words         each word's meaning, sample sentence, parts and its own roots
  Morphemes     meanings of prefixes, roots and suffixes

Formats, in rotation by Q No. A question takes the next format in the rotation that it can
support, so neighbouring questions differ:
  emoji      the sheet question with a picture
  scenario   the sheet question as a short scene with a picture
  hear       the sample sentence read aloud with the word blanked; choose the word
  tf         "<word> means: <meaning>", true or false
  odd        three words built from one root plus one that is not; pick the odd one
  match      words and their meanings
  build      tap the parts of the word in order
  type       type the word
  two        step 1: what a part means; step 2: the sheet question

Outputs:
  backend/data/quiz.json                        the game content (replaces the previous quiz)
  question_bank/quiz_formats_review.xlsx        one row per question for review

Usage: backend/.venv/bin/python scripts/build_quiz_formats.py
"""
import json
import random
import re
from collections import defaultdict
from pathlib import Path

from openpyxl import Workbook, load_workbook

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "question_bank" / "word_power_made_easy_with_QuestionBank.xlsx"
QUIZ = ROOT / "backend" / "data" / "quiz.json"
REVIEW = ROOT / "question_bank" / "quiz_formats_review.xlsx"
FORMATS = ["emoji", "scenario", "hear", "tf", "odd", "match", "build", "type", "two"]
LETTERS = "ABCD"
MAX_MEANING = 60

# Picture for the emoji and scenario formats, picked from words in the question.
PICTURES = {
    "money": "💰", "pay": "💰", "book": "📚", "read": "📖", "sea": "🌊", "water": "💧",
    "fire": "🔥", "sun": "☀️", "moon": "🌙", "star": "⭐", "animal": "🐾", "dog": "🐶",
    "cat": "🐱", "bird": "🐦", "fish": "🐟", "snake": "🐍", "tree": "🌳", "flower": "🌸",
    "hand": "✋", "eye": "👁️", "heart": "❤️", "brain": "🧠", "mind": "🧠", "music": "🎵",
    "king": "👑", "war": "⚔️", "food": "🍽️", "eat": "🍽️", "light": "💡", "earth": "🌍",
}
FALLBACK_PICTURE = {"emoji": "🔍", "scenario": "🧭"}


def picture(stem, kind):
    low = stem.lower()
    for word, emoji in PICTURES.items():
        if word in low:
            return emoji
    return FALLBACK_PICTURE[kind]


def read_sources():
    wb = load_workbook(SOURCE, read_only=True)
    words = {}
    for r in wb["Words"].iter_rows(min_row=2, values_only=True):
        if r[2]:
            words[r[2]] = {
                "meaning": (r[5] or "").strip(),
                "sentence": (r[6] or "").strip(),
                "parts": [p.strip() for p in (r[7] or "").split(",") if p.strip() and p.strip() != "-"],
                "roots": [x.strip() for x in (r[4] or "").split(",") if x.strip() and x.strip() != "-"],
            }
    morphemes = {r[0]: r[2] for r in wb["Morphemes"].iter_rows(min_row=2, values_only=True) if r[0]}
    questions = [r for r in wb["QuestionBank"].iter_rows(min_row=2, values_only=True) if r[0] is not None]
    return words, morphemes, questions


def parse_reasons(text):
    """'A. Word: Correct: reason' lines -> four plain reasons in A to D order."""
    out = {}
    for line in (text or "").splitlines():
        m = re.match(r"^([ABCD])\.\s*(.*)$", line.strip())
        if not m:
            continue
        body = m.group(2).split(": ", 1)[-1]
        out[m.group(1)] = re.sub(r"^(Correct|Wrong):\s*", "", body, flags=re.I).strip()
    return [out.get(letter, "") for letter in LETTERS]


def part_name(piece):
    """'ambi- (prefix)' -> 'ambi-'; 'vert (root)' -> 'vert'."""
    return piece.split(" (")[0].strip()


def tiles_for(word, info):
    """Parts of the word in order, when they spell the word exactly; otherwise two or three chunks."""
    pieces = [part_name(p).strip("-") for p in info["parts"]]
    if len(pieces) >= 2 and "".join(pieces) == word:
        return pieces
    cut = max(2, len(word) // 3)
    chunks = [word[:cut], word[cut:2 * cut], word[2 * cut:]]
    return [c for c in chunks if c]


def sentence_blank(word, sentence):
    stem = word[:-1] if word.endswith("e") else word
    pattern = re.compile(r"\b" + re.escape(stem) + r"\w*", re.IGNORECASE)
    if not sentence or not pattern.search(sentence):
        return None
    return pattern.sub("blank", sentence, count=1)


def build_all():
    words, morphemes, rows = read_sources()
    by_root = defaultdict(list)
    for w, info in words.items():
        for r in info["roots"]:
            by_root[r].append(w)

    roots, root_seen, questions, review = [], {}, [], []
    for idx, (qno, qroot, word, stem, a, b, c, d, letter, explanation, why) in enumerate(rows):
        rng = random.Random(qno)
        info = words[word]
        options = [a, b, c, d]
        answer = LETTERS.index(letter.strip().upper())
        reasons = parse_reasons(why)
        if qroot not in root_seen:
            root_seen[qroot] = len(roots)
            meaning = morphemes.get(qroot) or ""
            if not meaning:
                m = re.search(r"\(([^)]+)\)", explanation or "")
                meaning = m.group(1) if m else ""
            roots.append({"root": qroot, "meaning": meaning, "words": 0})
        roots[root_seen[qroot]]["words"] += 1

        def make(fmt):
            """Return the question body for one format, or None when this word cannot support it."""
            if fmt in ("emoji", "scenario"):
                return {"prompt": stem, "choices": options, "answer": answer, "reasons": reasons,
                        "scene": picture(stem, fmt)}
            if fmt == "hear":
                blank = sentence_blank(word, info["sentence"])
                if not blank:
                    return None
                return {"prompt": "Listen, then choose the word that fits the blank.", "speak": blank,
                        "choices": options, "answer": answer, "reasons": reasons}
            if fmt == "tf":
                truth = qno % 2 == 0
                meaning = info["meaning"]
                if not truth:
                    other = next((w for w in words if w != word and words[w]["meaning"] != meaning), None)
                    if other is None:
                        return None
                    meaning = words[other]["meaning"]
                if not meaning or len(meaning) > MAX_MEANING * 3:
                    return None
                return {"prompt": f'"{word}" means: {meaning}', "choices": ["True", "False"],
                        "answer": 0 if truth else 1}
            if fmt == "odd":
                own = [r for r in info["roots"] if len(by_root[r]) >= 3]
                if not own:
                    return None
                root_word = own[0]
                peers = sorted(x for x in by_root[root_word] if x != word)
                outside = sorted(w for w in words if root_word not in words[w]["roots"])
                if len(peers) < 2 or not outside:
                    return None
                trio = [word] + rng.sample(peers, 2)
                odd = rng.choice(outside)
                choices = trio + [odd]
                rng.shuffle(choices)
                return {"prompt": f'Which word is NOT built from "{root_word}"?', "choices": choices,
                        "answer": choices.index(odd)}
            if fmt == "match":
                own = [r for r in info["roots"] if len(by_root[r]) >= 3]
                if not own:
                    return None
                pool = sorted(x for x in by_root[own[0]] if x != word)
                group = [word] + rng.sample(pool, min(3, len(pool)))
                pairs = [[w, words[w]["meaning"]] for w in group]
                if any(len(p[1]) > MAX_MEANING * 3 for p in pairs):
                    return None
                return {"prompt": "Match each word to its meaning.", "pairs": pairs}
            if fmt == "build":
                tiles = tiles_for(word, info)
                if "".join(tiles) != word or len(tiles) < 2:
                    return None
                shuffled = tiles[:]
                rng.shuffle(shuffled)
                return {"prompt": f"Tap the pieces in order to build the word for: {info['meaning']}",
                        "tiles": shuffled, "target": word}
            if fmt == "type":
                return {"prompt": f"{stem} Type the word.", "target": word}
            if fmt == "two":
                part = next((p for p in info["parts"] if part_name(p) in morphemes), None)
                if part is None:
                    return None
                name = part_name(part)
                correct_meaning = morphemes[name]
                if not correct_meaning or len(correct_meaning) > MAX_MEANING:
                    return None
                distract = [m for m in morphemes.values() if m and m != correct_meaning and len(m) <= MAX_MEANING]
                if len(distract) < 3:
                    return None
                meanings = [correct_meaning] + rng.sample(sorted(set(distract)), 3)
                rng.shuffle(meanings)
                step1 = {"prompt": f'Step 1: what does "{name}" mean?', "choices": meanings,
                         "answer": meanings.index(correct_meaning), "good": f'"{name}" means {correct_meaning}.'}
                step2 = {"prompt": stem, "choices": options, "answer": answer, "good": explanation}
                return {"stages": [step1, step2]}
            return None

        preferred = FORMATS[idx % len(FORMATS)]
        order = FORMATS[idx % len(FORMATS):] + FORMATS[:idx % len(FORMATS)]
        chosen, body = None, None
        for fmt in order:
            body = make(fmt)
            if body is not None:
                chosen = fmt
                break
        if chosen is None:
            raise SystemExit(f"no format fits Q{qno} {word}")

        q = {"id": f"{qroot.lower()}-{qno}", "root": qroot, "format": chosen, "good": explanation,
             "try": "Read the reason for the option you picked, then try again."
             if chosen in ("emoji", "scenario", "hear") else
             {"tf": "Compare the word with its meaning again.",
              "odd": "Look for the word that does not contain this root.",
              "match": "Check which meaning fits each word.",
              "build": "Put the pieces in the right order and try again.",
              "type": "Check the spelling and try again.",
              "two": "Work out what the part means first."}[chosen],
             "roots": [[qroot, roots[root_seen[qroot]]["meaning"]]]}
        q.update(body)
        if "stages" in body:
            q.pop("reasons", None)
        questions.append(q)
        review.append([qno, qroot, word, preferred, chosen, body_summary(q), ""])
    return roots, questions, review


def body_summary(q):
    if q["format"] == "two":
        s1, s2 = q["stages"]
        return f'Step 1: {s1["prompt"]} [{" | ".join(s1["choices"])}]  Step 2: {s2["prompt"]} [{" | ".join(s2["choices"])}]'
    if q["format"] == "match":
        return " | ".join(f"{w} = {m}" for w, m in q["pairs"])
    if q["format"] == "build":
        return f'tiles {q["tiles"]} -> {q["target"]}'
    if q["format"] == "type":
        return f'type: {q["target"]}'
    if q["format"] == "hear":
        return f'says: {q["speak"]} [{" | ".join(q["choices"])}]'
    if q["format"] == "tf":
        return f'{q["prompt"]} -> {q["choices"][q["answer"]]}'
    if q["format"] == "odd":
        return f'[{" | ".join(q["choices"])}] odd: {q["choices"][q["answer"]]}'
    return " | ".join(f"{L}. {c}" for L, c in zip(LETTERS, q["choices"])) + f' (answer {LETTERS[q["answer"]]})'


def write_review(review):
    wb = Workbook()
    ws = wb.active
    ws.title = "Quiz formats"
    ws.append(["Q No", "Root", "Word", "Preferred format", "Format used", "Question as built", "Reviewed"])
    for row in review:
        ws.append(row)
    for col, width in zip("ABCDEFG", (8, 14, 18, 16, 14, 100, 12)):
        ws.column_dimensions[col].width = width
    wb.save(REVIEW)


def main():
    roots, questions, review = build_all()
    QUIZ.write_text(json.dumps({"roots": roots, "questions": questions}, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    write_review(review)
    counts = defaultdict(int)
    for q in questions:
        counts[q["format"]] += 1
    fell_back = sum(1 for r in review if r[3] != r[4])
    print(f"levels {len(roots)}, questions {len(questions)}, fell back {fell_back}: {dict(counts)}")


if __name__ == "__main__":
    main()
