"""Rich/Textual views and custom widgets."""

from __future__ import annotations

import random
from pathlib import Path

from rich.align import Align
from rich.columns import Columns
from rich.console import Console, ConsoleOptions, Group, RenderableType, RenderResult
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual.widget import Widget

from netsim.data.lessons import LESSONS
from netsim.data.text_content import (
    ARCHITECTURE_ITEMS,
    HELP_TEXT,
    SCENARIOS_TEXT,
    SIMULATION_TEXT,
)
from netsim.ui.headers import pixel_text
from netsim.ui.state import DIFFICULTY_MENU, MAIN_MENU, AppState, Screen


LESSONS_LIST_HEIGHT = len(LESSONS) + 6
LESSONS_MENU_TOTAL_HEIGHT = LESSONS_LIST_HEIGHT + 7 + 14
LESSONS_PERCENT_HEIGHT = LESSONS_MENU_TOTAL_HEIGHT - LESSONS_LIST_HEIGHT
NETSIM_LOGO = (
    Path(__file__).resolve().parents[2] / "assets" / "ascii" / "netsim_logo.txt"
).read_text(encoding="utf-8").strip("\n")
PERCENT_GLYPHS = {
    "1": [
        " ████",
        "▒▒███",
        " ▒███",
        " ▒███",
        " ▒███",
        " ▒███",
        " █████",
        "▒▒▒▒▒",
    ],
    "2": [
        "  ████████",
        " ███▒▒▒▒███",
        "▒▒▒    ▒███",
        "   ███████",
        "  ███▒▒▒▒",
        " ███      █",
        "▒██████████",
        "▒▒▒▒▒▒▒▒▒▒",
    ],
    "3": [
        "  ████████",
        " ███▒▒▒▒███",
        "▒▒▒    ▒███",
        "   ██████▒",
        "  ▒▒▒▒▒▒███",
        " ███   ▒███",
        "▒▒████████",
        " ▒▒▒▒▒▒▒▒",
    ],
    "4": [
        " █████ █████",
        "▒▒███ ▒▒███",
        " ▒███  ▒███ █",
        " ▒███████████",
        " ▒▒▒▒▒▒▒███▒█",
        "       ▒███▒",
        "       █████",
        "      ▒▒▒▒▒",
    ],
    "5": [
        " ██████████",
        "▒███▒▒▒▒▒▒█",
        "▒███     ▒",
        "▒█████████",
        "▒▒▒▒▒▒▒▒███",
        " ███   ▒███",
        "▒▒████████",
        " ▒▒▒▒▒▒▒▒",
    ],
    "6": [
        "  ████████",
        " ███▒▒▒▒███",
        "▒███   ▒▒▒",
        "▒█████████",
        "▒███▒▒▒▒███",
        "▒███   ▒███",
        "▒▒████████",
        " ▒▒▒▒▒▒▒▒",
    ],
    "7": [
        " ██████████",
        "▒███▒▒▒▒███",
        "▒▒▒    ███",
        "      ███",
        "     ███",
        "    ███",
        "   ███",
        "  ▒▒▒",
    ],
    "8": [
        "  ████████",
        " ███▒▒▒▒███",
        "▒███   ▒███",
        "▒▒████████",
        " ███▒▒▒▒███",
        "▒███   ▒███",
        "▒▒████████",
        " ▒▒▒▒▒▒▒▒",
    ],
    "9": [
        "  ████████",
        " ███▒▒▒▒███",
        "▒███   ▒███",
        "▒▒█████████",
        " ▒▒▒▒▒▒▒███",
        " ███   ▒███",
        "▒▒████████",
        " ▒▒▒▒▒▒▒▒",
    ],
    "0": [
        "    █████",
        "  ███▒▒▒███",
        " ███   ▒▒███",
        "▒███    ▒███",
        "▒███    ▒███",
        "▒▒███   ███",
        " ▒▒▒█████▒",
        "   ▒▒▒▒▒▒",
    ],
    "%": [
        " ███    ███",
        "▒███   ▒███",
        "     ▒███",
        "    ███▒",
        "  ▒███",
        " ███▒",
        "▒███   ▒███",
        " ▒▒▒    ▒▒▒",
    ],
}


