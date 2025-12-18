#!/usr/bin/env python3
"""
Blackjack Game Script.

A text-based implementation of the classic casino game Blackjack.
Manages game state, dealer logic, and score comparison.
"""

import random
import os
from typing import List, Union

# Intentamos importar el arte, fail-safe si no existe
try:
    from art import logo
except ImportError:
    logo = "--- BLACKJACK ---"

# --- CONSTANTES DE CONFIGURACION ---
# En Backend, estas constantes permiten cambiar las reglas del juego 
# sin tocar la logica interna.
DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACKJACK_THRESHOLD = 21
DEALER_STOP_THRESHOLD = 17
BLACKJACK_SCORE = 0  # Usamos 0 para representar un "Blackjack natural"


def clear_console():
    """Clears the console screen in a cross-platform way."""
    # En scripts profesionales, intentamos soportar Windows (nt) y Linux/Mac (posix)
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card() -> int:
    """
    Returns a random card from the deck.
    
    Returns:
        int: The value of the card drawn.
    """
    return random.choice(DECK)


def calculate_score(cards: List[int]) -> int:
    """
    Calculates the score of a hand of cards, adjusting for Aces.

    Args:
        cards (List[int]): A list of integers representing card values.

    Returns:
        int: The calculated score. Returns 0 explicitly for a Blackjack (2 cards totaling 21).
    """
    # Detectar Blackjack (Ace + 10) con solo 2 cartas
    if sum(cards) == BLACKJACK_THRESHOLD and len(cards) == 2:
        return BLACKJACK_SCORE

    # Manejo del As: Si nos pasamos de 21 y tenemos un 11, lo convertimos en 1.
    # Nota: remove() modifica la lista original. En Data Engineering a veces preferimos 
    # no mutar los inputs, pero para este juego es eficiente y correcto.
    if 11 in cards and sum(cards) > BLACKJACK_THRESHOLD:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score: int, computer_score: int) -> str:
    """
    Compares scores and determines the game outcome.

    Args:
        user_score (int): The player's final score.
        computer_score (int): The dealer's final score.

    Returns:
        str: A message describing the result (Win/Loss/Draw).
    """
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == BLACKJACK_SCORE:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == BLACKJACK_SCORE:
        return "Win with a Blackjack 😎"
    elif user_score > BLACKJACK_THRESHOLD:
        return "You went over. You lose 😭"
    elif computer_score > BLACKJACK_THRESHOLD:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """Main game logic execution."""
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Reparto inicial (2 cartas cada uno)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # --- TURNO DEL JUGADOR ---
    while not is_game_over:
        # Recalculamos score en cada iteracion por si cambio un As
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == BLACKJACK_SCORE or computer_score == BLACKJACK_SCORE or user_score > BLACKJACK_THRESHOLD:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # --- TURNO DE LA COMPUTADORA (DEALER) ---
    # El dealer debe pedir cartas si tiene menos de 17 y no tiene Blackjack
    # Nota: computer_score != 0 asegura que no pida carta si ya tiene Blackjack
    while computer_score != BLACKJACK_SCORE and computer_score < DEALER_STOP_THRESHOLD:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # --- RESULTADOS FINAL ---
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


def main():
    """Control loop to restart the game."""
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        clear_console()
        play_game()


if __name__ == "__ma