#!/usr/bin/env python3
"""
Calculator App.

A robust calculator script that allows chaining operations.
Demonstrates usage of first-class functions and dictionary mappings.
"""

try:
    from art import logo
except ImportError:
    logo = "--- CALCULATOR ---"


# --- FUNCIONES PURAS (LOGICA) ---
# Aqui introducimos Type Hinting. Ayuda a los IDEs y a otros devs 
# a saber que datos esperar.

def add(n1: float, n2: float) -> float:
    """Returns the sum of n1 and n2."""
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    """Returns the difference between n1 and n2."""
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    """Returns the product of n1 and n2."""
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    """
    Returns the division of n1 by n2. 
    Note: Division by zero should be handled by the caller.
    """
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2


# Diccionario de operaciones
# Clave: Simbolo (str) -> Valor: Funcion (callable)
OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# --- FUNCION DE CONTROL (INTERFAZ) ---

def calculator_session():
    """
    Runs a single session of calculations. 
    Returns True if the user wants to start a NEW calculation, 
    False if they want to exit completely.
    """
    print(logo)
    
    # Validacion inicial
    try:
        num1 = float(input("What is the first number?: "))
    except ValueError:
        print("Invalid input. Starting over.")
        return True # Reinicia la sesion

    should_accumulate = True

    while should_accumulate:
        for symbol in OPERATIONS:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        
        # Validamos que la operacion exista
        if operation_symbol not in OPERATIONS:
            print("Invalid operation selected.")
            continue

        try:
            num2 = float(input("What is the next number?: "))
        except ValueError:
            print("Invalid number.")
            continue

        # Seleccionamos la funcion del diccionario y ejecutamos
        calculation_function = OPERATIONS[operation_symbol]
        
        try:
            answer = calculation_function(num1, num2)
        except ValueError as e:
            # Capturamos el error de division por cero que definimos arriba
            print(f"Error: {e}")
            continue

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            return True # Indica al bucle principal que reinicie


def main():
    """
    Main application loop. 
    Replaces recursion with a secure infinite loop.
    """
    app_running = True
    while app_running:
        # Ejecutamos la sesion. Si calculator_session devuelve True, el bucle sigue.
        # Podriamos agregar logica para salir completamente si devolviera False.
        calculator_session()


if __name__ == "__main__":
    main()