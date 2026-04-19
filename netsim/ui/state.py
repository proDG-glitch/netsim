"""Central application state."""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum, auto

from netsim.data.lessons import LESSONS
from netsim.data.text_content import ARCHITECTURE_ITEMS
from netsim.quiz.logic import (
    Difficulty,
    QuizQuestion,
    QuizResult,
    QuizSession,
    build_session,
    build_session_for_categories,
    categories_for,
)


class Screen(Enum):
    HOME = auto()
    LESSONS_MENU = auto()
    LESSON_DETAIL = auto()
    ARCHITECTURE = auto()
    QUIZ_TOPICS = auto()
    QUIZ_DIFFICULTY = auto()
    QUIZ_DETAIL = auto()
    SIMULATION = auto()
    SCENARIOS = auto()
    HELP = auto()


MAIN_MENU = (
    ("lessons", "LESSONS"),
    ("quit", "EXIT"),
)

LESSON_QUIZ_CATEGORIES: dict[str, tuple[str, ...]] = {
    "intro_wireless": ("Transmission Basics", "Wireless"),
    "types_topologies": ("Infrastructure", "Wireless"),
    "radio_signal_basics": ("Transmission Basics", "Signals", "Nyquist", "Shannon", "Modulation"),
    "wireless_propagation": ("Signals", "Transmission Basics", "Wireless"),
    "medium_access_control": ("MAC", "Wireless"),
    "mesh_routing": ("Wireless", "Infrastructure"),
    "wsn_iot": ("Wireless", "Infrastructure"),
    "short_range": ("Wireless", "Mobile Networks"),
    "wifi_networks": ("Wireless", "MAC"),
    "mobile_networks": ("Mobile Networks", "Wireless"),
}

DIFFICULTY_MENU: tuple[tuple[str, Difficulty | None], ...] = (
    ("ALL DIFFICULTIES", None),
    ("EASY", Difficulty.EASY),
    ("MEDIUM", Difficulty.MEDIUM),
    ("HARD", Difficulty.HARD),
)


