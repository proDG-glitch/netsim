"""JSON question loading for NetSim quiz mode."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from netsim.quiz.logic import QuizQuestion


class QuestionLoadError(ValueError):
    """Raised when a quiz JSON file has an invalid shape."""


def load_questions(path: str | Path) -> list[QuizQuestion]:
    """Load and validate quiz questions from a JSON file."""

    question_path = Path(path)
    try:
        raw_items = json.loads(question_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise QuestionLoadError(f"Could not read quiz file: {question_path}") from exc
    except json.JSONDecodeError as exc:
        raise QuestionLoadError(f"Invalid JSON in quiz file: {question_path}") from exc

    if not isinstance(raw_items, list):
        raise QuestionLoadError("Quiz file must contain a JSON array of questions.")

    questions: list[QuizQuestion] = []
    for index, item in enumerate(raw_items, start=1):
        questions.append(_parse_question(item, index))
    if not questions:
        raise QuestionLoadError("Quiz file does not contain any questions.")
    return questions


def _parse_question(item: Any, index: int) -> QuizQuestion:
    if not isinstance(item, dict):
        raise QuestionLoadError(f"Question {index} must be an object.")

    category = _required_string(item, "category", index)
    prompt = _required_string(item, "question", index)
    question_explanation = item.get("explanation", "")
    answers = item.get("answers")
    correct = item.get("correct")
    explanations = item.get("explanations", item.get("option_explanations"))

    if not isinstance(answers, list) or not answers:
        raise QuestionLoadError(f"Question {index} must have a non-empty answers array.")
    if not isinstance(question_explanation, str):
        raise QuestionLoadError(f"Question {index} explanation must be a string.")
    if not all(isinstance(answer, str) and answer.strip() for answer in answers):
        raise QuestionLoadError(f"Question {index} answers must be non-empty strings.")
    if explanations is None:
        explanations = [""] * len(answers)
    if not isinstance(explanations, list) or len(explanations) != len(answers):
        raise QuestionLoadError(f"Question {index} explanations must match the answers array length.")
    if not all(isinstance(explanation, str) for explanation in explanations):
        raise QuestionLoadError(f"Question {index} explanations must be strings.")
    if not isinstance(correct, list) or not correct:
        raise QuestionLoadError(f"Question {index} must have a non-empty correct array.")
    if not all(isinstance(answer_index, int) for answer_index in correct):
        raise QuestionLoadError(f"Question {index} correct values must be integer indices.")

    answer_count = len(answers)
    correct_set = frozenset(correct)
    invalid_indices = sorted(answer_index for answer_index in correct_set if answer_index < 0 or answer_index >= answer_count)
    if invalid_indices:
        raise QuestionLoadError(f"Question {index} has out-of-range correct indices: {invalid_indices}.")

    return QuizQuestion(
        category=category.strip(),
        prompt=prompt.strip(),
        explanation=question_explanation.strip(),
        answers=tuple(answer.strip() for answer in answers),
        explanations=tuple(explanation.strip() for explanation in explanations),
        correct=correct_set,
    )


def _required_string(item: dict[str, Any], key: str, index: int) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value.strip():
        raise QuestionLoadError(f"Question {index} must have a non-empty {key!r} string.")
    return value
