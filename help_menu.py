"""Help menu (FR-10)."""

COMMANDS = [
    ("time", "show current time"),
    ("date", "show current date"),
    ("calculate", "do a calculation, e.g. calculate 12 + 8"),
    ("joke", "tell a joke"),
    ("quote", "motivational quote"),
    ("fact", "random fact"),
    ("game", "play number guessing game"),
    ("recommend", "rule-based activity suggestion (AI demo)"),
    ("perceptron", "single-neuron demo (DL demo)"),
    ("help", "show this menu"),
    ("exit", "quit the assistant"),
]


def print_help():
    print("Assistant:")
    for name, description in COMMANDS:
        print(f"  - {name:<12}{description}")
