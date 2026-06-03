# Functions with input example

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")


#PAUSE 1 - Create a function with multiple inputs
def greet_with_names(name1, name2,name3):
    print(f"Hello {name1} {name2} {name3}")


first_name = input("Name one:\n")
second_name = input("Name two:\n")
last_name = input("Name three:\n")

greet_with_names(first_name, second_name, last_name)


#PAUSE 2 - Modify the function so that it prints the expected values.
'''
def greet_with(name, location)
    Hello name
    What is it like in location
'''

def greet_with(name, location):
    print(f"Hello {name}\nWhat is it like in {location}")


#PAUSE 3 - Call the greet_with() function using keyword arguments.

greet_with("Zenani", "Johannesburg")