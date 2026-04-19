"""Command-line entrypoint for NetSim quiz mode."""

from __future__ import annotations

import argparse
import curses
import random
from pathlib import Path

from netsim.quiz.loader import QuestionLoadError, load_questions
from netsim.quiz.logic import build_session, categories_for
from netsim.quiz.ui import QuizUI


DEFAULT_QUESTIONS = Path("assets/quiz/questions.json")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the standalone NetSim terminal quiz.")
    parser.add_argument(
        "questions",
        nargs="?",
        default=DEFAULT_QUESTIONS,
        type=Path,
        help=f"Path to quiz JSON file. Defaults to {DEFAULT_QUESTIONS}.",
    )
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed for repeatable runs.")
    args = parser.parse_args()

    try:
        questions = load_questions(args.questions)
    except QuestionLoadError as exc:
        print(exc)
        return 1

    rng = random.Random(args.seed)

    def run(stdscr: curses.window) -> None:
        ui = QuizUI(stdscr)
        category = ui.choose_category(categories_for(questions))
        difficulty = ui.choose_difficulty()
        session = build_session(questions, category=category, difficulty=difficulty, rng=rng)
        ui.run_session(session)

    try:
        curses.wrapper(run)
    except KeyboardInterrupt:
        print("Quiz exited.")
    except ValueError as exc:
        print(exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

