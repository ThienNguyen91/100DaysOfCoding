from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_machine = CoffeeMaker()
machine_menu = Menu()
money_machine = MoneyMachine()
def start():

    print(machine_menu.get_items())
    ask = input("What's is your order: ")
    if ask.lower() == "report":
        my_machine.report()
        money_machine.report()
        start()
    Drink = machine_menu.find_drink(order_name=ask.lower())
    if not Drink:
        return
    elif not my_machine.is_resource_sufficient(Drink):
        return
    elif not money_machine.make_payment(Drink.cost):
        return
    my_machine.make_coffee(Drink)
    start()


start()