def render_percentage_badge(value: int) -> Panel:
    percent_text = f"{max(0, min(999, value))}%"
    rows = [""] * 8
    for index, char in enumerate(percent_text):
        glyph = PERCENT_GLYPHS[char]
        glyph_width = max(len(line) for line in glyph)
        next_char = percent_text[index + 1] if index + 1 < len(percent_text) else ""
        spacer = "   " if char.isdigit() and next_char == "%" else "  "
        for row_index, glyph_row in enumerate(glyph):
            rows[row_index] += glyph_row.ljust(glyph_width)
            if next_char:
                rows[row_index] += spacer
    badge = Text("\n".join(rows), style="#9fe7ff bold")
    return Panel(
        Align.center(badge, vertical="middle"),
        title="BEST SCORE",
        border_style="#53b4ff",
        padding=(1, 1),
        height=LESSONS_PERCENT_HEIGHT,
    )


class ArchitectureDiagram(Widget):
    def __init__(self, selected_key: str) -> None:
        super().__init__()
        self.selected_key = selected_key

    def box(self, label: str, key: str, border: str, style: str = "#d8efff") -> Panel:
        active = key == self.selected_key or (
            self.selected_key == "pod" and key in {"pod_a", "pod_b"}
        ) or (
            self.selected_key == "kubelet" and key in {"kubelet_1", "kubelet_2"}
        ) or (
            self.selected_key == "kube_proxy" and key in {"kube_proxy_1", "kube_proxy_2"}
        )
        return Panel(
            Align.center(Text(label, style=style if not active else "#05111d bold"), vertical="middle"),
            border_style="#8fe0ff" if active else border,
            style="on #8fe0ff" if active else "",
            padding=(1, 1),
        )

    def render(self) -> RenderableType:
        control_plane = Table.grid(expand=True)
        for _ in range(4):
            control_plane.add_column(ratio=1)
        control_plane.add_row(
            self.box("API", "api_server", "#53b4ff"),
            self.box("SCHEDULER", "scheduler", "#53b4ff"),
            self.box("CONTROLLER", "controller_manager", "#53b4ff"),
            self.box("ETCD", "etcd", "#53b4ff"),
        )

        worker_one = Group(
            Text("WORKER NODE 1", style="#d8efff bold"),
            self.box("POD A", "pod_a", "#e0b75f"),
            Columns(
                [
                    self.box("KUBELET", "kubelet_1", "#57d18a"),
                    self.box("KUBE-PROXY", "kube_proxy_1", "#57d18a"),
                ],
                equal=True,
                expand=True,
            ),
        )
        worker_two = Group(
            Text("WORKER NODE 2", style="#d8efff bold"),
            self.box("POD B", "pod_b", "#e0b75f"),
            Columns(
                [
                    self.box("KUBELET", "kubelet_2", "#57d18a"),
                    self.box("KUBE-PROXY", "kube_proxy_2", "#57d18a"),
                ],
                equal=True,
                expand=True,
            ),
        )
        workers = Columns(
            [
                Panel(worker_one, border_style="#57d18a", padding=(1, 1)),
                Panel(worker_two, border_style="#57d18a", padding=(1, 1)),
            ],
            equal=True,
            expand=True,
            padding=0,
        )
        return Group(
            Panel(control_plane, title="CONTROL PLANE", border_style="#53b4ff", padding=(1, 1)),
            Panel(workers, title="WORKER NODES", border_style="#57d18a", padding=(1, 1)),
        )


class AsciiProgressBar(Widget):
    def __init__(self, current: int, total: int) -> None:
        super().__init__()
        self.current = current
        self.total = total

    def render(self) -> RenderableType:
        total_slots = 24
        filled = 0 if self.total == 0 else round((self.current / self.total) * total_slots)
        top = "╔" + ("═" * total_slots) + "╗"
        middle = "║" + ("█" * filled) + (" " * (total_slots - filled)) + "║"
        bottom = "╚" + ("═" * total_slots) + "╝"
        label = f"{self.current}/{self.total}"
        body = Text("\n".join([top, middle, bottom, label]), style="#8fe0ff bold")
        return Panel(Align.center(body), title="PROGRESS", border_style="#53b4ff")


class FullWidthProgressBar:
    def __init__(self, completed: int, total: int) -> None:
        self.completed = completed
        self.total = total

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        width = max(1, options.max_width)
        filled = 0 if self.total == 0 else round((self.completed / self.total) * width)
        yield Text(("#" * filled) + ("-" * (width - filled)), style="#8fe0ff bold")


