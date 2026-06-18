from art import logo, vs
from game_data import data
import random


user_score = 0


def random_choices():
    global list_num
    list_num = []

    for x in range(1,3):
        list_num.append(random.randint(0, len(data) - 1))

    print(f"Compare A: {data[list_num[0]]["name"]}, a {data[list_num[0]]["description"]}, from {data[list_num[0]]["country"]}.")
    print(vs)
    print(f"Against B: {data[list_num[1]]["name"]}, a {data[list_num[1]]["description"]}, from {data[list_num[1]]["country"]}.")

    return list_num



def most_followers():
    most_followers_num = 0
    a_followers = data[list_num[0]]["follower_count"]
    b_followers = data[list_num[1]]["follower_count"]

    if a_followers > b_followers:
        most_followers_num = a_followers
    else:
        most_followers_num = b_followers

    return most_followers_num



def user_input():
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    return user_guess



def users_followers_max(user_guess_letter):
    user_guess_follower_count = 0
    if user_guess_letter == "A":
        user_guess_follower_count = data[list_num[0]]["follower_count"]
    elif user_guess_letter == "B":
        user_guess_follower_count = data[list_num[1]]["follower_count"]

    return user_guess_follower_count



continue_game = True

def guess_check():
    global user_score, continue_game
    guess_follower_count = users_followers_max(user_input())
    actual_follower_count = most_followers()
    print(logo)
    if guess_follower_count == actual_follower_count:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
        continue_game = True
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        continue_game = False

    return continue_game



def run_game():
    result = True
    while result:
        random_choices()
        result = guess_check()


print(logo)
run_game()