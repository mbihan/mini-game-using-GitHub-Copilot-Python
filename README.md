
# Rock Paper Scissors — CLI mini-game-using-GitHub-Copilot-Python
The repo has code to develop the classic rock, paper, scissors minigame, with the help of GitHub Codespaces and GitHub Copilot.


The rock, paper, scissors game is a hand game in which each player chooses one of the three tools. From a programming point of view, this challenge is a nice exercise to practice conditional decisions, iterations, and the use of Python modules.

This project will demonstrate my ability to:

- Use GitHub Codespaces as a development environment.
- Use GitHub Copilot as an assistant.
- Develop input and output routines in a Python console application.

GameReadMe
===========

Overview
--------
This is a simple command-line Rock Paper Scissors game played against the computer. The app lets the player pick rock, paper, or scissors each round, reports the outcome, and tracks the cumulative score across multiple rounds. At the end of each round the player can choose whether to play again; when the player quits the final score is displayed.

Gameplay Rules
--------------
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both players choose the same option, the round is a draw

How to run
----------
1. Ensure Python 3.8+ is installed on your machine (the project was developed with Python 3.x).
2. (Optional) Create and activate a virtual environment:
   - python -m venv .venv
   - source .venv/bin/activate  (Linux/macOS) or .venv\Scripts\activate (Windows)
3. Install dependencies (if any):
   - pip install -r requirements.txt
4. Run the game:
   - python app.py

What the app does
-----------------
- Prompts the player for a choice (rock, paper, scissors).
- Randomly selects the computer's choice.
- Determines the winner of the round and prints a human-friendly outcome.
- Updates and displays cumulative scores (Player wins, Computer wins, Draws).
- After each round prompts the player to play again; quitting prints the final score.

Project structure
-----------------
- app.py        — CLI entrypoint and game loop
- src/game.py   — Game logic (valid choices, winner determination, outcome text)
- tests/        — Test suite (pytest)
- requirements.txt — Python dependencies (if present)

Technology stack
----------------
- Language: Python (3.x)
- Standard library: random, sys, builtins (no external libraries required to run the CLI)
- Testing: pytest (used for the test suite)
- Development environment: any system that can run Python (Linux, macOS, Windows)

Testing
-------
Run the test suite with:
- pytest

Notes
-----
- The app is intentionally minimal and implemented for educational/demo purposes.
- Modify src/game.py to extend rules or add features (score persistence, best-of series, multiplayer, etc.).

License
-------
See repository LICENSE or treat as MIT-style for sample/demo code unless a different license is provided.
