from words import words
import random, string


def initialize_lives():
    lives = 4  # initial lives

    return lives


def reset_guessed_letters():
    correct_letters = set()  # tracking the correct guessed letters
    guessed_letters = set()  # tracking the guessed letters

    return correct_letters, guessed_letters


def choose_random_word():
    word = random.choice(words).upper()  # Select a random word
    word_letters = set(word)  # extracting the selected word letters

    return word, word_letters


def get_player_name():
    player_name = input("Please enter your name: ")
    return player_name.title()


def display_word_status(word, correct_letters):
    # showing the status of the guessed word
    return " ".join(l if l in correct_letters else "_" for l in word)


def get_valid_letter(guessed_letters):
    # validating the guessed letter
    guessed_letter = input("Please guess a letter: ").upper()
    if (
        guessed_letter in string.ascii_uppercase
        and len(guessed_letter) == 1
        and guessed_letter not in guessed_letters
    ):
        return guessed_letter
    else:
        print("\nGuess exactly one letter from alphabet characters!")
        print("and make sure you have not guessed that letter before!")
        return None


def end_game_message(player_name, win_status, word):
    # Showing the game result
    won = True if win_status else False
    if won:
        print(f"\nCongratulations {player_name}, you have won!")
        print(f"The word was: {display_word_status(word, correct_letters)}")
    else:
        print(f"\nSorry, you lost!\nThe word was {' '.join(l for l in word)}")


def ask_play_again():
    # checking if the user wants to play again or not
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    return play_again == "yes" or play_again == "y"


if __name__ == "__main__":
    # getting the required data for starting the game
    lives = initialize_lives()
    correct_letters, guessed_letters = reset_guessed_letters()
    word, word_letters = choose_random_word()

    if player_name := get_player_name():
        print(f"\nWelcome to Hangman, {player_name}.")
    else:
        player_name = "player"
        print(f"\nWelcome to Hangman, {player_name}.")
    print("\nyour have 4 lives to guess the word, otherwise you lose. Good Luck!")

    while True:
        print(f"\nWord: {display_word_status(word, correct_letters)}")
        print(f"Guessed: {'  '.join(sorted(guessed_letters))}")
        print(f"Remaining Lives:{lives}")

        guessed_letter = get_valid_letter(guessed_letters)
        if guessed_letter:
            guessed_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                correct_letters.add(guessed_letter)
            else:
                lives -= 1

        if lives == 0 or len(correct_letters) == len(word_letters):
            end_game_message(
                player_name, len(correct_letters) == len(word_letters), word
            )

            if not ask_play_again():
                break
            else:
                # resetting the data for the next game
                lives = initialize_lives()
                correct_letters, guessed_letters = reset_guessed_letters()
                word, word_letters = choose_random_word()
