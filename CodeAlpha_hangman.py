import random

# Predefined word list
WORDS = ["python", "rocket", "jungle", "bridge", "castle"]

def display_state(guessed_letters, word, wrong_guesses):
    """Display the current game state."""
    # Show the word with blanks
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display}")
    print(f"Wrong guesses left: {6 - wrong_guesses}")
    print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

def hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("=" * 40)
    print("      Welcome to Hangman!")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have {max_wrong} incorrect guesses.")

    while wrong_guesses < max_wrong:
        display_state(guessed_letters, word, wrong_guesses)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You won! The word was: {word}")
            return

        # Get player input
        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"'{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"'{guess}' is NOT in the word.")

    # Game over
    print(f"\n💀 Game over! You ran out of guesses. The word was: '{word}'")

if __name__ == "__main__":
    while True:
        hangman()
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye.")
            break