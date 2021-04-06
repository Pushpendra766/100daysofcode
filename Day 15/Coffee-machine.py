from art import logo

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
    "profit": 0,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['profit']}")


def check_resource(ans):

    if MENU[ans]["ingredients"]["water"] >= resources["water"]:
        print("Sorry that's not enough water.")
        return False
    else:
        return True


def insert_coin():
    print("Please insert coins.")
    quarters = int(input("how many quarters? : "))
    dimes = int(input("how many dimes? : "))
    nickles = int(input("how many nickles? : "))
    pennies = int(input("how many pennies? : "))
    money = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    return money


def create_coffee(ans):
    resources['water'] -= MENU[ans]["ingredients"]["water"]
    resources['coffee'] -= MENU[ans]["ingredients"]["coffee"]
    if ans != "espresso":
        resources['milk'] -= MENU[ans]["ingredients"]["milk"]

    resources['profit'] += MENU[ans]["cost"]

    print(f"Here is your {ans} ☕ Enjoy!")


turn_off = False

while not turn_off:
    print(logo)
    ans = input("What would you like? (espresso/latte/cappuccino): ")

    if ans == 'report':
        report()
    elif ans == 'off':
        turn_off = True
    else:
        if check_resource(ans):
            money = insert_coin()
            if money >= MENU[ans]["cost"]:
                if money > MENU[ans]["cost"]:
                    change = round((money - MENU[ans]["cost"]),2)
                    print(f"Here is ${change} in change.")
                create_coffee(ans)
            else:
                print("Sorry that's not enough money. Money refunded.")
