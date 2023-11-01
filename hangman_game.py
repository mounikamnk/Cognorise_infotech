import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman_display(incorrect_guesses):
    hangman_figures = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    return hangman_figures[incorrect_guesses]

def play_hangman():
    word = choose_random_word(word_list)
    guessed_letters = []
    incorrect_guesses = 0

    while True:
        print(hangman_display(incorrect_guesses))
        print(display_word(word, guessed_letters))

        if incorrect_guesses == 6:
            print(f"Sorry, you lost! The word was '{word}'.")
            break

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations, you won!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing!")

play_hangman()
