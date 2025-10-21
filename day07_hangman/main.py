# hangman.py
# ------------------------------
# Proyecto: Hangman (Ahorcado)
# Basado en el curso 100 Days of Code - Angela Yu
# Versión mejorada con buena estructura y legibilidad
# ------------------------------

import random
import hangman_words
import hangman_art

# Constante para las vidas máximas
MAX_LIVES = 6


def choose_word():
    """Elige una palabra al azar de la lista de palabras."""
    return random.choice(hangman_words.word_list)


def create_display(word):
    """Crea una lista con guiones bajos del mismo largo que la palabra."""
    display = []
    for _ in word:
        display.append("_")
    return display


def update_display(chosen_word, display, guess):
    """Actualiza el display reemplazando guiones por la letra acertada."""
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


def play_game():
    """Función principal que controla el flujo del juego."""
    print(hangman_art.logo)
    chosen_word = choose_word()
    display = create_display(chosen_word)
    lives = MAX_LIVES
    guessed_letters = []

    print("Palabra a adivinar: " + " ".join(display))

    game_over = False
    while not game_over:
        print(f"\nTienes {lives}/{MAX_LIVES} vidas restantes.")
        guess = input("Adivina una letra: ").lower()

        # Verificar si ya se adivinó esa letra
        if guess in guessed_letters:
            print(f"Ya intentaste con la letra '{guess}'. Prueba otra.")
            continue
        guessed_letters.append(guess)

        # Revisar si el intento fue correcto
        if guess in chosen_word:
            update_display(chosen_word, display, guess)
            print(f"¡Bien! La letra '{guess}' está en la palabra.")
        else:
            lives -= 1
            print(f"La letra '{guess}' NO está en la palabra. Pierdes una vida.")

        # Mostrar progreso actual
        print("Palabra: " + " ".join(display))
        print(hangman_art.stages[lives])

        # Revisar condiciones de fin
        if "_" not in display:
            game_over = True
            print("**************************** ¡GANASTE! ****************************")
        elif lives == 0:
            game_over = True
            print(f"*********************** PERDISTE :( La palabra era: {chosen_word} ***********************")


# Ejecutar el juego
play_game()
EOD
