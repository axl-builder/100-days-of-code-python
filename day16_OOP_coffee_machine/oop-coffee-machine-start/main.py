#!/usr/bin/env python3
"""
OOP Coffee Machine.

Main controller script that orchestrates the interaction between
Menu, CoffeeMaker, and MoneyMachine objects.
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
try:
    from art import logo
except ImportError:
    logo = "--- COFFEE MACHINE ---"


def main():
    # 1. Instanciamos los objetos (Contratamos a los empleados)
    # Usamos nombres en ingles para mantener consistencia con las Clases
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    print(logo)
    is_on = True

    while is_on:
        # Obtenemos las opciones dinamicamente del objeto menu
        options = menu.get_items()
        
        # Correccion: lower() y strip() van FUERA del input
        choice = input(f"What would you like? ({options}): ").lower().strip()

        if choice == "off":
            is_on = False
        elif choice == "report":
            # Delegamos la tarea de reporte a cada objeto
            coffee_maker.report()
            money_machine.report()
        else:
            # 2. Buscamos la bebida UNA sola vez
            # find_drink devuelve un objeto MenuItem (con .cost, .ingredients) o None
            drink = menu.find_drink(choice)
            
            # Verificamos si drink existe (find_drink suele manejar el print de error si es None)
            if drink:
                # 3. Verificamos recursos (La cafetera sabe si tiene suficiente)
                if coffee_maker.is_resource_sufficient(drink):
                    
                    # 4. Procesamos el pago y verificamos si fue exitoso
                    # make_payment devuelve True si pago, False si no.
                    # Pasamos drink.cost directamente del objeto drink.
                    if money_machine.make_payment(drink.cost):
                        
                        # 5. Hacemos el cafe (Solo si todo lo anterior paso)
                        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()