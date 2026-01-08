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
	player_wins = comp_wins = draws = 0
	while True:
		player = _prompt_choice()
		if player is None:
			print("Goodbye")
			print(f"Score — Player: {player_wins}, Computer: {comp_wins}, Draws: {draws}")
			break
		comp = choice(list(game.VALID_CHOICES))
		result = game.determine_winner(player, comp)
		print(game.outcome_text(result, player, comp))
		if result == "p1":
			player_wins += 1
		elif result == "p2":
			comp_wins += 1
		else:
			draws += 1
		again = input("Play again? (y/N): ").strip().lower()
		if again != "y":
			print("Thanks for playing")
			print(f"Final score — Player: {player_wins}, Computer: {comp_wins}, Draws: {draws}")
			break


if __name__ == "__main__":
	main()

