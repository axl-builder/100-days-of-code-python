#!/usr/bin/env python3
"""
Tip Calculator
Simple script to split a bill including tip between people.

"""

from typing import Tuple


def get_positive_float(prompt: str) -> float:
    """Solicita al usuario un número decimal positivo y lo devuelve como float."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Por favor ingresa un número mayor que 0.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Debes ingresar un número (ej: 23.50).")


def get_non_negative_int(prompt: str) -> int:
    """Solicita al usuario un entero no negativo y lo devuelve."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                print("Por favor ingresa un número entero >= 0.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero (ej: 15).")


def calculate_split(bill_total: float, tip_percentage: int, num_people: int) -> Tuple[float, float]:
    """
    Calcula el total con propina y cuánto paga cada persona.
    Devuelve una tupla (total_con_propina, pago_por_persona).
    """
    tip_amount = bill_total * tip_percentage / 100
    total_with_tip = bill_total + tip_amount

    if num_people <= 0:
        # Si se pone 0 personas, evitamos división por cero devolviendo el total general
        return total_with_tip, total_with_tip

    per_person = total_with_tip / num_people
    return total_with_tip, per_person


def format_currency(amount: float) -> str:
    """Formatea un número como moneda con dos decimales (ej: 12.50)."""
    return f"${amount:.2f}"


def main() -> None:
    """Flujo principal del programa."""
    print("Welcome to the tip calculator!\n")

    bill = get_positive_float("What was the total bill? $")
    tip = get_non_negative_int("What percentage tip would you like to give? (ej: 10, 12, 15) ")
    people = get_non_negative_int("How many people to split the bill? ")

    total, per_person = calculate_split(bill, tip, people)

    if people <= 0:
        print("\nNúmero de personas inválido (≤ 0). Mostrando el total con propina:")
        print(f"Total: {format_currency(total)}")
    else:
        print(f"\nTotal con propina: {format_currency(total)}")
        print(f"Cada persona debe pagar: {format_currency(per_person)}")


if __name__ == "__main__":
    main()
