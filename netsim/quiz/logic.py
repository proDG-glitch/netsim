"""Quiz rules, shuffling, scoring, and filtering."""

from __future__ import annotations

import random
from dataclasses import dataclass
from enum import Enum
from typing import TypeVar


T = TypeVar("T")


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


@dataclass(frozen=True)
class AnswerOption:
    text: str
    explanation: str
    is_correct: bool


@dataclass(frozen=True)
class QuizQuestion:
    category: str
    prompt: str
    explanation: str
    answers: tuple[str, ...]
    explanations: tuple[str, ...]
    correct: frozenset[int]

    @property
    def difficulty(self) -> Difficulty:
        correct_count = len(self.correct)
        if correct_count <= 1:
            return Difficulty.EASY
        if correct_count == 2:
            return Difficulty.MEDIUM
        return Difficulty.HARD

    def shuffled(self, rng: random.Random) -> "QuizQuestion":
        return randomize_question(self, rng)


@dataclass(frozen=True)
class QuizResult:
    question: QuizQuestion
    selected: frozenset[int]

    @property
    def is_correct(self) -> bool:
        return self.selected == self.question.correct


class QuizSession:
    def __init__(self, questions: list[QuizQuestion]) -> None:
        if not questions:
            raise ValueError("QuizSession needs at least one question.")
        self.questions = questions
        self.current_index = 0
        self.results: list[QuizResult] = []

    @property
    def total(self) -> int:
        return len(self.questions)

    @property
    def completed(self) -> int:
        return len(self.results)

    @property
    def score(self) -> int:
        return sum(1 for result in self.results if result.is_correct)

    @property
    def current_question(self) -> QuizQuestion:
        return self.questions[self.current_index]

    @property
    def is_finished(self) -> bool:
        return self.completed >= self.total

    def submit(self, selected: set[int]) -> QuizResult:
        result = QuizResult(question=self.current_question, selected=frozenset(selected))
        self.results.append(result)
        self.current_index += 1
        return result


def categories_for(questions: list[QuizQuestion]) -> list[str]:
    return sorted({question.category for question in questions})


def fisher_yates_shuffle(items: list[T], rng: random.Random) -> None:
    """Shuffle items in-place with unbiased O(n) Fisher-Yates."""

    for index in range(len(items) - 1, 0, -1):
        swap_index = rng.randrange(index + 1)
        items[index], items[swap_index] = items[swap_index], items[index]


def randomize_question(question: QuizQuestion, rng: random.Random | None = None) -> QuizQuestion:
    """Return a copy of question with answers shuffled and correct indices rebuilt."""

    rng = rng or random.Random()
    options = [
        AnswerOption(
            text=answer,
            explanation=question.explanations[index],
            is_correct=index in question.correct,
        )
        for index, answer in enumerate(question.answers)
    ]
    fisher_yates_shuffle(options, rng)

    answers = tuple(option.text for option in options)
    explanations = tuple(option.explanation for option in options)
    correct = frozenset(index for index, option in enumerate(options) if option.is_correct)
    return QuizQuestion(
        category=question.category,
        prompt=question.prompt,
        explanation=question.explanation,
        answers=answers,
        explanations=explanations,
        correct=correct,
    )


def build_session(
    questions: list[QuizQuestion],
    *,
    category: str | None,
    difficulty: Difficulty | None,
    rng: random.Random | None = None,
) -> QuizSession:
    rng = rng or random.Random()
    filtered = [
        question
        for question in questions
        if (category is None or question.category == category)
        and (difficulty is None or question.difficulty == difficulty)
    ]
    if not filtered:
        raise ValueError("No questions match that category and difficulty.")

    shuffled_questions = [randomize_question(question, rng) for question in filtered]
    fisher_yates_shuffle(shuffled_questions, rng)
    return QuizSession(shuffled_questions)


def build_session_for_categories(
    questions: list[QuizQuestion],
    *,
    categories: set[str],
    difficulty: Difficulty | None = None,
    rng: random.Random | None = None,
) -> QuizSession:
    rng = rng or random.Random()
    filtered = [
        question
        for question in questions
        if question.category in categories and (difficulty is None or question.difficulty == difficulty)
    ]
    if not filtered:
        raise ValueError("No questions match this lesson.")

    shuffled_questions = [randomize_question(question, rng) for question in filtered]
    fisher_yates_shuffle(shuffled_questions, rng)
    return QuizSession(shuffled_questions)
