print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n"))
people = int(input("How many people to split the bill?\n"))

total_per_person = float((bill/people) * ((100+tip)/100))

print(f"Each person should pay: ${total_per_person:.2f}")


