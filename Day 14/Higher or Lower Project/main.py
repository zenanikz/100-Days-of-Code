from art import logo, vs
from game_data import data
import random


global current_score, user_guess
current_score = 0
list_num = []



def logo_image():
    print(logo)



def vs_image():
    print(vs)



def random_choices():
    list_num.clear()
    for x in range(1,3):
        list_num.append(random.randint(0, len(data)))

    print(f"Compare A: {data[list_num[0]]["name"]}, a {data[list_num[0]]["description"]}, from {data[list_num[0]]["country"]}.")
    vs_image()
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



def users_followers_max():
    user_guess_letter = user_input()
    user_guess_follower_count = 0
    if user_guess_letter == "A":
        user_guess_follower_count = data[list_num[0]]["follower_count"]
    elif user_guess_letter == "B":
        user_guess_follower_count = data[list_num[1]]["follower_count"]

    return user_guess_follower_count



def score_calculator():
    global current_score
    current_score += 1

    return current_score



def guess_check():
    guess_follower_count = users_followers_max()
    actual_follower_count = most_followers()
    logo_image()
    if guess_follower_count == actual_follower_count:
        user_score = score_calculator()
        print(f"You're right! Current score: {user_score}")
        run_game()
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")



logo_image()
def run_game():
    random_choices()
    most_followers()
    guess_check()


run_game()