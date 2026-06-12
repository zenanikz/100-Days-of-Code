#PAUSE 1
#Look at the code and answer the following questions:
"""
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()
"""

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
'''
    The for loop is running a variable through the range of 1 to 20
'''
# 2. When is the function meant to print "You got it"?
'''
    The function is meant to print "You got it" when i is 20
'''
# 3. What are your assumptions about the value of i?
'''
    My assumption of the value of i is that i will never be 20 in this loop because
    the loop will end when i reaches 19
'''


#PAUSE 2
# Fix the code so that the print statement executes.

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()