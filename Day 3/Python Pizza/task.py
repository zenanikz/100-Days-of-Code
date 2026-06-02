print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n").upper()
extra_cheese = input("Do you want extra cheese? Y or N:\n").upper()

pizza_total = 0

if size == "S":
    pizza_total += 15
    if pepperoni == "Y":
        pizza_total += 2
elif size == "M":
    pizza_total += 20
    if pepperoni == "Y":
        pizza_total += 3
elif size == "L":
    pizza_total += 25
    if pepperoni == "Y":
        pizza_total += 3
else:
    print("Something went wrong with your order, please try again")

if extra_cheese == "Y":
    pizza_total += 1

print(f"Your final bill is: ${pizza_total}.")



