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
}

def check(coffee):
    for each_ingredients in MENU[coffee]["ingredients"]:
        if resources[each_ingredients] < MENU[coffee]["ingredients"][each_ingredients]:
            return each_ingredients
    return True
def insert_coin(money_requirement):
    while True:
        try:
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            break
        except ValueError:
            print("Wrong value")
    total_money = (quarters * 25 + dimes * 10 + nickles * 5 + pennies) / 100
    return round(total_money - money_requirement, 2)
def make_coffee(coffee):
    for each_ingredient in MENU[coffee]["ingredients"]:
        resources[each_ingredient] -= MENU[coffee]["ingredients"][each_ingredient]
    return coffee

def start():
    Coffe_choose = input("What would you like? (espresso/latte/cappuccino): ")
    if Coffe_choose.lower() == "report":
        print(resources)
    if Coffe_choose.lower() == "off" or Coffe_choose.lower() not in ["espresso", "latte", "cappuccino"]:
        return

    #Check if enough ingredients, if not then ask for new coffee
    while True:
        is_enough = check(Coffe_choose)
        if is_enough in resources.keys():
            ask_continue = input(f"We don't have enough {is_enough} for your order, do you want to choose new coffee?, type 'yes' or 'no' ")
            if ask_continue != "yes":
                return
            Coffe_choose = input("What would you like? (espresso/latte/cappuccino): ")
        else:
            break
    #Insert coin
    have_charge = insert_coin(MENU[Coffe_choose]["cost"])
    if have_charge < 0:
        print("Sorry that's not enough money. Money refunded.")
        return
    #Everything has been successfully
    print(f"Here is ${have_charge} in change.")
    print(f"Here is your {make_coffee(Coffe_choose)} ☕️. Enjoy!")
    start()

start()



