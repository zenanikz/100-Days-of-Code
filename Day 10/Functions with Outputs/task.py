# PAUSE 1
# Create a function called format_name() that takes two inputs: f_name and `l_name'.

def format_name(f_name, l_name):
    # PAUSE 2
    # Use the title() function to modify the f_name and l_name parameters into Title Case.

    return f_name.title(), l_name.title()


first_name = input("First name\n")
last_name = input("Last name\n")

print(f"Hi {" ".join(format_name(first_name, last_name))}")
