# PAUSE 1
# Play computer and go through the code line by line as if you were executing the code to figure out why 1994 does not work as expected.
# Then go ahead and fix the code.
'''
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
'''


year = int(input("What's your year of birth?\n"))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")