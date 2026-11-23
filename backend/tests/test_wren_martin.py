from fastapi.testclient import TestClient

from app import content
from app.main import create_app
from app.store import MemoryStore


def client():
    return TestClient(create_app(MemoryStore()))


def new_player(c, name="Arjun"):
    return c.post("/api/players", json={"name": name}).json()


def test_chapters_list_has_quiz_chapters_in_order():
    c = client()
    chapters = c.get("/api/wm/chapters").json()["chapters"]
    numbers = [ch["chapter"] for ch in chapters]
    assert numbers == sorted(numbers)
    assert 1 in numbers and 43 in numbers
    assert sum(ch["count"] for ch in chapters) == len(content._wm()["questions"])


def test_questions_never_include_answers():
    c = client()
    code = new_player(c)["code"]
    body = c.get(f"/api/players/{code}/wm/chapters/1/questions").json()
    assert body["questions"]
    for q in body["questions"]:
        assert "correct" not in q and "reasons" not in q and "explanation" not in q
        assert len(q["options"]) == 4


def test_unknown_chapter_is_404():
    c = client()
    code = new_player(c)["code"]
    assert c.get(f"/api/players/{code}/wm/chapters/99/questions").status_code == 404


def test_correct_answer_scores_and_marks_done():
    c = client()
    code = new_player(c)["code"]
    q = content.wm_questions(1)[0]
    res = c.post(f"/api/players/{code}/wm/answers",
                 json={"chapter": 1, "question_id": q["id"], "choice": q["correct"]}).json()
    assert res["correct"] is True and res["first_try"] is True
    assert res["points_awarded"] > 0 and res["candies_awarded"] > 0
    again = c.post(f"/api/players/{code}/wm/answers",
                   json={"chapter": 1, "question_id": q["id"], "choice": q["correct"]}).json()
    assert again["already_answered"] is True and again["points_awarded"] == 0
    listing = c.get(f"/api/players/{code}/wm/chapters/1/questions").json()
    assert listing["done"] == 1


def test_wrong_answer_gives_reason_and_no_points():
    c = client()
    code = new_player(c)["code"]
    q = content.wm_questions(1)[0]
    wrong = (q["correct"] + 1) % 4
    res = c.post(f"/api/players/{code}/wm/answers",
                 json={"chapter": 1, "question_id": q["id"], "choice": wrong}).json()
    assert res["correct"] is False and res["points_awarded"] == 0
    assert res["explanation"] == q["reasons"][wrong]
    # A later right answer still scores, but not as a first try.
    right = c.post(f"/api/players/{code}/wm/answers",
                   json={"chapter": 1, "question_id": q["id"], "choice": q["correct"]}).json()
    assert right["correct"] is True and right["first_try"] is False


def test_points_are_shared_with_word_wizard_profile():
    c = client()
    code = new_player(c)["code"]
    q = content.wm_questions(2)[0]
    c.post(f"/api/players/{code}/wm/answers",
           json={"chapter": 2, "question_id": q["id"], "choice": q["correct"]})
    profile = c.get(f"/api/players/{code}").json()
    assert profile["points"] > 0 and profile["candies"] > 0
    board = c.get("/api/leaderboard?limit=5").json()["rows"]
    assert board[0]["points"] == profile["points"]


def test_progress_counts_done_questions_per_chapter():
    c = client()
    code = new_player(c)["code"]
    qs = content.wm_questions(3)[:2]
    for q in qs:
        c.post(f"/api/players/{code}/wm/answers",
               json={"chapter": 3, "question_id": q["id"], "choice": q["correct"]})
    assert c.get(f"/api/players/{code}/wm/progress").json() == {"done": {"3": 2}}


def test_student_test_builds_only_the_chosen_formats_and_chapters():
    c = client()
    items = c.get("/api/wm/tests/build", params={"chapters": "38,40", "formats": "BC", "count": 20}).json()["items"]
    assert items, "fill-in chapters should give items"
    assert {i["format"] for i in items} <= {"B", "C"}
    assert {i["chapter"] for i in items} <= {38, 40}
    assert all("answer" not in i and "explanation" not in i for i in items)


def test_student_test_is_marked_on_the_server():
    c = client()
    items = c.get("/api/wm/tests/build", params={"chapters": "1", "formats": "A", "count": 3}).json()["items"]
    assert len(items) == 3
    qid = items[0]["id"].split("|")[0]
    question = content.wm_find_question(1, qid)
    right_letter = "ABCD"[question["correct"]]
    wrong_letter = "ABCD"[(question["correct"] + 1) % 4]
    graded = c.post("/api/wm/tests/grade", json={"items": [
        {"id": f"{qid}|A", "answer": right_letter},
        {"id": f"{qid}|A", "answer": wrong_letter},
        {"id": "not-a-question|A", "answer": "A"},
    ]}).json()
    assert [r["correct"] for r in graded["results"]] == [True, False, False]
    assert graded["score"] == 1 and graded["total"] == 3
    assert graded["results"][0]["expected"].startswith(f"{right_letter}. ")


def test_student_test_true_false_is_checked_against_the_word():
    c = client()
    items = c.get("/api/wm/tests/build", params={"chapters": "38,40,41", "formats": "C", "count": 5}).json()["items"]
    item = items[0]
    variant = item["id"].split("|")[2]
    expected = "True" if variant == "T" else "False"
    graded = c.post("/api/wm/tests/grade", json={"items": [{"id": item["id"], "answer": expected}]}).json()
    assert graded["results"][0]["correct"] is True
    wrong = "False" if expected == "True" else "True"
    graded = c.post("/api/wm/tests/grade", json={"items": [{"id": item["id"], "answer": wrong}]}).json()
    assert graded["results"][0]["correct"] is False


def test_student_test_rejects_bad_choices():
    c = client()
    assert c.get("/api/wm/tests/build", params={"chapters": "999"}).status_code == 404
    assert c.get("/api/wm/tests/build", params={"chapters": "x"}).status_code == 400
    assert c.get("/api/wm/tests/build", params={"formats": "Z"}).status_code == 400
