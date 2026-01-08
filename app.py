"""Simple Rock-Paper-Scissors CLI application."""

from random import choice
from src import game


def _prompt_choice():
	valid = ", ".join(sorted(game.VALID_CHOICES))
	while True:
		try:
			s = input(f"Choose ({valid}): ").strip().lower()
		except (EOFError, KeyboardInterrupt):
			print()
			return None
		if not s:
			continue
		if s in game.VALID_CHOICES:
			return s
		print(f"Invalid choice: {s}")


def main():
	print("Rock Paper Scissors — play against the computer")
	while True:
		player = _prompt_choice()
		if player is None:
			print("Goodbye")
			break
		comp = choice(list(game.VALID_CHOICES))
		result = game.determine_winner(player, comp)
		print(game.outcome_text(result, player, comp))
		again = input("Play again? (y/N): ").strip().lower()
		if again != "y":
			print("Thanks for playing")
			break


if __name__ == "__main__":
	main()

