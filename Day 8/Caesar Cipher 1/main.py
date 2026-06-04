alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# original_text = ""
# shift_amount = 0

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

index_original_text = []
new_text = []
index = 0
over_index = 0

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):
    original_text = text
    shift_amount = shift


# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

    for x in original_text:
        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        index = alphabet.index(x) + shift_amount
        if index > 25:
            over_index = index - 26
            index_original_text.append(over_index)
        else:
            index_original_text.append(index)

    for y in index_original_text:
        new_text.append(alphabet[y])

    print(f"Here is the encoded result: {"".join(new_text)}")


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)







