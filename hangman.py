import random

# List of words
words = ["apple", "tiger", "house", "robot", "green"]

# Choose random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:

    display_word = ""

    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word completed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    # Avoid repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

# If user loses
if wrong_guesses == max_wrong:
    print("\n😢 Game Over!")
    print("The word was:", word)