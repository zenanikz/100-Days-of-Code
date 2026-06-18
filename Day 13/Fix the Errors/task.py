# PAUSE 1
# Fix the bug so that the print statement displays the correct value of age in the output area.
'''
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")
'''


try:
    age = int(input("How old are you?\n"))
    if age > 18:
        print(f"You can drive at age {age}.")
except ValueError:
    print("Your age isn't a valid number. Please fix that.")