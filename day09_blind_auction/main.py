#!/usr/bin/env python3
"""
Blind Auction Program.

This script facilitates a silent auction where users input their names and bids.
The highest bidder is determined and announced at the end.
"""

# Intentamos importar art, pero si no existe, el programa sigue funcionando (Fail-safe)
try:
    from art import logo
except ImportError:
    logo = "--- BLIND AUCTION ---"


def find_highest_bidder(bidding_record):
    """
    Determines the winner of the auction based on the highest bid.

    Args:
        bidding_record (dict): A dictionary where keys are names (str) 
                               and values are bid amounts (float).

    Returns:
        tuple: A tuple containing the winner's name (str) and the highest bid (float).
               Returns (None, 0) if the dictionary is empty.
    """
    highest_bid = 0.0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    return winner, highest_bid


def main():
    """
    Main function to handle user input and control the flow of the auction.
    """
    print(logo)
    bids = {}
    continue_bidding = True

    while continue_bidding:
        name = input("What is your name?: ").strip() # strip() elimina espacios accidentales
        
        # Validacion de entrada para evitar crashes si ponen texto en vez de numeros
        try:
            price = float(input("What is your bid?: $"))
        except ValueError:
            print("Invalid input. Please enter a number for the bid.")
            continue

        bids[name] = price

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        
        if should_continue == "no":
            continue_bidding = False
            # Capturamos los valores retornados por la funcion
            winner_name, highest_price = find_highest_bidder(bids)
            
            # Formateamos el precio a 2 decimales para que parezca dinero real
            print(f"The winner is {winner_name} with a bid of ${highest_price:.2f}")
            
        elif should_continue == "yes":
            # Metodo simple para limpiar pantalla
            print("\n" * 20)
        else:
            print("Invalid response. Continuing auction by default.")


if __name__ == "__main__":
    main()