#!/usr/bin/env python3

import random

# ASCII art para las opciones
ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Lista con las opciones posibles
options = [ROCK, PAPER, SCISSORS]
names = ["Rock", "Paper", "Scissors"]


def get_user_choice():
    """
    Pide la elección del usuario.
    Devuelve 0, 1 o 2 según la opción elegida.
    Si el usuario escribe 'q', se lanza KeyboardInterrupt para salir del juego.
    """
    prompt = (
        "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"
        "(or 'q' to quit): "
    )
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == "q":
            raise KeyboardInterrupt  # Permite salir del juego limpiamente

        if user_input in ["0", "1", "2"]:
            return int(user_input)

        print("Invalid choice. Please enter 0, 1, 2 or 'q' to quit.")


def get_computer_choice():
    """Devuelve un número aleatorio entre 0 y 2."""
    return random.randint(0, 2)


def determine_winner(user, computer):
    """
    Determina el resultado del juego:
    - "win" si el usuario gana
    - "lose" si el usuario pierde
    - "draw" si empatan
    """
    if user == computer:
        return "draw"

    # Lógica de victoria del jugador
    if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (
        user == 2 and computer == 1
    ):
        return "win"

    return "lose"


def print_round_result(user_choice, computer_choice, result):
    """Imprime las elecciones y el resultado de la ronda."""
    print(f"\nYou chose: {names[user_choice]}")
    print(options[user_choice])
    print(f"Computer chose: {names[computer_choice]}")
    print(options[computer_choice])

    if result == "win":
        print("You win! 🎉\n")
    elif result == "lose":
        print("You lose. 😢\n")
    else:
        print("It's a draw. 🤝\n")


def main():
    """Función principal del juego."""
    print("Welcome to Rock, Paper, Scissors!\n")

    try:
        while True:
            try:
                user_choice = get_user_choice()
            except KeyboardInterrupt:
                print("\nThanks for playing — goodbye!")
                break

            computer_choice = get_computer_choice()
            result = determine_winner(user_choice, computer_choice)
            print_round_result(user_choice, computer_choice, result)

    except (EOFError, KeyboardInterrupt):
        print("\nSession ended. Bye!")


if __name__ == "__main__":
    main()
