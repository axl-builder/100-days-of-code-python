#!/usr/bin/env python3
"""
Number Guessing Game.

A logic game where the user must guess a random number within a range,
with limited attempts based on difficulty.
"""

from random import randint
import sys

# Intentamos importar art de manera segura
try:
    from art import logo
except ImportError:
    logo = "--- GUESS THE NUMBER ---"

# --- CONFIGURACION (CONSTANTES) ---
# Al tener esto aqui, cambiamos las reglas del juego en un solo lugar.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100


def check_answer(user_guess: int, actual_answer: int, turns: int) -> int:
    """
    Checks answer against guess.
    
    Returns:
        int: The number of turns remaining.
    """
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        # Importante: Retornamos los turnos restantes incluso si gano,
        # para mantener la consistencia del tipo de dato (siempre devuelve int).
        return turns


def set_difficulty() -> int:
    """Prompts user for difficulty level and returns associated turns."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")


def game():
    """Main game logic."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    # Usamos f-strings con las constantes para que el texto siempre sea correcto
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    
    answer = randint(MIN_NUMBER, MAX_NUMBER)
    
    # Debugging: Util para desarrollo, comentar en produccion
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Validacion de entrada: Evitamos que el programa muera si no ingresan un numero
        try:
            user_input = input("Make a guess: ")
            guess = int(user_input)
        except ValueError:
            print("That's not a number! You lose a turn for invalid input.")
            # Penalizamos el error o simplemente continuamos (a tu eleccion)
            # turns -= 1 
            continue

        # Actualizamos los turnos usando la funcion
        turns = check_answer(user_guess=guess, actual_answer=answer, turns=turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            # Salimos de la funcion game(), terminando el juego actual
            return
        elif guess != answer:
            print("Guess again.")


if __name__ == "__main__":
    # Bucle para permitir reiniciar el juego sin ejecutar el script de nuevo
    while True:
        game()
        if input("Play again? (y/n): ").lower() != "y":
            print("Goodbye!")
            break