"""Curses UI renderer for standalone quiz mode."""

from __future__ import annotations

import curses
import textwrap
from collections.abc import Sequence

from netsim.quiz.logic import Difficulty, QuizResult, QuizSession


HEADER = r"""
  ___  _   _ ___ ____   __  __  ___  ____  _____
 / _ \| | | |_ _|__  | |  \/  |/ _ \|  _ \| ____|
| | | | | | || |  / /  | |\/| | | | | | | |  _|
| |_| | |_| || | / /_  | |  | | |_| | |_| | |___
 \__\_\\___/|___|____| |_|  |_|\___/|____/|_____|
""".strip("\n")


class QuizUI:
    def __init__(self, stdscr: curses.window) -> None:
        self.stdscr = stdscr
        curses.curs_set(0)
        curses.use_default_colors()
        self.stdscr.keypad(True)

    def choose_category(self, categories: Sequence[str]) -> str | None:
        options = ["Random mix", *categories]
        choice = self._menu("Choose category", options)
        return None if choice == 0 else options[choice]

    def choose_difficulty(self) -> Difficulty | None:
        options = ["All difficulties", "Easy", "Medium", "Hard"]
        choice = self._menu("Choose difficulty", options)
        if choice == 0:
            return None
        return Difficulty(options[choice].lower())

    def run_session(self, session: QuizSession) -> None:
        while not session.is_finished:
            result = self._ask_question(session)
            self._show_result(session, result)
        self._show_summary(session)

    def _menu(self, title: str, options: Sequence[str]) -> int:
        selected = 0
        while True:
            self._clear()
            row = self._draw_header()
            row = self._add_wrapped(row + 1, title, curses.A_BOLD)
            row += 1
            for index, option in enumerate(options):
                marker = ">" if index == selected else " "
                attr = curses.A_REVERSE if index == selected else curses.A_NORMAL
                self._add_line(row, f"{marker} {option}", attr)
                row += 1
            self._add_footer("Up/Down move  Enter select  q quit")
            key = self.stdscr.getch()
            if key in (curses.KEY_UP, ord("k")):
                selected = (selected - 1) % len(options)
            elif key in (curses.KEY_DOWN, ord("j")):
                selected = (selected + 1) % len(options)
            elif key in (curses.KEY_ENTER, 10, 13):
                return selected
            elif key in (ord("q"), ord("Q")):
                raise KeyboardInterrupt

    def _ask_question(self, session: QuizSession) -> QuizResult:
        question = session.current_question
        selected_answer = 0
        selected_answers: set[int] = set()

        while True:
            self._clear()
            row = self._draw_header()
            row = self._draw_progress(row + 1, session.completed, session.total)
            row = self._add_wrapped(row + 1, f"{question.category} - {question.difficulty.value}", curses.A_DIM)
            row = self._add_wrapped(row + 1, question.prompt, curses.A_BOLD)
            row += 1

            for index, answer in enumerate(question.answers):
                cursor = ">" if index == selected_answer else " "
                check = "x" if index in selected_answers else " "
                attr = curses.A_REVERSE if index == selected_answer else curses.A_NORMAL
                row = self._add_wrapped(row, f"{cursor} ({check}) {answer}", attr, indent=4)

            self._add_footer("Up/Down move  Space toggle  Enter submit  q quit")
            key = self.stdscr.getch()
            if key in (curses.KEY_UP, ord("k")):
                selected_answer = (selected_answer - 1) % len(question.answers)
            elif key in (curses.KEY_DOWN, ord("j")):
                selected_answer = (selected_answer + 1) % len(question.answers)
            elif key == ord(" "):
                if selected_answer in selected_answers:
                    selected_answers.remove(selected_answer)
                else:
                    selected_answers.add(selected_answer)
            elif key in (curses.KEY_ENTER, 10, 13) and selected_answers:
                return session.submit(selected_answers)
            elif key in (ord("q"), ord("Q")):
                raise KeyboardInterrupt

    def _show_result(self, session: QuizSession, result: QuizResult) -> None:
        self._clear()
        row = self._draw_header()
        row = self._draw_progress(row + 1, session.completed, session.total)
        verdict = "CORRECT" if result.is_correct else "INCORRECT"
        row = self._add_wrapped(row + 1, verdict, curses.A_BOLD)
        row = self._add_wrapped(row + 1, f"Score: {session.score}/{session.completed}")
        row += 1
        row = self._add_wrapped(row, "Correct answer set:", curses.A_BOLD)
        for index in sorted(result.question.correct):
            row = self._add_wrapped(row, f"- {result.question.answers[index]}", indent=2)
        if not result.is_correct:
            row += 1
            row = self._add_wrapped(row, "Your answer set:", curses.A_BOLD)
            if result.selected:
                for index in sorted(result.selected):
                    row = self._add_wrapped(row, f"- {result.question.answers[index]}", indent=2)
            else:
                row = self._add_wrapped(row, "- No answer selected", indent=2)
        self._add_footer("Enter continue  q quit")
        self._wait_for_enter()

    def _show_summary(self, session: QuizSession) -> None:
        self._clear()
        row = self._draw_header()
        row = self._draw_progress(row + 1, session.total, session.total)
        row = self._add_wrapped(row + 1, "Quiz complete", curses.A_BOLD)
        self._add_wrapped(row + 1, f"Final score: {session.score}/{session.total}", curses.A_BOLD)
        self._add_footer("Enter exit")
        self._wait_for_enter(allow_quit=False)

    def _draw_header(self) -> int:
        row = 0
        for line in HEADER.splitlines():
            self._add_line(row, line, curses.A_BOLD)
            row += 1
        return row

    def _draw_progress(self, row: int, completed: int, total: int) -> int:
        _, width = self.stdscr.getmaxyx()
        bar_width = max(1, width - 1)
        filled = 0 if total == 0 else round((completed / total) * bar_width)
        bar = "#" * filled + "-" * (bar_width - filled)
        self._add_line(row, bar)
        return row + 1

    def _wait_for_enter(self, *, allow_quit: bool = True) -> None:
        while True:
            key = self.stdscr.getch()
            if key in (curses.KEY_ENTER, 10, 13):
                return
            if allow_quit and key in (ord("q"), ord("Q")):
                raise KeyboardInterrupt

    def _clear(self) -> None:
        self.stdscr.erase()

    def _add_footer(self, text: str) -> None:
        height, _ = self.stdscr.getmaxyx()
        self._add_line(height - 1, text, curses.A_DIM)
        self.stdscr.refresh()

    def _add_wrapped(self, row: int, text: str, attr: int = curses.A_NORMAL, *, indent: int = 0) -> int:
        _, width = self.stdscr.getmaxyx()
        wrap_width = max(10, width - indent - 1)
        for line in textwrap.wrap(text, width=wrap_width) or [""]:
            self._add_line(row, (" " * indent) + line, attr)
            row += 1
        return row

    def _add_line(self, row: int, text: str, attr: int = curses.A_NORMAL) -> None:
        height, width = self.stdscr.getmaxyx()
        if 0 <= row < height:
            self.stdscr.addnstr(row, 0, text, max(0, width - 1), attr)

