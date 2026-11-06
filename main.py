"""Mini Alexa - a rule-based, offline virtual assistant (Nexbridge AI Internship P1).

Request -> classification -> response loop:
  input -> normalize -> keyword match (intent recognition) -> call module -> print

AI concept: the whole program is a rule-based system. Each keyword check is an
explicit rule; a trained model would learn such a mapping from data instead.
"""

import calculator
import content
import datetime_utils
import game
import ai_concepts
import greetings
import help_menu

EXIT_WORDS = ("exit", "quit", "bye")
GREETING_WORDS = ("hello", "hi", "hey")
FALLBACK = "I'm not sure I understood that — type 'help' to see what I can do."


def has_word(words, text):
    """True if any trigger word appears as a whole word in the text."""
    tokens = text.split()
    return any(w in tokens for w in words)


def route(command, user_name, session):
    """Match a normalized command to a feature. Returns (response, should_exit)."""
    # Exit is checked first so "bye" always works.
    if has_word(EXIT_WORDS, command):
        return f"Goodbye, {user_name}! Have a great day.", True
    # Calculator before others so "calculate 5 x 3" isn't misread.
    if "calculate" in command or "calc" in command or any(
            ch.isdigit() for ch in command):
        session["last_feature"] = "calculator"
        return calculator.calculate(command), False
    if "time" in command:
        return f"{user_name}, {datetime_utils.get_current_time()}", False
    if "date" in command or "day" in command:
        return datetime_utils.get_current_date(), False
    if "joke" in command:
        return content.get_random_joke(), False
    if "quote" in command or "motivat" in command:
        return content.get_random_quote(), False
    if "fact" in command:
        return content.get_random_fact(), False
    if "game" in command or "guess" in command:
        return game.play_guessing_game(), False
    if "recommend" in command or "suggest" in command:
        return ai_concepts.recommend_activity(), False
    if "perceptron" in command or "neuron" in command:
        return ai_concepts.perceptron_demo(), False
    if "help" in command:
        help_menu.print_help()
        return None, False
    if has_word(GREETING_WORDS, command):
        return f"Hello again, {user_name}!", False
    return FALLBACK, False  # FR-12: unknown input never crashes


def main():
    print("=" * 43)
    print("        MINI ALEXA - VIRTUAL ASSISTANT")
    print("=" * 43)
    user_name = greetings.get_user_name()   # session state (in-memory only)
    print(f"Assistant: {greetings.build_greeting(user_name)}\n")
    session = {}
    while True:
        try:
            command = input("You: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print(f"\nAssistant: Goodbye, {user_name}! Have a great day.")
            break
        if not command:
            continue
        try:
            response, should_exit = route(command, user_name, session)
        except Exception as error:  # top-level safety net
            response, should_exit = f"Oops, something went wrong ({error}).", False
        if response:
            print(f"Assistant: {response}")
        print()
        if should_exit:
            break
    print("=" * 43)


if __name__ == "__main__":
    main()
