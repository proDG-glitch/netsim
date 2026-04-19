# netsim

NetSim is a full-screen terminal dashboard built with `Textual` and `Rich`.
It uses a central app state machine, ASCII banner rendering, framed multi-pane layouts,
an interactive architecture explorer, quiz flow screens, and JSON score persistence.

Run it with:

```bash
python3 main.py
```

The main menu includes Lessons and Exit. Each lesson opens with a built-in quiz
in the right-side lesson pane. Quiz questions load from `assets/quiz/questions.json`,
shuffle questions and answers, and allow multiple answers per question.

Run the standalone quiz mode with:

```bash
python3 quiz_cli.py
```

Or provide another JSON file:

```bash
python3 quiz_cli.py path/to/questions.json
```

Controls:

- `Up` / `Down` move selection
- `Enter` opens or confirms
- `h` goes home
- `b` goes back
- `q` quits
- `1-4` choose quiz answers
- `0` backs out of supported screens

Standalone quiz controls:

- `Up` / `Down` move selection
- `Space` toggles an answer
- `Enter` submits or continues
- `q` exits
