"""Textual app shell."""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static

from netsim.ui.headers import render_banner
from netsim.ui.state import AppState, Screen
from netsim.ui.views import content_for, sidebar_for


class NetSimApp(App):
    CSS = """
    Screen {
        background: #06111a;
        color: #d8efff;
    }

    #root {
        layout: vertical;
    }

    #banner {
        height: 12;
    }

    #body {
        height: 1fr;
    }

    #sidebar {
        width: 54;
        min-width: 54;
        margin-right: 1;
    }

    #content {
        width: 1fr;
        height: 1fr;
    }

    #footer {
        height: 1;
        color: #f6c66b;
        text-style: bold;
    }
    """

    BINDINGS = [
        ("up", "move_up", "UP"),
        ("down", "move_down", "DOWN"),
        ("enter", "confirm", "ENTER"),
        ("space", "toggle_answer", "TOGGLE"),
        ("backspace", "go_back", "BACK"),
        ("h", "go_home", "HOME"),
        ("b", "go_back", "BACK"),
        ("q", "quit_app", "QUIT"),
        ("0", "digit('0')", "ZERO"),
        ("1", "digit('1')", "ONE"),
        ("2", "digit('2')", "TWO"),
        ("3", "digit('3')", "THREE"),
        ("4", "digit('4')", "FOUR"),
    ]

    def __init__(
        self,
        state: AppState,
        score_path: Path,
        save_callback: Callable[[Path, dict[str, int]], None],
    ) -> None:
        super().__init__()
        self.state = state
        self.score_path = score_path
        self.save_callback = save_callback

    def compose(self) -> ComposeResult:
        yield Container(
            Static(id="banner"),
            Horizontal(
                Static(id="sidebar"),
                Static(id="content"),
                id="body",
            ),
            Static(id="footer"),
            id="root",
        )

    def on_mount(self) -> None:
        self.refresh_layout()
        self.set_interval(0.09, self.animate_matrix)

    def animate_matrix(self) -> None:
        self.state.matrix_frame += 1
        self.query_one("#content", Static).update(content_for(self.state))

    def action_move_up(self) -> None:
        self.state.move_up()
        self.refresh_layout()

    def action_move_down(self) -> None:
        self.state.move_down()
        self.refresh_layout()

    def action_confirm(self) -> None:
        if self.state.screen in {Screen.LESSON_DETAIL, Screen.QUIZ_DETAIL} and self.state.quiz_feedback_visible:
            self.state.advance_after_feedback()
        else:
            result = self.state.open_selected()
            if result == "quit":
                self.exit()
                return
        self.save_scores()
        self.refresh_layout()

    def action_toggle_answer(self) -> None:
        if self.state.screen in {Screen.LESSON_DETAIL, Screen.QUIZ_DETAIL}:
            self.state.toggle_quiz_answer()
            self.refresh_layout()

    def action_go_home(self) -> None:
        self.state.go_home()
        self.refresh_layout()

    def action_go_back(self) -> None:
        self.state.go_back()
        self.refresh_layout()

    def action_quit_app(self) -> None:
        if self.state.screen == Screen.HOME:
            self.exit()
            return
        self.state.go_back()
        self.refresh_layout()

    def action_digit(self, digit: str) -> None:
        self.state.select_number(int(digit))
        self.save_scores()
        self.refresh_layout()

    def refresh_layout(self) -> None:
        self.query_one("#banner", Static).update(render_banner(self.state.banner_key()))
        self.query_one("#sidebar", Static).update(sidebar_for(self.state))
        self.query_one("#content", Static).update(content_for(self.state))
        self.query_one("#footer", Static).update(self.footer_text())

    def footer_text(self) -> str:
        if self.state.screen == Screen.LESSONS_MENU:
            return "[Up/Down] Move  [Enter] Open Lesson  [1-9/0] Jump In  [Backspace/b/q] Back  [h] Home"
        if self.state.screen == Screen.LESSON_DETAIL:
            if self.state.quiz_feedback_visible:
                return "[Enter] Next  [Backspace/b/q] Back  [h] Home"
            if self.state.quiz_session is not None and self.state.quiz_session.is_finished:
                return "[Backspace/b/q] Back  [h] Home"
            return "[Up/Down] Move  [Enter] Select/Submit  [Space/1-4] Toggle  [Backspace/b/q] Back  [h] Home"
        if self.state.screen == Screen.QUIZ_DETAIL:
            if self.state.quiz_feedback_visible:
                return "[Enter] Next  [0/Backspace/b/q] Back  [h] Home"
            return "[Up/Down] Move  [Enter] Select/Submit  [Space/1-4] Toggle  [0/Backspace/b/q] Back  [h] Home"
        if self.state.screen == Screen.QUIZ_TOPICS:
            return "[Up/Down] Category  [Enter] Continue  [Backspace/b/q] Back  [h] Home"
        if self.state.screen == Screen.QUIZ_DIFFICULTY:
            return "[Up/Down] Difficulty  [Enter] Start  [Backspace/b/q] Back  [h] Home"
        return "[Up/Down] Move  [Enter] Open  [Backspace/b] Back  [h] Home  [q] Back/Quit"

    def save_scores(self) -> None:
        self.save_callback(self.score_path, self.state.best_scores)
