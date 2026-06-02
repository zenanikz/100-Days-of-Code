#PAUSE 1. Fix the len() function so it has no more warnings or errors.
len("12345")


#PAUSE 2. Write out 4 type checks to print all 4 data types
int_check = 12
str_check = "12"
bool_check = True
float_check = 12.002

print(type(int_check), type(str_check), type(bool_check), type(float_check))


#PAUSE 3. Make this line of code run without errors
'''
print("Number of letters in your name: " + len(input("Enter your name")))
'''
print("Number of letters in your name: " + str(len(input("Enter your name\n"))))