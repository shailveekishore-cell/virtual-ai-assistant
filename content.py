"""Quotes, jokes and facts (FR-06, FR-07, FR-08).

Each feature is a predefined list; random.choice() picks one per request.

ML analogy: selecting content with simple rules mirrors, at a very
conceptual level, how a recommendation engine picks items to show.
"""

import random

QUOTES = [
    "The only way to do great work is to love what you do.",
    "Success is the sum of small efforts repeated day in and day out.",
    "Don't watch the clock; do what it does. Keep going.",
    "It always seems impossible until it's done.",
    "Believe you can and you're halfway there.",
    "Every expert was once a beginner.",
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 kinds of people: those who understand binary and those who don't.",
    "Why was the function sad? It didn't get any arguments.",
    "I would tell you a UDP joke, but you might not get it.",
    "A SQL query walks into a bar, goes up to two tables and asks: 'Can I join you?'",
]

FACTS = [
    "The term 'Artificial Intelligence' was coined in 1956 at the Dartmouth workshop.",
    "The first computer bug was a real moth found in a Harvard Mark II relay in 1947.",
    "Python is named after Monty Python, not the snake.",
    "The perceptron, an early neural network unit, was introduced by Frank Rosenblatt in 1958.",
    "Honey never spoils; edible honey has been found in ancient Egyptian tombs.",
    "A day on Venus is longer than a year on Venus.",
]


def get_random_quote():
    return random.choice(QUOTES)


def get_random_joke():
    return random.choice(JOKES)


def get_random_fact():
    return random.choice(FACTS)
