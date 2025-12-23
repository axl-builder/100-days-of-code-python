#!/usr/bin/env python3
"""
Higher Lower Game.

A game where the user guesses which celebrity has more Instagram followers.
Demonstrates dictionary manipulation and game loops.
"""

import random
import os

# Manejo de imports seguros
try:
    from art import logo, vs
    from game_data import data
except ImportError:
    print("Error: Missing 'art.py' or 'game_data.py'.")
    logo = "--- HIGHER LOWER ---"
    vs = " vs "
    data = [] # Evita crash si no hay datos, aunque el juego no funcionara


def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def format_data(account):
    """
    Takes the account dictionary and returns the printable format.
    
    Args:
        account (dict): A dictionary containing name, description, and country.
        
    Returns:
        str: Formatted string like 'Shakira, a Musician, from Colombia'.
    """
    name = account["name"]
    descr = account["description"]
    country = account["country"]
    return f"{name}, a {descr}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """
    Checks if the user's guess is correct.

    Returns:
        bool: True if correct, False otherwise.
    """
    if a_followers > b_followers:
        # Si A tiene mas, el usuario gana si eligio 'a'
        return guess == "a"
    else:
        # Si B tiene mas (o igual), el usuario gana si eligio 'b'
        return guess == "b"


def main():
    """Main execution loop."""
    score = 0
    game_should_continue = True
    
    # Seleccion inicial: Elegimos una cuenta aleatoria para A
    account_a = random.choice(data)
    
    print(logo)

    while game_should_continue:
        # Generamos la cuenta B
        account_b = random.choice(data)

        # Validacion: Asegurar que A y B no sean iguales
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Input del usuario
        guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

        # Extraemos los seguidores para comparar
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        
        # Verificamos la respuesta
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Limpiamos pantalla para la siguiente ronda (Mejora de UI)
        clear_console()
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            
            # LOGICA CLAVE: El ganador B se convierte en el nuevo A
            # Esto da continuidad al juego
            account_a = account_b
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == "__main__":
    main()