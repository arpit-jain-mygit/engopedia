"""Scoring rules. Kept as pure functions so they are easy to test and tune."""

POINTS_CORRECT = 10       # any correct answer
FIRST_TRY_BONUS = 5       # correct on the first attempt
STREAK_BONUS = 10         # every STREAK_EVERY first-try answers in a row
STREAK_EVERY = 3
CANDY_PER_CORRECT = 1     # one candy per question, never repeated

def score_answer(first_try, streak_before):
    """Return (points, candies, new_streak) for one correct answer."""
    if not first_try:
        return POINTS_CORRECT, CANDY_PER_CORRECT, 0
    streak = streak_before + 1
    points = POINTS_CORRECT + FIRST_TRY_BONUS
    if streak % STREAK_EVERY == 0:
        points += STREAK_BONUS
    return points, CANDY_PER_CORRECT, streak


def stars_for(first_try_correct, total):
    """1 to 3 stars, based on the share of questions answered right first time."""
    if total <= 0:
        return 1
    share = first_try_correct / total
    if share >= 0.8:
        return 3
    if share >= 0.5:
        return 2
    return 1


# Candies are kept per category. Word Wizard and Grammar earn them today. The Cambridge
# categories are listed so the app can show them, and stay at 0 until they earn candies.
def candies_by_category(player):
    return {"word_wizard": player.get("candies_ww", 0), "grammar": player.get("candies_wm", 0),
            "cambridge_maths": 0, "cambridge_english": 0}


def total_candies(player):
    return player.get("candies_ww", 0) + player.get("candies_wm", 0)


def spend_candies(player, price):
    """Shop purchases take candies from Word Wizard first, then from Grammar."""
    from_ww = min(player.get("candies_ww", 0), price)
    player["candies_ww"] = player.get("candies_ww", 0) - from_ww
    player["candies_wm"] = player.get("candies_wm", 0) - (price - from_ww)
