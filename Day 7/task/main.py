import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

guess = input("Guess a letter: ").lower()

display = ""
temp_display = []
index = 0

for x in range(len(chosen_word)):
    temp_display.append("_")

while guess not in chosen_word:
    guess = input("Guess a letter: ").lower()


# TODO-2: Change the for loop so that you keep the previous correct letters in display.

while display != chosen_word:
    for letter in chosen_word:
        if letter == guess:
            temp_display[index] = letter
        index += 1

    index = 0
    display = "".join(temp_display)
    print(display)

    if display == chosen_word:
        print("You win!")
    else:
        guess = input("Guess a letter: ").lower()