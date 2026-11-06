"""Number guessing game (FR-09)."""

import random

MIN_NUMBER = 1       # lowest possible secret number
MAX_NUMBER = 20      # highest possible secret number
MAX_ATTEMPTS = 5     # guesses allowed per game


def play_guessing_game():
    """Run one game: the user gets MAX_ATTEMPTS guesses with higher/lower hints."""
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Assistant: I'm thinking of a number between {MIN_NUMBER} and "
          f"{MAX_NUMBER}. You have {MAX_ATTEMPTS} tries.")
    for attempt in range(1, MAX_ATTEMPTS + 1):
        raw = input(f"Guess #{attempt}: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Assistant: That's not a whole number. Try again.")
            continue  # an invalid guess still uses up the attempt
        if guess == secret:
            return f"You got it in {attempt} tries! The number was {secret}."
        if attempt < MAX_ATTEMPTS:
            hint = "higher" if guess < secret else "lower"
            print(f"Assistant: Try {hint}.")
    return f"Out of tries! The number was {secret}. Better luck next time."
