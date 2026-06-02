import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.choice(choices)

if user_choice == 0:
    print(rock)
    print(f"Computer chose:\n{computer_choice}")
    if computer_choice == rock:
        print("Nobody wins!")
    elif computer_choice == paper:
        print("Computer wins!")
    elif computer_choice == scissors:
        print("You win!")
elif user_choice == 1:
    print(paper)
    print(f"Computer chose:\n{computer_choice}")
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == paper:
        print("Nobody wins!")
    elif computer_choice == scissors:
        print("Computer wins!")
elif user_choice == 2:
    print(scissors)
    print(f"Computer chose:\n{computer_choice}")
    if computer_choice == rock:
        print("Computer wins!")
    elif computer_choice == paper:
        print("You win!")
    elif computer_choice == scissors:
        print("Nobody wins!")
else:
    print("What you selected doesn't exist.")