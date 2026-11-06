# Virtual AI Assistant (Mini Alexa)

A text-based, rule-based assistant that runs offline in the terminal using only
the Python 3 standard library. No installs, datasets, APIs or ML libraries.

## Run
    python main.py

## Commands
| Command | What it does |
|---|---|
| time / date | Current time / date |
| calculate 12 + 8 | + - * / (also `x`); handles divide-by-zero and bad input |
| joke / quote / fact | Random item from a predefined list |
| game | Number guessing game (1-20, 5 tries, higher/lower hints) |
| recommend | Rule-based activity suggestion by time of day (AI demo) |
| perceptron | Single-neuron demo: inputs, weights, bias, step activation (DL demo) |
| help | List commands |
| exit / quit / bye | End the session |

Anything else gets a friendly fallback message.

## AI / ML / DL concepts
- **Rule-based system / intent recognition / keyword detection:** `main.route()`
- **Decision tree & classification analogy:** `ai_concepts.recommend_activity()`
- **Session "memory":** the stored user name, reused in responses
- **Artificial neuron, weights, bias, activation, forward propagation,
  hidden layer, perceptron:** `ai_concepts.perceptron_demo()` (fixed weights, no training)

## Files
main.py, greetings.py, datetime_utils.py, calculator.py, content.py, game.py,
ai_concepts.py, help_menu.py
