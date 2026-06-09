# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "\"", "|", "\\", "<", ",", ">", ".", "?", "/", "~", "`", "±", "§"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

index_original_text = []
new_text = []
index = 0
new_index = 0


def decrypt(original_text, shift_amount):
    for x in original_text:
        if x in symbols or x in numbers or x == " ":
            index_original_text.append(x)
        else:
            index = alphabet.index(x) - shift_amount
            if index < 0:
                new_index = index + 26
                index_original_text.append(new_index)
            else:
                index_original_text.append(index)

    for y in index_original_text:
        if y in symbols or y in numbers or y == " ":
            new_text.append(y)
        else:
            new_text.append(alphabet[y])

    print(f"Here is the decoded result: {"".join(new_text)}")


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in symbols or letter in numbers or letter == " ":
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        decrypt(original_text, shift_amount)
    elif encode_or_decode == "encode":
        encrypt(original_text, shift_amount)

# TODO-3: Can you figure out a way to restart the cipher program?
    restart = input(f"Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "yes":
        game()
    elif restart == "no":
        print("Goodbye")


def game():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("No such command exists.")
    # if direction == "encode" or direction == "decode":
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

game()