@dataclass
class AppState:
    screen: Screen = Screen.HOME
    main_menu_index: int = 0
    lesson_index: int = 0
    architecture_index: int = 0
    quiz_category_index: int = 0
    quiz_difficulty_index: int = 0
    quiz_answer_index: int = 0
    quiz_selected_answers: set[int] = field(default_factory=set)
    quiz_feedback_visible: bool = False
    last_quiz_result: QuizResult | None = None
    quiz_session: QuizSession | None = None
    quiz_error: str | None = None
    quiz_questions: list[QuizQuestion] = field(default_factory=list)
    matrix_frame: int = 0
    previous_screen: Screen = Screen.HOME
    best_scores: dict[str, int] = field(default_factory=dict)
    rng: random.Random = field(default_factory=random.Random)

    def quiz_categories(self) -> list[str | None]:
        return [None, *categories_for(self.quiz_questions)]

    def current_lesson(self):
        return LESSONS[self.lesson_index]

    def current_question(self):
        if self.quiz_session is None or self.quiz_session.is_finished:
            return None
        return self.quiz_session.current_question

    def quiz_choice_count(self) -> int:
        question = self.current_question()
        if question is None:
            return 0
        return len(question.answers) + 1

    def submit_choice_index(self) -> int | None:
        question = self.current_question()
        if question is None:
            return None
        return len(question.answers)

    def current_architecture_item(self):
        return ARCHITECTURE_ITEMS[self.architecture_index]

    def current_menu_key(self) -> str:
        return MAIN_MENU[self.main_menu_index][0]

    def selected_quiz_category(self) -> str | None:
        categories = self.quiz_categories()
        if not categories:
            return None
        return categories[self.quiz_category_index]

    def selected_quiz_difficulty(self) -> Difficulty | None:
        return DIFFICULTY_MENU[self.quiz_difficulty_index][1]

    def selected_quiz_label(self) -> str:
        category = self.selected_quiz_category()
        return "RANDOM MIX" if category is None else category.upper()

    def selected_difficulty_label(self) -> str:
        return DIFFICULTY_MENU[self.quiz_difficulty_index][0]

    def quiz_score_percent(self) -> int:
        if self.quiz_session is None or self.quiz_session.completed == 0:
            return 0
        return round((self.quiz_session.score / self.quiz_session.completed) * 100)

    def quiz_best_key(self) -> str:
        if self.screen == Screen.LESSON_DETAIL:
            return f"lesson:{self.current_lesson().key}"
        category = self.selected_quiz_category() or "random_mix"
        difficulty = self.selected_quiz_difficulty()
        difficulty_key = difficulty.value if difficulty else "all"
        return f"quiz:{category}:{difficulty_key}"

    def quiz_best_score(self) -> int:
        return self.best_scores.get(self.quiz_best_key(), 0)

    def banner_key(self) -> str:
        if self.screen == Screen.HOME:
            return "NETSIM"
        if self.screen == Screen.LESSONS_MENU:
            return "LESSONS"
        if self.screen == Screen.LESSON_DETAIL:
            return self.current_lesson().ascii_header or self.current_lesson().title
        if self.screen == Screen.ARCHITECTURE:
            return "ARCHITECTURE"
        if self.screen in {Screen.QUIZ_TOPICS, Screen.QUIZ_DIFFICULTY, Screen.QUIZ_DETAIL}:
            return "QUIZ MODE"
        if self.screen == Screen.QUIZ_DETAIL:
            return "QUIZ MODE"
        if self.screen == Screen.SIMULATION:
            return "SIMULATION"
        if self.screen == Screen.SCENARIOS:
            return "SCENARIOS"
        return "HELP"

    def go_home(self) -> None:
        self.screen = Screen.HOME
        self.main_menu_index = 0
        self.previous_screen = Screen.HOME

    def go_back(self) -> None:
        if self.screen == Screen.LESSON_DETAIL:
            self.reset_active_quiz()
            self.screen = Screen.LESSONS_MENU
            return
        if self.screen == Screen.QUIZ_DETAIL:
            self.reset_active_quiz()
            self.screen = Screen.QUIZ_DIFFICULTY
            return
        if self.screen == Screen.QUIZ_DIFFICULTY:
            self.screen = Screen.QUIZ_TOPICS
            return
        if self.screen != Screen.HOME:
            self.screen = Screen.HOME
            self.main_menu_index = 0

    def move_up(self) -> None:
        if self.screen == Screen.HOME:
            self.main_menu_index = (self.main_menu_index - 1) % len(MAIN_MENU)
        elif self.screen == Screen.LESSONS_MENU:
            self.lesson_index = (self.lesson_index - 1) % len(LESSONS)
        elif self.screen == Screen.LESSON_DETAIL:
            choice_count = self.quiz_choice_count()
            if choice_count:
                self.quiz_answer_index = (self.quiz_answer_index - 1) % choice_count
        elif self.screen == Screen.ARCHITECTURE:
            self.architecture_index = (self.architecture_index - 1) % len(ARCHITECTURE_ITEMS)
        elif self.screen == Screen.QUIZ_TOPICS:
            categories = self.quiz_categories()
            if categories:
                self.quiz_category_index = (self.quiz_category_index - 1) % len(categories)
        elif self.screen == Screen.QUIZ_DIFFICULTY:
            self.quiz_difficulty_index = (self.quiz_difficulty_index - 1) % len(DIFFICULTY_MENU)
        elif self.screen == Screen.QUIZ_DETAIL:
            choice_count = self.quiz_choice_count()
            if choice_count:
                self.quiz_answer_index = (self.quiz_answer_index - 1) % choice_count

    def move_down(self) -> None:
        if self.screen == Screen.HOME:
            self.main_menu_index = (self.main_menu_index + 1) % len(MAIN_MENU)
        elif self.screen == Screen.LESSONS_MENU:
            self.lesson_index = (self.lesson_index + 1) % len(LESSONS)
        elif self.screen == Screen.LESSON_DETAIL:
            choice_count = self.quiz_choice_count()
            if choice_count:
                self.quiz_answer_index = (self.quiz_answer_index + 1) % choice_count
        elif self.screen == Screen.ARCHITECTURE:
            self.architecture_index = (self.architecture_index + 1) % len(ARCHITECTURE_ITEMS)
        elif self.screen == Screen.QUIZ_TOPICS:
            categories = self.quiz_categories()
            if categories:
                self.quiz_category_index = (self.quiz_category_index + 1) % len(categories)
        elif self.screen == Screen.QUIZ_DIFFICULTY:
            self.quiz_difficulty_index = (self.quiz_difficulty_index + 1) % len(DIFFICULTY_MENU)
        elif self.screen == Screen.QUIZ_DETAIL:
            choice_count = self.quiz_choice_count()
            if choice_count:
                self.quiz_answer_index = (self.quiz_answer_index + 1) % choice_count

    def open_selected(self) -> str | None:
        if self.screen == Screen.HOME:
            key = self.current_menu_key()
            if key == "lessons":
                self.previous_screen = self.screen
                self.screen = Screen.LESSONS_MENU
            elif key == "architecture":
                self.previous_screen = self.screen
                self.screen = Screen.ARCHITECTURE
            elif key == "quiz":
                self.previous_screen = self.screen
                self.screen = Screen.QUIZ_TOPICS
            elif key == "simulation":
                self.previous_screen = self.screen
                self.screen = Screen.SIMULATION
            elif key == "scenarios":
                self.previous_screen = self.screen
                self.screen = Screen.SCENARIOS
            elif key == "help":
                self.previous_screen = self.screen
                self.screen = Screen.HELP
            elif key == "quit":
                return "quit"
            return None
        if self.screen == Screen.LESSONS_MENU:
            self.start_lesson_quiz()
            self.screen = Screen.LESSON_DETAIL
            return None
        if self.screen == Screen.LESSON_DETAIL:
            if self.quiz_feedback_visible:
                return None
            self.confirm_quiz_choice()
            return None
        if self.screen == Screen.QUIZ_TOPICS:
            self.quiz_error = None
            self.screen = Screen.QUIZ_DIFFICULTY
            return None
        if self.screen == Screen.QUIZ_DIFFICULTY:
            self.start_quiz()
            return None
        if self.screen == Screen.QUIZ_DETAIL:
            if self.quiz_feedback_visible:
                return None
            self.confirm_quiz_choice()
            return None
        return None

    def confirm_quiz_choice(self) -> None:
        if self.quiz_answer_index == self.submit_choice_index():
            self.submit_quiz_answer()
            return
        self.toggle_quiz_answer()

    def select_number(self, number: int) -> str | None:
        if self.screen == Screen.LESSONS_MENU:
            lesson_number = 10 if number == 0 else number
            if 1 <= lesson_number <= len(LESSONS):
                self.lesson_index = lesson_number - 1
                self.start_lesson_quiz()
                self.screen = Screen.LESSON_DETAIL
            return None
        if number == 0:
            self.go_back()
            return None
        if self.screen in {Screen.LESSON_DETAIL, Screen.QUIZ_DETAIL}:
            question = self.current_question()
            if question is not None and 1 <= number <= len(question.answers):
                self.quiz_answer_index = number - 1
                self.toggle_quiz_answer()
        return None

    def start_lesson_quiz(self) -> None:
        self.quiz_error = None
        categories = set(LESSON_QUIZ_CATEGORIES.get(self.current_lesson().key, ()))
        try:
            self.quiz_session = build_session_for_categories(
                self.quiz_questions,
                categories=categories,
                rng=self.rng,
            )
        except ValueError as exc:
            self.quiz_session = None
            self.quiz_error = str(exc)
            return
        self.quiz_answer_index = 0
        self.quiz_selected_answers.clear()
        self.quiz_feedback_visible = False
        self.last_quiz_result = None

    def start_quiz(self) -> None:
        self.quiz_error = None
        try:
            self.quiz_session = build_session(
                self.quiz_questions,
                category=self.selected_quiz_category(),
                difficulty=self.selected_quiz_difficulty(),
                rng=self.rng,
            )
        except ValueError as exc:
            self.quiz_error = str(exc)
            return
        self.quiz_answer_index = 0
        self.quiz_selected_answers.clear()
        self.quiz_feedback_visible = True
        self.quiz_feedback_visible = False
        self.last_quiz_result = None
        self.screen = Screen.QUIZ_DETAIL

    def reset_active_quiz(self) -> None:
        self.quiz_session = None
        self.quiz_answer_index = 0
        self.quiz_selected_answers.clear()
        self.quiz_feedback_visible = False
        self.last_quiz_result = None

    def toggle_quiz_answer(self) -> None:
        if self.quiz_feedback_visible:
            return
        question = self.current_question()
        if question is None or self.quiz_answer_index >= len(question.answers):
            return
        if self.quiz_answer_index in self.quiz_selected_answers:
            self.quiz_selected_answers.remove(self.quiz_answer_index)
        else:
            self.quiz_selected_answers.add(self.quiz_answer_index)

    def submit_quiz_answer(self) -> None:
        if self.quiz_session is None or self.current_question() is None or not self.quiz_selected_answers:
            return
        self.last_quiz_result = self.quiz_session.submit(self.quiz_selected_answers)
        self.quiz_selected_answers = set()
        self.quiz_answer_index = 0
        self.quiz_feedback_visible = True

    def advance_after_feedback(self) -> None:
        if not self.quiz_feedback_visible or self.quiz_session is None:
            return
        if not self.quiz_session.is_finished:
            self.quiz_answer_index = 0
            self.quiz_selected_answers.clear()
            self.quiz_feedback_visible = False
            self.last_quiz_result = None
            return
        self.record_progress()
        if self.screen == Screen.LESSON_DETAIL:
            self.quiz_feedback_visible = False
            self.last_quiz_result = None
            return
        self.reset_active_quiz()
        self.screen = Screen.QUIZ_TOPICS

    def record_progress(self) -> None:
        if self.quiz_session is None or self.quiz_session.total == 0:
            return
        score = round((self.quiz_session.score / self.quiz_session.total) * 100)
        key = self.quiz_best_key()
        previous = self.best_scores.get(key, 0)
        if score > previous:
            self.best_scores[key] = score
