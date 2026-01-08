"""Rock Paper Scissors game logic.

Rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
"""

VALID_CHOICES = {"rock", "paper", "scissors"}

_BEATS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

def _normalize(choice: str) -> str:
    if not isinstance(choice, str):
        raise ValueError("choice must be a string")
    return choice.strip().lower()

def determine_winner(p1: str, p2: str) -> str:
    """Determine winner between p1 and p2.

    Returns:
      - "draw" if same choice
      - "p1" if first player wins
      - "p2" if second player wins

    Raises ValueError for invalid choices.
    """
    a = _normalize(p1)
    b = _normalize(p2)
    if a not in VALID_CHOICES:
        raise ValueError(f"invalid choice: {p1}")
    if b not in VALID_CHOICES:
        raise ValueError(f"invalid choice: {p2}")
    if a == b:
        return "draw"
    if _BEATS[a] == b:
        return "p1"
    return "p2"

def outcome_text(result: str, p1: str, p2: str) -> str:
    """Return a human friendly outcome message."""
    if result == "draw":
        return f"Both chose {p1}. It's a draw."
    winner = "Player" if result == "p1" else "Computer"
    return f"{winner} wins: {p1} vs {p2}."
