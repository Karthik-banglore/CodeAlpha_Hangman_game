import random

def hangman():
    words = ["apple", "robot", "train", "music", "cloud"]
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {attempts} incorrect guesses allowed.")

    while attempts > 0:
        display = [letter if letter in guessed else "_" for letter in word]
        print("\nWord: " + " ".join(display))

        guess = input("Enter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.append(guess)
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

        if all(letter in guessed for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print(f"\nGame over. The word was: {word}")

if __name__ == "__main__":
    hangman()