class MatrixRain:
    CHARS = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝ0123456789"

    def __init__(self, frame: int) -> None:
        self.frame = frame

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        width = max(8, options.max_width - 1)
        height = max(4, getattr(options, "height", None) or LESSONS_MENU_TOTAL_HEIGHT - 4)
        row_chars = [[" " for _ in range(width)] for _ in range(height)]
        row_styles = [["" for _ in range(width)] for _ in range(height)]
        stream_count = max(4, width // 4)
        motion_frame = self.frame // 2
        shimmer = self.frame % 4

        for stream_id in range(stream_count):
            rng = random.Random(stream_id * 8191)
            column = min(width - 1, (stream_id * 4) + rng.randrange(0, 2))
            speed = 1
            length = rng.randrange(max(7, height // 3), max(8, min(height, height // 2 + 8)))
            offset = rng.randrange(height * 2)
            cycle = height + (length * 2)
            base_head = ((motion_frame * speed) + offset) % cycle - length

            for head in (base_head, base_head - (cycle // 2)):
                for trail_index in range(length):
                    y = head - trail_index
                    if not 0 <= y < height:
                        continue
                    char_rng = random.Random((self.frame // 6) + stream_id * 101 + y * 17)
                    char = char_rng.choice(self.CHARS)
                    age = max(0.0, min(1.0, (trail_index - (shimmer * 0.18)) / max(1, length - 1)))
                    if trail_index == 0 and shimmer in {0, 1}:
                        style = "#f7fbff bold"
                    elif age < 0.3:
                        style = "#8fe0ff bold"
                    elif age < 0.66:
                        style = "#2f8fb8"
                    else:
                        style = "#123d52 dim"
                    row_chars[y][column] = char
                    row_styles[y][column] = style

        for y in range(height):
            row = Text()
            for char, style in zip(row_chars[y], row_styles[y], strict=True):
                row.append(char, style=style)
            row.no_wrap = True
            row.overflow = "crop"
            yield row


def menu_panel(state: AppState) -> Panel:
    lines = Text()
    for index, (_, label) in enumerate(MAIN_MENU):
        style = "#04101b on #8fe0ff bold" if index == state.main_menu_index else "#d8efff"
        prefix = ">" if index == state.main_menu_index else " "
        lines.append(f"{prefix} {label}\n", style=style)
    return Panel(lines, title="MAIN MENU", border_style="#53b4ff", padding=(1, 1))


def home_info_panel(state: AppState) -> Panel:
    key = state.current_menu_key()
    descriptions = {
        "lessons": "Start the structured wireless-network lessons with built-in JSON-backed quizzes.",
        "quit": "Exit the simulator.",
    }
    return Panel(Text(descriptions[key].upper(), style="#d8efff"), title="INFO", border_style="#53b4ff", padding=(1, 1))


def architecture_sidebar(state: AppState) -> Group:
    item = state.current_architecture_item()
    lines = Text()
    for index, architecture_item in enumerate(ARCHITECTURE_ITEMS):
        style = "#04101b on #8fe0ff bold" if index == state.architecture_index else "#d8efff"
        prefix = ">" if index == state.architecture_index else " "
        lines.append(f"{prefix} {architecture_item['label']}\n", style=style)
    return Group(
        Panel(lines, title="COMPONENTS", border_style="#53b4ff", padding=(1, 1)),
        Panel(Align.center(pixel_text("NET"), vertical="middle"), border_style="#53b4ff", padding=(0, 1)),
        Panel(Text(item["role"].upper(), style="#d8efff"), title="ROLE", border_style="#53b4ff", padding=(1, 1)),
        Panel(Text(item["details"].upper(), style="#d8efff"), title=item["label"], border_style="#53b4ff", padding=(1, 1)),
    )


def lessons_sidebar(state: AppState) -> Group:
    lines = Text()
    for index, item in enumerate(LESSONS):
        style = "#04101b on #8fe0ff bold" if index == state.lesson_index else "#d8efff"
        prefix = ">" if index == state.lesson_index else " "
        lines.append(f"{prefix} {item.title}\n", style=style)
    return Group(
        Panel(
            lines,
            title="LESSONS",
            border_style="#53b4ff",
            padding=(1, 1),
            height=LESSONS_LIST_HEIGHT,
        ),
        render_percentage_badge(state.lesson_best_score()),
    )


def lessons_content(state: AppState) -> RenderableType:
    lesson = state.current_lesson()
    preview_text = Text()
    preview_text.append(f"{lesson.title}\n\n", style="#8fe0ff bold")
    preview_text.append(lesson.preview.upper())
    preview_text.append("\n\nPRESS ENTER TO OPEN THIS LESSON.")
    return Panel(
        preview_text,
        title="LESSON PREVIEW",
        border_style="#53b4ff",
        padding=(1, 2),
        height=LESSONS_MENU_TOTAL_HEIGHT,
    )


def lesson_detail_sidebar(state: AppState) -> Panel:
    lesson = state.current_lesson()
    text = Text()
    text.append(f"{lesson.title}\n\n", style="#8fe0ff bold")
    text.append(lesson.description.upper())
    text.append("\n\nYOU ARE INSIDE THIS LESSON.")
    text.append("\nBACKSPACE, B, OR Q RETURNS TO THE LESSON LIST.")
    return Panel(text, title="LESSON INFO", border_style="#53b4ff", padding=(1, 1))


def lesson_detail_content(state: AppState) -> RenderableType:
    return lesson_quiz_panel(state)


QUESTION_PANEL_HEIGHT = LESSONS_MENU_TOTAL_HEIGHT // 2
EXPLANATION_PANEL_HEIGHT = LESSONS_MENU_TOTAL_HEIGHT - QUESTION_PANEL_HEIGHT


def stacked_quiz_windows(question: RenderableType, explanation: RenderableType, *, explanation_title: str = "") -> Group:
    return Group(
        Panel(
            question,
            title="QUESTION",
            border_style="#53b4ff",
            padding=(1, 2),
            height=QUESTION_PANEL_HEIGHT,
        ),
        Panel(
            explanation,
            title=explanation_title,
            border_style="#53b4ff",
            padding=(1, 2),
            height=EXPLANATION_PANEL_HEIGHT,
        ),
    )


def with_matrix_right(left: RenderableType, matrix_frame: int) -> Table:
    layout = Table.grid(expand=True)
    layout.add_column(ratio=1)
    layout.add_column(ratio=1)
    layout.add_row(
        left,
        Panel(
            MatrixRain(matrix_frame),
            title="",
            border_style="#53b4ff",
            padding=(1, 2),
            height=LESSONS_MENU_TOTAL_HEIGHT,
        ),
    )
    return layout


def lesson_quiz_panel(state: AppState) -> RenderableType:
    session = state.quiz_session
    if session is None:
        message = state.quiz_error or "No quiz questions are mapped for this lesson."
        return stacked_quiz_windows(Text(message.upper(), style="#f6c66b bold"), Text(""))
    if session.is_finished and not state.quiz_feedback_visible:
        score = round((session.score / session.total) * 100) if session.total else 0
        text = Text()
        text.append("QUIZ COMPLETE\n\n", style="#8fe0ff bold")
        text.append(f"SCORE: {session.score}/{session.total}\n")
        text.append(f"PERCENT: {score}%\n\n")
        text.append("BACKSPACE, B, OR Q RETURNS TO THE LESSON LIST.")
        return stacked_quiz_windows(text, Text(""))

    result = state.last_quiz_result
    question = result.question if state.quiz_feedback_visible and result else state.current_question()
    if question is None:
        return stacked_quiz_windows(Text("QUIZ COMPLETE.", style="#d8efff"), Text(""))

    prompt = Text()
    prompt.append(f"{question.prompt.upper()}\n\n", style="#d8efff bold")

    for index, answer in enumerate(question.answers):
        selected = index in (result.selected if state.quiz_feedback_visible and result else state.quiz_selected_answers)
        correct = state.quiz_feedback_visible and index in question.correct
        if state.quiz_feedback_visible:
            if correct:
                style = "#04101b on #57d18a bold"
            elif selected:
                style = "#ffffff on #b84a4a bold"
            else:
                style = "#d8efff"
            prefix = " "
        else:
            if index == state.quiz_answer_index:
                style = "#04101b on #8fe0ff bold"
            elif selected:
                style = "#04101b on #6fc7e8"
            else:
                style = "#d8efff"
            prefix = ">" if index == state.quiz_answer_index else " "
        prompt.append(f"{prefix} {answer}\n", style=style)

    if not state.quiz_feedback_visible:
        submit_index = len(question.answers)
        style = "#04101b on #8fe0ff bold" if state.quiz_answer_index == submit_index else "#8fe0ff bold"
        prefix = ">" if state.quiz_answer_index == submit_index else " "
        prompt.append(f"{prefix} SUBMIT\n", style=style)

    if state.quiz_feedback_visible and result:
        prompt.append("\n")
        prompt.append("CORRECT\n\n" if result.is_correct else "INCORRECT\n\n", style="#57d18a bold" if result.is_correct else "#f6c66b bold")
        prompt.append(f"SCORE: {session.score}/{session.completed}\n")
        prompt.append(f"QUESTION: {session.completed}/{session.total}\n\n")
        prompt.append("CORRECT SET:\n", style="#8fe0ff bold")
        for index in sorted(question.correct):
            prompt.append(f"- {question.answers[index]}\n")
        prompt.append("\nPRESS ENTER TO CONTINUE.")
    else:
        prompt.append("\n")
        prompt.append(
            f"QUESTION: {session.completed + 1}/{session.total}   SCORE: {session.score}/{session.completed}\n",
            style="#8fe0ff bold",
        )
        prompt.append("SPACE TOGGLES, ENTER SUBMITS.")

    explanations = Text()
    submitted = state.quiz_feedback_visible and result
    if submitted:
        if question.explanation:
            explanations.append(f"{question.explanation}\n\n", style="#d8efff bold")
        else:
            explanations.append("NO GENERAL EXPLANATION AVAILABLE.\n\n", style="#d8efff")
        for index, answer in enumerate(question.answers):
            correct = index in question.correct
            style = "#57d18a bold" if correct else "#f08a8a bold"
            explanations.append(f"{answer}\n", style=style)
            explanations.append(f"{question.explanations[index]}\n\n", style="#d8efff")

    left = stacked_quiz_windows(prompt, explanations, explanation_title="EXPLANATION")
    return left


def quiz_topics_sidebar(state: AppState) -> Group:
    lines = Text()
    categories = state.quiz_categories()
    for index, category in enumerate(categories):
        label = "RANDOM MIX" if category is None else category.upper()
        style = "#04101b on #8fe0ff bold" if index == state.quiz_category_index else "#d8efff"
        prefix = ">" if index == state.quiz_category_index else " "
        lines.append(f"{prefix} {label}\n", style=style)
    selected = state.selected_quiz_label()
    return Group(
        Panel(lines, title="CATEGORIES", border_style="#53b4ff", padding=(1, 1)),
        Panel(Text(f"SELECTED: {selected}\n\nQUESTIONS LOADED: {len(state.quiz_questions)}", style="#d8efff"), title="QUIZ MODE", border_style="#53b4ff", padding=(1, 1)),
        Panel(Align.center(pixel_text("QUIZ"), vertical="middle"), title="MODE", border_style="#53b4ff", padding=(1, 1)),
    )


def quiz_topics_content(state: AppState) -> RenderableType:
    text = Text()
    text.append("QUIZ MODE\n\n", style="#8fe0ff bold")
    if not state.quiz_questions:
        text.append("NO JSON QUESTIONS WERE LOADED.\n")
        text.append("CHECK ASSETS/QUIZ/QUESTIONS.JSON.")
    else:
        text.append("CHOOSE A CATEGORY OR RANDOM MIX.\n\n")
        text.append("QUESTIONS AND ANSWERS ARE SHUFFLED EACH RUN.\n")
        text.append("SOME QUESTIONS HAVE MULTIPLE CORRECT ANSWERS.\n\n")
        text.append("PRESS ENTER TO CHOOSE DIFFICULTY.")
    return Columns(
        [
            Panel(text, border_style="#53b4ff", padding=(1, 2)),
            Panel(
                Align.center(pixel_text(state.selected_quiz_label()[:4]), vertical="middle"),
                title="CATEGORY",
                border_style="#53b4ff",
                padding=(4, 2),
            ),
        ],
        equal=True,
        expand=True,
    )


def quiz_difficulty_sidebar(state: AppState) -> Group:
    lines = Text()
    for index, (label, _) in enumerate(DIFFICULTY_MENU):
        style = "#04101b on #8fe0ff bold" if index == state.quiz_difficulty_index else "#d8efff"
        prefix = ">" if index == state.quiz_difficulty_index else " "
        lines.append(f"{prefix} {label}\n", style=style)
    return Group(
        Panel(lines, title="DIFFICULTY", border_style="#53b4ff", padding=(1, 1)),
        Panel(Text(f"CATEGORY: {state.selected_quiz_label()}\nBEST SCORE: {state.quiz_best_score()}%", style="#d8efff"), title="SELECTION", border_style="#53b4ff", padding=(1, 1)),
    )


def quiz_difficulty_content(state: AppState) -> RenderableType:
    text = Text()
    text.append("READY CHECK\n\n", style="#8fe0ff bold")
    text.append(f"CATEGORY: {state.selected_quiz_label()}\n")
    text.append(f"DIFFICULTY: {state.selected_difficulty_label()}\n\n")
    text.append("EASY = ONE CORRECT ANSWER\n")
    text.append("MEDIUM = TWO CORRECT ANSWERS\n")
    text.append("HARD = THREE OR MORE CORRECT ANSWERS\n\n")
    if state.quiz_error:
        text.append(f"{state.quiz_error.upper()}\n\n", style="#f6c66b bold")
    text.append("PRESS ENTER TO START.")
    return Panel(text, title="QUIZ SETUP", border_style="#53b4ff", padding=(1, 2))


def quiz_detail_content(state: AppState) -> RenderableType:
    session = state.quiz_session
    result = state.last_quiz_result
    question = result.question if state.quiz_feedback_visible and result else state.current_question()
    if session is None or question is None:
        return Panel(Text("NO ACTIVE QUIZ SESSION.", style="#d8efff"), title="QUIZ", border_style="#53b4ff", padding=(1, 2))

    options = Text()
    for index, option in enumerate(question.answers):
        selected = index in (result.selected if state.quiz_feedback_visible and result else state.quiz_selected_answers)
        correct = state.quiz_feedback_visible and index in question.correct
        if state.quiz_feedback_visible:
            if correct:
                style = "#04101b on #57d18a bold"
            elif selected:
                style = "#ffffff on #b84a4a bold"
            else:
                style = "#d8efff"
            prefix = " "
        else:
            if index == state.quiz_answer_index:
                style = "#04101b on #8fe0ff bold"
            elif selected:
                style = "#04101b on #6fc7e8"
            else:
                style = "#d8efff"
            prefix = ">" if index == state.quiz_answer_index else " "
        options.append(f"{prefix} {option}\n", style=style)
    if not state.quiz_feedback_visible:
        submit_index = len(question.answers)
        style = "#04101b on #8fe0ff bold" if state.quiz_answer_index == submit_index else "#8fe0ff bold"
        prefix = ">" if state.quiz_answer_index == submit_index else " "
        options.append(f"\n{prefix} SUBMIT\n", style=style)

    feedback = Text()
    if state.quiz_feedback_visible:
        is_correct = bool(result and result.is_correct)
        feedback_style = "#57d18a bold" if is_correct else "#f6c66b bold"
        feedback.append("CORRECT\n\n" if is_correct else "INCORRECT\n\n", style=feedback_style)
        feedback.append(f"SCORE: {session.score}/{session.completed}\n\n")
        feedback.append("CORRECT SET:\n", style="#8fe0ff bold")
        for index in sorted(question.correct):
            feedback.append(f"- {question.answers[index]}\n")
    else:
        feedback.append("MOVE WITH UP/DOWN.\n")
        feedback.append("TOGGLE ONE OR MORE ANSWERS WITH SPACE OR KEYS 1-4.\n")
        feedback.append("ENTER SELECTS OR SUBMITS.")
    counter = Panel(
        Align.center(
            pixel_text(f"{min(session.completed + 1, session.total)}/{session.total}"), vertical="middle"
        ),
        title="QUESTION",
        border_style="#53b4ff",
        padding=(1, 1),
    )
    decorative = Panel(
        Align.center(pixel_text("Q"), vertical="middle"),
        title=question.difficulty.value.upper(),
        border_style="#53b4ff",
        padding=(2, 1),
    )
    top = Columns(
        [
            Panel(
                Text(question.prompt.upper(), style="#d8efff bold"),
                title="PROMPT",
                border_style="#53b4ff",
                padding=(1, 2),
            ),
            counter,
        ],
        equal=True,
        expand=True,
    )
    middle = Columns(
        [
            Panel(options, title="OPTIONS", border_style="#53b4ff", padding=(1, 1)),
            Panel(feedback, title="FEEDBACK", border_style="#53b4ff", padding=(1, 2)),
            decorative,
        ],
        equal=True,
        expand=True,
    )
    return Group(top, middle, Text("PROGRESS", style="#8fe0ff bold"), FullWidthProgressBar(session.completed, session.total))


def placeholder_content(text: str) -> RenderableType:
    return Panel(Text(text.upper(), style="#d8efff"), border_style="#53b4ff", padding=(1, 2))


def home_content() -> RenderableType:
    logo = Text(NETSIM_LOGO, style="#8fe0ff")
    return Panel(
        Align.center(logo, vertical="middle"),
        border_style="#53b4ff",
        padding=(1, 2),
        height=LESSONS_MENU_TOTAL_HEIGHT,
    )


def sidebar_for(state: AppState) -> RenderableType:
    if state.screen == Screen.HOME:
        return Group(menu_panel(state), home_info_panel(state))
    if state.screen == Screen.LESSONS_MENU:
        return lessons_sidebar(state)
    if state.screen == Screen.LESSON_DETAIL:
        return lessons_sidebar(state)
    if state.screen == Screen.ARCHITECTURE:
        return architecture_sidebar(state)
    if state.screen == Screen.QUIZ_TOPICS:
        return quiz_topics_sidebar(state)
    if state.screen == Screen.QUIZ_DIFFICULTY:
        return quiz_difficulty_sidebar(state)
    if state.screen == Screen.QUIZ_DETAIL:
        info = Text()
        info.append("QUIZ MODE\n\n", style="#8fe0ff bold")
        if state.quiz_session is not None:
            info.append(f"CATEGORY: {state.selected_quiz_label()}\n")
            info.append(f"DIFFICULTY: {state.selected_difficulty_label()}\n")
            info.append(f"SCORE: {state.quiz_session.score}/{state.quiz_session.completed}\n")
            info.append(f"BEST SCORE: {state.quiz_best_score()}%\n\n")
        info.append("0 RETURNS TO THE TOPIC LIST.")
        return Panel(info, title="QUIZ STATUS", border_style="#53b4ff", padding=(1, 1))
    if state.screen == Screen.SIMULATION:
        return Panel(Text("SIMULATION CONTROLS WILL APPEAR HERE."), title="SIM", border_style="#53b4ff")
    if state.screen == Screen.SCENARIOS:
        return Panel(Text("SCENARIO CONTROLS WILL APPEAR HERE."), title="SCENARIOS", border_style="#53b4ff")
    return Panel(Text(HELP_TEXT.upper(), style="#d8efff"), title="HELP", border_style="#53b4ff", padding=(1, 1))


def content_for(state: AppState) -> RenderableType:
    if state.screen == Screen.HOME:
        return with_matrix_right(home_content(), state.matrix_frame)
    if state.screen == Screen.LESSONS_MENU:
        return with_matrix_right(lessons_content(state), state.matrix_frame)
    if state.screen == Screen.LESSON_DETAIL:
        return with_matrix_right(lesson_detail_content(state), state.matrix_frame)
    if state.screen == Screen.ARCHITECTURE:
        selected = state.current_architecture_item()["key"]
        return with_matrix_right(ArchitectureDiagram(selected).render(), state.matrix_frame)
    if state.screen == Screen.QUIZ_TOPICS:
        return with_matrix_right(quiz_topics_content(state), state.matrix_frame)
    if state.screen == Screen.QUIZ_DIFFICULTY:
        return with_matrix_right(quiz_difficulty_content(state), state.matrix_frame)
    if state.screen == Screen.QUIZ_DETAIL:
        return with_matrix_right(quiz_detail_content(state), state.matrix_frame)
    if state.screen == Screen.SIMULATION:
        return with_matrix_right(placeholder_content(SIMULATION_TEXT), state.matrix_frame)
    if state.screen == Screen.SCENARIOS:
        return with_matrix_right(placeholder_content(SCENARIOS_TEXT), state.matrix_frame)
    return with_matrix_right(placeholder_content(HELP_TEXT), state.matrix_frame)
