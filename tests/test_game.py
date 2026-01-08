import pytest

from src import game


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("rock", "scissors", "p1"),
        ("scissors", "paper", "p1"),
        ("paper", "rock", "p1"),
        ("scissors", "rock", "p2"),
        ("paper", "scissors", "p2"),
        ("rock", "paper", "p2"),
        ("rock", "rock", "draw"),
        ("paper", "paper", "draw"),
        ("scissors", "scissors", "draw"),
    ],
)
def test_determine_winner(a, b, expected):
    assert game.determine_winner(a, b) == expected


def test_invalid_choice_raises():
    with pytest.raises(ValueError):
        game.determine_winner("lizard", "rock")
    with pytest.raises(ValueError):
        game.determine_winner("rock", 123)
