"""Educational AI / ML / DL demonstrations (FR-13, FR-14).

Nothing here is trained. These are plain-Python analogies.
"""

from datetime import datetime

# ---- Perceptron settings: fixed, NOT learned (a trained model would learn them)
WEIGHTS = [0.5, 0.3, 0.2]   # one weight per input
BIAS = -1.0                 # constant added to the weighted sum
HIDDEN_WEIGHT = 1.0         # weight used by the optional second "layer"
HIDDEN_BIAS = -0.5


def recommend_activity(hour=None):
    """Rule-based decision (AI concept) / decision-tree analogy (ML concept).

    The if/elif chain is a tiny decision tree: the current hour is the input
    feature and the returned activity is the predicted "class".
    """
    if hour is None:
        hour = datetime.now().hour
    if 5 <= hour < 11:
        return "It's morning - a good time for breakfast and planning your day."
    if 11 <= hour < 14:
        return "It's midday - time for lunch and a short break."
    if 14 <= hour < 18:
        return "It's afternoon - a great time for focused work or study."
    if 18 <= hour < 22:
        return "It's evening - time for dinner and relaxing."
    return "It's late - time to rest and get some sleep."


def step_activation(value):
    """Step activation function: output 1 if value > 0, else 0."""
    return 1 if value > 0 else 0


def perceptron(inputs):
    """Single artificial neuron: weighted sum + bias -> step activation.

    Forward propagation: inputs -> weights/bias -> activation -> output.
    """
    weighted_sum = sum(x * w for x, w in zip(inputs, WEIGHTS)) + BIAS
    return weighted_sum, step_activation(weighted_sum)


def perceptron_demo():
    """Ask for 2-3 numbers, run the neuron, and explain each step."""
    raw = input("Enter 2 or 3 numbers separated by spaces: ").split()
    try:
        inputs = [float(x) for x in raw]
    except ValueError:
        return "Those weren't all numbers - try something like '2 3 1'."
    if not 2 <= len(inputs) <= 3:
        return "Please enter 2 or 3 numbers."
    weighted_sum, output = perceptron(inputs)
    hidden = step_activation(output * HIDDEN_WEIGHT + HIDDEN_BIAS)
    lines = [f"Inputs: {inputs}",
             f"Weights (fixed): {WEIGHTS[:len(inputs)]}",
             f"Bias: {BIAS}",
             f"Weighted sum + bias = {round(weighted_sum, 3)}",
             f"Step activation output = {output}",
             f"Hidden layer output (second neuron) = {hidden}",
             "This single neuron is the perceptron - the simplest unit of a "
             "neural network. Here nothing is trained; the weights are fixed."]
    return "\n".join("  " + line for line in lines)
