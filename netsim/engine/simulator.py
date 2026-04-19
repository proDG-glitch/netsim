"""Simulator bootstrapping."""

from __future__ import annotations

from pathlib import Path

from netsim.engine.persistence import load_scores, save_scores
from netsim.quiz.loader import QuestionLoadError, load_questions
from netsim.ui.app import NetSimApp
from netsim.ui.state import AppState


def run() -> None:
    root = Path(__file__).resolve().parents[2]
    score_path = root / "scores.json"
    question_path = root / "assets" / "quiz" / "questions.json"
    try:
        quiz_questions = load_questions(question_path)
    except QuestionLoadError:
        quiz_questions = []
    state = AppState(best_scores=load_scores(score_path), quiz_questions=quiz_questions)
    app = NetSimApp(state=state, score_path=score_path, save_callback=save_scores)
    app.run()
