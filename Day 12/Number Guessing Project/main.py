from art import logo
import random, sys

print(logo)

attempts, attempts_used = 0, 0

def init_attempts():
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if user_difficulty == "easy":
        attempts = 10
    elif user_difficulty == "hard":
        attempts = 5

    return attempts


def prompt_user():
    user_choice = int(input("Make a guess: "))

    return user_choice


def checking_guess():
    computer_number = random.randint(1, 100)
    attempts_used = init_attempts()

    print(f"You have {attempts_used} remaining to guess the number.")
    user_choice = prompt_user()

    while attempts_used > 1:
        if user_choice < computer_number:
            attempts_used -= 1
            print("Too low.\nGuess again.")
        elif user_choice == computer_number:
            print(f"You got it! The answer was {computer_number}.")
            sys.exit()
        elif user_choice > computer_number:
            attempts_used -= 1
            print("Too high.\nGuess again.")
        print(f"You have {attempts_used} remaining to guess the number.")
        user_choice = prompt_user()
    else:
        print("You've run out of guesses. Refresh the page to run again.")


def play():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    checking_guess()

play()
