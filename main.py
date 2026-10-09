import random
from words import WORD_LIST
from hangman_art import LOGO, STAGES

def play_hangman():
    print(LOGO)
    print("Welcome to Hangman Game!\n")

    # Select random word and hint
    selected = random.choice(WORD_LIST)
    chosen_word = selected["word"].upper()
    hint = selected["hint"]

    lives = 6
    guessed_letters = []
    display = ["_"] * len(chosen_word)

    print(f"HINT: {hint}")
    print(f"Word to guess: {' '.join(display)}\n")

    game_over = False

    while not game_over:
        guess = input("Guess a letter: ").strip().upper()

        # Validation checks
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.append(guess)

        # Check guess in word
        if guess in chosen_word:
            print(f"Good job! '{guess}' is in the word.")
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            lives -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Remaining Lives: {lives}")

        # Display current state
        print(STAGES[6 - lives])
        print(f"Word: {' '.join(display)}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}\n")

        # Win condition
        if "_" not in display:
            game_over = True
            print("🎉 Congratulations! You guessed the word and WON! 🎉")

        # Lose condition
        if lives == 0:
            game_over = True
            print(f"☠️ You lost all lives! Game Over. The correct word was: {chosen_word}")

if __name__ == "__main__":
    play_hangman()