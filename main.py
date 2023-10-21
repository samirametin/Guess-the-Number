from random import randint

EASY_GAME = 10
HARD_GAME = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_GAME
    elif difficulty == "hard":
        return HARD_GAME


def check_answer(answer, guess, turns):
    if answer < guess:
        print("Too high.")
        return turns - 1
    elif answer > guess:
        print("Too low.")
        return turns - 1
    else:
        print(f"You guessed the number. The number was {answer}")
        return


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    print(f"PSsst the number is {number}")
    attemps = set_difficulty()
    guess = 0
    while number != guess:
        print(f"You have {attemps} attemps remainig to guess the number. ")
        guess = int(input("Make a guess: "))
        attemps = check_answer(number, guess, attemps)
        if attemps == 0:
            print("You've run out of guesses, you lose. ")
            return
        elif number != guess:
            print("Guess again. ")


game()
