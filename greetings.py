"""Greeting and name capture (FR-01, FR-02).

AI concept: Human-Computer Interaction - the assistant opens the
conversation and stores a piece of session state (the user's name).
"""

ASSISTANT_NAME = "Mini Alexa"
DEFAULT_USER_NAME = "friend"  # used if the user presses Enter without typing


def get_user_name():
    """Greet the user, ask for their name, and return it (session memory)."""
    print(f"Assistant: Hi! I'm {ASSISTANT_NAME}. What's your name?")
    name = input("You: ").strip()
    return name.title() if name else DEFAULT_USER_NAME


def build_greeting(user_name):
    """Return a short welcome message that reuses the stored name."""
    return (f"Nice to meet you, {user_name}! Type 'help' "
            f"to see what I can do.")
