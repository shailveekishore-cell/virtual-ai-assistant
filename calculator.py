"""Basic calculator (FR-05).

Parses a command such as "calculate 12 + 8" or "5*3" into two numbers and
an operator. Invalid input and division by zero return friendly messages
instead of raising errors.
"""

import re

# Matches: number, operator (+ - * / x), number. Whitespace is optional.
_PATTERN = re.compile(
    r"(-?\d+(?:\.\d+)?)\s*([+\-*/x])\s*(-?\d+(?:\.\d+)?)"
)


def parse_expression(text):
    """Extract (left, operator, right) from text, or None if not found."""
    match = _PATTERN.search(text)
    if not match:
        return None
    left, operator, right = match.groups()
    return float(left), operator, float(right)


def calculate(text):
    """Evaluate the expression in text and return a response string."""
    parsed = parse_expression(text)
    if parsed is None:
        return ("I couldn't find a calculation. Try something like "
                "'calculate 12 + 8'.")
    left, operator, right = parsed
    try:
        if operator == "+":
            result = left + right
        elif operator == "-":
            result = left - right
        elif operator in ("*", "x"):
            result = left * right
        else:  # "/"
            result = left / right
    except ZeroDivisionError:
        return "I can't divide by zero — try a different number."
    # Show whole numbers without a trailing ".0"
    if result == int(result):
        result = int(result)
    else:
        result = round(result, 6)
    return f"The result is {result}"
