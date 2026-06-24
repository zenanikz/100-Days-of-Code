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


 
def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")



def user_drink_prompt():
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    return user_drink



def sufficient_resources(user_drink):
    u_ingredients = MENU[user_drink]["ingredients"]
    
    if resources["water"] < u_ingredients["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif "milk" in u_ingredients and resources["milk"] < u_ingredients["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif resources["coffee"] < u_ingredients["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False

    return True
    


def process_coins(user_drink):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickels = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total_given = quarters + dimes + nickels + pennies
    change = round(total_given - MENU[user_drink]["cost"], 3)

    if change >= 0:
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_drink}☕️. Enjoy!")
        resources["money"] += MENU[user_drink]["cost"]

        resources["water"] -= MENU[user_drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_drink]["ingredients"]["coffee"]
        if "milk" in MENU[user_drink]["ingredients"]:
            resources["milk"] -= MENU[user_drink]["ingredients"]["milk"]
    else:
        print("Sorry, that's not enough money. Money refunded.")  



def coffee_order():
    while True:
        user_drink = user_drink_prompt()
        if user_drink == "off":
            break
        elif user_drink == "report":
            report()
        else:
            if sufficient_resources(user_drink):
                process_coins(user_drink)



coffee_order()