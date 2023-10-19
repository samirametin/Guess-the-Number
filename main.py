from random import randint
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = randint(1,100)

if difficulty == 'easy':
    number_of_attemps = 10
elif difficulty == 'hard':
    number_of_attemps = 5


is_game_over = False

while not is_game_over:
    print(f"You have {number_of_attemps} attemps remainig to guess the number. ")
    guess = int(input("Make a guess: "))

    if number < guess:
        print("Too high. \nGuess again")
        number_of_attemps -= 1
    elif number > guess:
        print("Too low. \nGuess again")
        number_of_attemps -= 1
    else:
        print("You guessed the number.")
        is_game_over = True

    if number_of_attemps == 0:
        print("You've run out of guesses, you lose. ")
        is_game_over = True




