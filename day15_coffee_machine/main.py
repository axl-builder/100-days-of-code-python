#!/usr/bin/env python3
"""
Coffee Machine Program.

Simulates a coffee machine logic processing resources, coins, and transaction handling.
"""

# Import seguro
try:
    from art import logo
except ImportError:
    logo = "--- COFFEE MACHINE ---"

# CONSTANTES
# En backend, las configuraciones fijas van en mayusculas al inicio.
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# Estado inicial de recursos
starting_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resources, money):
    """Prints the current state of resources and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml") # .get() evita errores si no hay leche
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def is_resource_sufficient(order_ingredients, current_resources):
    """
    Returns True when order can be made, False if ingredients are insufficient.
    
    Args:
        order_ingredients (dict): Ingredients required for the drink.
        current_resources (dict): Resources currently in the machine.
    """
    # Iteramos dinamicamente sobre lo que pide la bebida.
    # No necesitamos una lista externa de ingredientes.
    for item in order_ingredients:
        if order_ingredients[item] > current_resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Prompts the user for coins and returns the total amount.
    """
    print("Please insert coins.")
    total = 0.0
    for coin, value in COIN_VALUES.items():
        try:
            # Input validation basico
            count = int(input(f"How many {coin}?: "))
            total += count * value
        except ValueError:
            print(f"Invalid input for {coin}, counting as 0.")
            continue
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Return True when the payment is accepted, or False if money is insufficient.
    Also handles the change logic.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients, current_resources):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        current_resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def main():
    """Main program flow."""
    # Inicializamos variables de estado
    money_profit = 0.0
    # Copiamos el recurso inicial para no modificar la constante original (Buena practica)
    resources = starting_resources.copy() 
    is_on = True

    print(logo)

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        if choice == "off":
            is_on = False
            print("Turning off. Goodbye!")
        elif choice == "report":
            print_report(resources, money_profit)
        elif choice in MENU:
            drink = MENU[choice]
            
            # 1. Verificar Recursos
            if is_resource_sufficient(drink["ingredients"], resources):
                
                # 2. Procesar Pago (Solo si hay recursos)
                payment = process_coins()
                
                # 3. Verificar Transaccion
                if is_transaction_successful(payment, drink["cost"]):
                    
                    # 4. Hacer Cafe (Solo si se pago correctamente)
                    make_coffee(choice, drink["ingredients"], resources)
                    money_profit += drink["cost"]
        else:
            print("Invalid selection. Please choose a drink from the menu.")


if __name__ == "__main__":
    main()