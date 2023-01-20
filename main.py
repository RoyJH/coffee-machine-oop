from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable


running = True
my_menu = Menu()
my_machine = CoffeeMaker()
my_register = MoneyMachine()

while running:
    if my_machine.resources["water"] < 50 or my_machine.resources["coffee"] < 18:
        print("Insufficient resources to make any additional drinks.")
        print("Powering down...")
        running = False
        break
    menu_table = PrettyTable()
    menu_table.field_names = ["Drink Selection", "Cost"]
    menu_table.add_rows(
        [
            ["Latte", "$2.50"],
            ["Espresso", "$1.50"],
            ["Cappuccino", "$3.00"]
        ]
    )
    menu_table.align = "l"
    print(menu_table)
    print("Which drink would you like?")
    selection = input("Type selection: 'latte', 'espresso', 'cappuccino': ").lower()
    if selection == "off":
        running = False
    elif selection == "report":
        my_machine.report()
        my_register.report()
    else:
        drink = my_menu.find_drink(selection)
        if my_machine.is_resource_sufficient(drink):
            if my_register.make_payment(drink.cost):
                my_machine.make_coffee(drink)
            else:
                print(f"Insufficient resources to make a {drink.name}")
