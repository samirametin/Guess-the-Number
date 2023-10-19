from random import randint
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = randint(1,100)

if difficulty == 'easy':
    number_of_attemps = 10
elif difficulty == 'hard':
    number_of_attemps = 5
print(f"You have {number_of_attemps} attemps remainig to guess the number. ")

guess = int(input("Make a guess: "))

if number < guess:
    print(f"Too high. ")
    
elif number > guess:
    print("Too low. ")
else:
    print("You guessed the number. ")