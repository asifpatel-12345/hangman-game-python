# 🎯 Hangman Game in Python

A classic command-line interface (CLI) Hangman Game built with Python. Test your vocabulary skills by guessing the hidden word letter by letter before running out of lives and drawing the complete stick-figure!

---

## 🌟 Features

- 🎮 **Interactive CLI Experience:** Clear visual cues with ASCII art for hangman stages.
- 💡 **Helpful Hints:** Every secret word comes with a relevant hint to guide you.
- 🛡️ **Input Validation:** Prevents duplicate letter guesses and validates input format.
- 🧩 **Modular Code Structure:** Clean separation of game logic, ASCII graphics, and data files.

---

## 📁 Project Structure

```text
hangman-game/
│
├── main.py              # Core game loop and user interaction logic
├── hangman_art.py      # ASCII art drawings for banner logo and hangman stages
├── words.py            # Word dictionary containing words and hints
└── README.md           # Project documentation