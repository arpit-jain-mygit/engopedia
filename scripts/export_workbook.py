"""Export the Word Power Made Easy workbook into JSON seed data for the app.

Reads the Morphemes and Words sheets, then writes backend/data/words.json and
backend/data/morphemes.json. Run once after the workbook changes.
"""
import json
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

SOURCE = Path(sys.argv[1])
OUT_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

wb = load_workbook(SOURCE, read_only=True, data_only=True)

morphemes = {}
for name, mtype, meaning, *_used in wb["Morphemes"].iter_rows(min_row=2, values_only=True):
    if name:
        morphemes[name] = {"type": mtype, "meaning": meaning}

words = []
for _no, session, word, built_from, roots, meaning, sentence, *_levels in wb["Words"].iter_rows(min_row=2, values_only=True):
    if not word:
        continue
    parts = []
    for piece in (built_from or "").split(" + "):
        piece = piece.strip()
        # Morphemes are written as "text (meaning)"; plain words have no annotation.
        text = re.sub(r"\s*\(.*\)$", "", piece)
        parts.append(text)
    root_list = [r.strip() for r in (roots or "").split(",") if r.strip() and r.strip() != "-"]
    words.append({
        "word": word,
        "session": session,
        "parts": parts,
        "roots": root_list,
        "meaning": meaning or "",
        "sentence": sentence or "",
    })

(OUT_DIR / "words.json").write_text(json.dumps(words, ensure_ascii=False, indent=1), encoding="utf-8")
(OUT_DIR / "morphemes.json").write_text(json.dumps(morphemes, ensure_ascii=False, indent=1), encoding="utf-8")
print("words:", len(words), "morphemes:", len(morphemes))
