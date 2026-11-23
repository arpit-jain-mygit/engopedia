"""Cambridge Stage 8 content and student-made tests: content is complete and tests are built and marked correctly."""
from app import cambridge


def test_all_25_chapters_have_notes_and_questions():
    chapters = cambridge.chapters()
    assert [c["chapter"] for c in chapters] == list(range(1, 26))
    for c in chapters:
        ch = cambridge.chapter(c["chapter"])
        assert ch["notes"], f"chapter {c['chapter']} has no notes"
        assert c["questions"] >= 10, f"chapter {c['chapter']} has too few questions"


def test_every_question_is_well_formed():
    seen = set()
    for c in cambridge.chapters():
        for q in cambridge.questions(c["chapter"]):
            assert q["id"] not in seen
            seen.add(q["id"])
            assert len(q["options"]) in (2, 4)
            assert len(set(q["options"])) == len(q["options"])
            assert q["answer"] in q["options"]
            assert q["explanation"]
            if q.get("blank"):
                assert q["blank"].count("____") == 1


def test_build_only_uses_chosen_chapters_and_formats():
    items = cambridge.build([3], ["A", "D"], 50)
    assert items
    assert all(i["chapter"] == 3 for i in items)
    assert {i["format"] for i in items} <= {"A", "D"}


def test_build_respects_count():
    assert len(cambridge.build([1, 2], ["A", "B", "C", "D"], 7)) == 7


def test_multiple_choice_grades_the_right_letter():
    q = cambridge.quiz(1)[0]
    right = [L for L in "ABCD" if cambridge.grade([{"id": q["id"], "answer": L}])["results"][0]["correct"]]
    assert len(right) == 1
    wrong = next(L for L in "ABCD" if L != right[0])
    assert cambridge.grade([{"id": q["id"], "answer": wrong}])["results"][0]["correct"] is False


def test_write_answer_ignores_spaces_and_case():
    item = next(i for i in cambridge.build([5], ["D"], 50) if i["id"].startswith("c05-q03"))
    assert cambridge.grade([{"id": item["id"], "answer": "6 ( 3n - 1 )"}])["results"][0]["correct"]


def test_unknown_id_is_reported():
    result = cambridge.grade([{"id": "nope", "answer": "x"}])
    assert result["results"][0]["known"] is False
    assert result["score"] == 0
