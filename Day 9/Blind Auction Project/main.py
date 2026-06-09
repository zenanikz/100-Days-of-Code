from art import logo
print(logo)

bids = {}

# TODO-1: Ask the user for input
def user_input():
    bidder_name = input("What is your name?: ")
    bidder_price = int(input("What is your bid?: $ "))

# TODO-2: Save data into dictionary {name: price}
    bids[bidder_name] = bidder_price
    new_bids()


# TODO-3: Whether if new bids need to be added
def new_bids():
    new_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if new_bids == "yes":
        user_input()
    else:
# TODO-4: Compare bids in dictionary
        print(f"The winner is {max(bids, key=bids.get)} with a bid of ${max(bids.values())}")


user_input()