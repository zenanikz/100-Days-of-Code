import sys
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

global user_cards, computer_cards, sum_user_cards, sum_computer_cards

user_cards, computer_cards = [], []

def choose_cards():
    user_random = random.choice(cards)
    computer_random = random.choice(cards)

    user_cards.append(user_random)
    computer_cards.append(computer_random)

    return (user_cards, computer_cards)


def check_user_cards():
    sum_user_cards, count_x,  initial_total_user_cards = 0, 0, 0

    for u_c in user_cards:
        initial_total_user_cards += u_c

    for x in user_cards:
        if x == 11 and initial_total_user_cards <= 21:
            x = 1
            sum_user_cards += x
            user_cards[count_x] = x
        else:
            sum_user_cards += x
        count_x += 1

    count_x = 0

    return sum_user_cards


def check_computer_cards():
    sum_computer_cards, count_y, initial_total_computer_cards = 0, 0, 0

    for c_c in computer_cards:
        initial_total_computer_cards += c_c

    for y in computer_cards:
        if y == 11 and initial_total_computer_cards <= 21:
            y = 1
            sum_computer_cards += y
            computer_cards[count_y] = y
        else:
            sum_computer_cards += y
        count_y += 1

    count_y = 0

    return sum_computer_cards


def start_game():
    user_cards.clear()
    computer_cards.clear()

    print(logo)

    for start in range(0, 2):
        choose_cards()

    sum_user_cards = check_user_cards()

    print(f"    Your cards: {user_cards}, current score: {sum_user_cards}")
    print(f"    Computer's first card: {computer_cards[0]}")

    win_or_lose()


def continue_playing():
    global sum_user_cards, sum_computer_cards

    choose_cards()

    sum_user_cards = check_user_cards()
    sum_computer_cards = check_computer_cards()

    print(f"    Your cards: {user_cards}, current score: {sum_user_cards}")
    print(f"    Computer's first card: {computer_cards[0]}")

    win_or_lose()

    return (sum_computer_cards, sum_user_cards)


def final_print():
    sum_user_cards = check_user_cards()
    sum_computer_cards = check_computer_cards()

    print(f"    Your final hand: {user_cards}, final score: {sum_user_cards}")
    print(f"    Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")

def win_or_lose():
    sum_user_cards = check_user_cards()
    sum_computer_cards = check_computer_cards()

    if sum_user_cards >= 21:
        final_print()
        print("You lose😤")
        initialise_game()
    elif sum_computer_cards >= 21:
        final_print()
        print("Oppenent went over. You win😁")
        initialise_game()
    else:
        play_again()


def play_again():
    sum_user_cards = check_user_cards()
    sum_computer_cards = check_computer_cards()

    pass_or_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if pass_or_another == "y":
        continue_playing()
    elif pass_or_another == "n":
        final_print()
        if sum_computer_cards < sum_user_cards:
            print("Oppenent went over. You win😁")
        elif sum_computer_cards == sum_user_cards:
            print("Draw")
        else:
            print("You lose😤")

        initialise_game()


def initialise_game():
    game_init = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if game_init == "y":
        start_game()
        play_again()
    else:
        sys.exit()

initialise_game()