import utils


def get_answer(types: list[str], answers: list[str]) -> str:
    """Return answer with highest score."""
    scores = get_scores(types, answers)
    return answers[scores.index(max(scores))]


def get_scores(types: list[str], answers: list[str]) -> list[int]:
    """Return scores for all answers."""
    if not (types and answers):
        raise ValueError

    # TODO: Implement this
    return [1] * len(answers)
