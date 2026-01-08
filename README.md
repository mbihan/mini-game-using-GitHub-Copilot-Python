```markdown
# Rock Paper Scissors — CLI mini-game

This repository contains a simple Rock–Paper–Scissors command-line game.

How to run:

```bash
python app.py
```

Run tests:

```bash
pip install -r requirements.txt
python -m pytest -q
```


This repository contains a small, extensible Python mini-game inspired by the Microsoft learning challenge project. It's a console-based Number Guessing mini-game with difficulty levels, simple scoring, and tests so you can iterate quickly.

Features
- Level-based random target ranges (easy→small range, hard→larger range)
- Limited attempts, clear feedback (too low / too high)
- Simple test suite using `pytest`

Quick start

1. Create a virtual environment and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the game:

```bash
python -m src --level 2
```

3. Run tests:

```bash
pytest -q
```

Files of interest
- `src/game.py` — core game logic (random target, evaluation functions)
- `src/__main__.py` — CLI runner
- `tests/test_game.py` — unit tests for game logic

Feel free to ask me to extend this to a GUI, add persistence (high score file), or convert it to a Pygame variant.

```
# mini-game-using-GitHub-Copilot-Python
The repo has code to develop the classic rock, paper, scissors minigame, with the help of GitHub Codespaces and GitHub Copilot.


The rock, paper, scissors game is a hand game in which each player chooses one of the three tools. From a programming point of view, this challenge is a nice exercise to practice conditional decisions, iterations, and the use of Python modules.

The winner of the game is based in three simple rules:

Rock beats scissors.
Scissors beat paper.
Paper beats rock.


This project will demonstrate my ability to:

Use GitHub Codespaces as a development environment.
Use GitHub Copilot as an assistant.
Develop input and output routines in a Python console application.

