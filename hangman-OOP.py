from words import words
import random, string


class HangmanGame:
    player_list = []

    def __init__(self) -> None:
        self.__word = random.choice(words).upper()  # select a random word
        self.__word_letters = set(self.__word)  # extract the selected word letters
        self.__correct_letters = set()  # tracking the correct guessed letters
        self.guessed_letters = set()  # tracking the guessed letters
        self.__lives = 4  # initial lives
        self.__win_state = False
        self.player_name = self.get_player_name()
        HangmanGame.player_list.append(self)
        self.display_welcome_message()

    def get_player_name(self) -> str:
        # getting player's name
        name = input("Please enter your name: ").title()
        if name:
            return name
        return "Player-" + str(len(HangmanGame.player_list) + 1)

    def get_valid_letter(self) -> str:
        # validating the guessed letter
        # it must be a single capital letter which is not a duplicate
        guessed_letter = input(f"{self.player_name}, Please guess a letter: ").upper()
        if (
            guessed_letter in string.ascii_uppercase
            and len(guessed_letter) == 1
            and guessed_letter not in self.guessed_letters
        ):
            return guessed_letter
        else:
            print("\nGuess exactly one letter from alphabet characters!")
            print("and make sure you have not guessed that letter before!")
            return None

    def __minus_lives(self) -> None:
        # reducing the number of lives
        self.__lives -= 1

    def __has_lives(self) -> bool:
        # checking the player lives to continue
        return self.__lives > 0

    def has_won(self) -> bool:
        # checking if the player has won or not
        if len(self.__correct_letters) == len(self.__word_letters):
            self.__win_state = True
        return self.__win_state

    def can_continue(self) -> bool:
        # checking if the player can continue playing
        return self.__has_lives() and not self.has_won()

    def display_welcome_message(self) -> None:
        # showing a welcome message and game rules
        print(f"\nWelcome to Hangman, {self.player_name}.")
        print("You have 4 lives to guess the word, otherwise you lose. Good Luck!")

    def display_word_status(self) -> str:
        # showing the guessed word status based on the correct guessed letters
        return " ".join(l if l in self.__correct_letters else "_" for l in self.__word)

    def display_guessed_letters(self) -> str:
        # showing all of the guessed letters
        return "  ".join(sorted(self.guessed_letters))

    def display_game_status(self):
        # displaying a game status for player
        print(f"\n{self.player_name} Status =>")
        print(f"Word: {self.display_word_status()}")
        print(f"Guessed: {self.display_guessed_letters()}")
        print(f"Lives: {self.__lives}")

    def display_endgame_message(self) -> None:
        if self.__win_state:
            # winner message
            print(f"\nCongratulations {self.player_name}, you have won!")
            print(f"The word was: {self.display_word_status()}")
        else:
            # loser message
            print(f"\nSorry {self.player_name}, you lost!")
            print(f"The word was {' '.join(l for l in self.__word)}")

    def play_game(self):
        # start/resume the game for player
        self.display_game_status()
        guessed_letter = self.get_valid_letter()
        if guessed_letter:
            self.guessed_letters.add(guessed_letter)
            if guessed_letter in self.__word_letters:
                self.__correct_letters.add(guessed_letter)
            else:
                self.__minus_lives()

        if not self.can_continue():
            self.display_endgame_message()

    @classmethod
    def game_has_winner(cls):
        # checking if any player has won
        return any(player.has_won() is True for player in cls.player_list)

    @classmethod
    def game_has_ended(cls):
        # checking if the game has ended
        return not any(player.can_continue() is True for player in cls.player_list)


class GameController:
    # HangmanGame controller
    def __init__(self, cls) -> None:
        if cls.player_list:
            while True:
                for player in cls.player_list:
                    if player.can_continue():
                        player.play_game()
                if cls.game_has_winner():
                    print("\nThe winner is:")
                    for player in cls.player_list:
                        if player.has_won():
                            print(player.player_name)
                    break
                if cls.game_has_ended():
                    print("\nNobody won!!!")
                    break
        else:
            print("\nPlease add players in order to play the game!")


def game_commands():
    # printing game commands for the players
    print(
        """
    add   (a): for adding a new player to the game,
    play  (p): to start the game,
    reset (r): to remove all players,
    exit  (e): to exit the game"""
    )


if __name__ == "__main__":
    game_commands()
    while True:
        order = input("\nWhat do you want to do? ").lower()
        if order == "add" or order == "a":
            HangmanGame()
        elif order == "play" or order == "p":
            GameController(HangmanGame)
            game_commands()
        elif order == "reset" or order == "r":
            HangmanGame.player_list.clear()
            print("\nAll the players have been removed.")
        elif order == "exit" or order == "e":
            print("\nThanks for playing.")
            break
        else:
            print("\nPlease use one of the mentioned commands or their abbreviation")
            game_commands()
