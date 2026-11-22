"""Turn a batch data module into roots/<root>.json files.

Several words can share one root, so questions are grouped by root.
The correct answer is spread across A-D.
"""
import importlib
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
mod = importlib.import_module(sys.argv[1])
groups = defaultdict(list)
for i, item in enumerate(mod.BATCH):
    pos = i % 4
    options = [w for w in item["wrong"]]
    options.insert(pos, item["correct"])
    reasons = {}
    for j, L in enumerate("ABCD"):
        opt = options[j]
        reasons[L] = item["correct_reason"] if opt == item["correct"] else item["wrong"][opt]
    groups[item["root"]].append({
        "word": item["word"], "question": item["question"], "options": options,
        "correct": "ABCD"[pos], "explanation": item["explanation"], "reasons": reasons,
    })
for root, qs in groups.items():
    path = HERE / "roots" / f"{root}.json"
    path.write_text(json.dumps(qs, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", len(groups), "root files for", len(mod.BATCH), "questions")
