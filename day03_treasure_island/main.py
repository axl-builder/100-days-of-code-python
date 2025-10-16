#!/usr/bin/env python3
"""
Juego de texto simple para practicar control de flujo e I/O en Python.
"""


WELCOME_ART = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''


def get_player_choice(prompt: str, valid_choices: tuple[str, ...]) -> str:
    """
    Solicita una entrada al jugador hasta que introduzca una opción válida.

    Args:
        prompt: Mensaje que se muestra al usuario.
        valid_choices: Tupla de opciones válidas en minúsculas (por ejemplo ('left','right')).

    Returns:
        La opción elegida (en minúsculas).
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Opción no válida: '{choice}'. Por favor elige: {', '.join(valid_choices)}.\n")


def first_decision() -> str:
    """Primera decisión del juego: cruce."""
    prompt = "Estás en un cruce. ¿A dónde quieres ir? (left/right)\n> "
    return get_player_choice(prompt, ("left", "right"))


def second_decision() -> str:
    """Segunda decisión del juego: lago."""
    prompt = (
        "Has llegado a un lago. En el centro hay una isla. "
        "¿Quieres esperar un barco o nadar? (wait/swim)\n> "
    )
    return get_player_choice(prompt, ("wait", "swim"))


def third_decision() -> str:
    """Tercera decisión del juego: puertas en la isla."""
    prompt = (
        "Llegas a la isla sano y salvo. Hay una casa con 3 puertas: "
        "red, yellow y blue. ¿Qué color eliges?\n> "
    )
    return get_player_choice(prompt, ("red", "yellow", "blue"))


def game_over(reason: str) -> None:
    """Imprime mensaje de 'Game Over' con la razón y termina."""
    print(f"{reason} Game Over.\n")


def win() -> None:
    """Imprime mensaje de victoria."""
    print("¡Felicidades! Has encontrado el tesoro. You Win!\n")


def play_game() -> None:
    """
    Controlador principal del juego: orquesta las decisiones y las consecuencias.
    Separar la lógica así ayuda a probar y mantener el código.
    """
    print(WELCOME_ART)
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")

    # Primera decisión
    choice1 = first_decision()
    if choice1 == "left":
        # Segunda decisión
        choice2 = second_decision()
        if choice2 == "wait":
            # Tercera decisión
            choice3 = third_decision()
            if choice3 == "red":
                game_over("Te quemaste en fuego.")
            elif choice3 == "blue":
                game_over("Fuiste devorado por bestias.")
            elif choice3 == "yellow":
                win()
            else:
                # Esto no debería ocurrir por la validación, pero dejamos un fallback.
                game_over("Elección desconocida.")
        else:  # swim
            game_over("Te atacaron las truchas.")
    else:  # right
        game_over("Caíste en un agujero.")


def main() -> None:
    """Punto de entrada del script. Permite que el juego se importe sin ejecutarse."""
    play_game()


if __name__ == "__main__":
    main()
