import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}



# TODO 3: Print the report 
def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")



# TODO 1: Prompt the user for their order
def user_drink_prompt():
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    return user_drink



def drink_order(user_drink):
    # TODO 2: Turn off the coffee machine
    if user_drink == "off":
        sys.exit()
    
    if user_drink == "report":
        report()
    else:
        return user_drink



# TODO 4: Check for sufficient resources
def sufficient_resources(user_drink):
    suff_water, suff_milk, suff_coffee, count = 0, 0, 0, 0
    u_ingredients = MENU[user_drink]["ingredients"]

    suff_water = resources["water"] - u_ingredients["water"]
    suff_coffee = resources["coffee"] - u_ingredients["coffee"]
    if user_drink != "espresso":
        suff_milk = resources["milk"] - u_ingredients["milk"]
    
    if suff_water < 0:
        print("Sorry, there is not enough water.")
        count += 1
    elif suff_milk < 0:
        print("Sorry, there is not enough milk.")
        count += 1
    elif suff_coffee < 0:
        print("Sorry, there is not enough coffee.")
        count += 1

    return count
    


# TODO 5: Process coins
def process_coins(user_drink, count):
    count = sufficient_resources(user_drink)

    if count > 0:
        pass
    else:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many dimes?: ")) * 0.10
        nickels = int(input("how many nickles?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01
        total_given = quarters + dimes + nickels + pennies
        change = round(total_given - MENU[user_drink]["cost"], 3)



        #TODO 6: Check if transaction is successful
        if change >= 0:
            print(f"Here is ${change} in change.")
            print(f"Here is your {user_drink}☕️. Enjoy!")
            resources["money"] += MENU[user_drink]["cost"]


            #TODO 7: Make coffee
            resources["water"] -= MENU[user_drink]["ingredients"]["water"]
            resources["coffee"] -= MENU[user_drink]["ingredients"]["coffee"]
            if user_drink != "espresso":
                resources["milk"] -= MENU[user_drink]["ingredients"]["milk"]
        elif change < 0:
            print("Sorry, that's not enough money. Money refunded.")  



def coffee_order():
    user_drink = user_drink_prompt()
    count = 0
    while user_drink != "off":
        if user_drink == "report":
            drink_order(user_drink)
            user_drink = user_drink_prompt()
        else:
            drink_order(user_drink)
            process_coins(user_drink, count)
            user_drink = user_drink_prompt()
        count = 0



coffee_order()