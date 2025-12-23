import string

try:
    import art
    print(art.logo)
except ImportError:
    print("--- CAESAR CIPHER ---")

ALPHABET = string.ascii_lowercase

def caesar(original_text, shift_amount, direction):
    """
    Procesa un texto usando el cifrado César.
    
    Args:
        original_text (str): El mensaje a procesar.
        shift_amount (int): Cantidad de desplazamiento.
        direction (str): 'encode' o 'decode'.
    """
    output_text = ""
    
    # Optimizacion: Si el shift es 105, solo nos interesa el resto de dividir por 26.
    shift_amount = shift_amount % len(ALPHABET)
    
    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in ALPHABET:
            output_text += letter
        else:
            # Buscamos el indice actual
            current_index = ALPHABET.index(letter)
            
            # Calculamos el nuevo indice
            new_index = current_index + shift_amount
            
            # Usamos modulo para asegurar que siempre este entre 0 y 25.
            # Python maneja indices negativos con modulo perfectamente.
            new_index %= len(ALPHABET)
            
            output_text += ALPHABET[new_index]
            
    print(f"Here is the {direction}d result: {output_text}")

def main():
    """Función principal que maneja el flujo del programa."""
    should_continue = True

    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        
        # Validacion basica de entrada
        if direction not in ["encode", "decode"]:
            print("Invalid direction. Please type 'encode' or 'decode'.")
            continue

        text = input("Type your message:\n").lower()
        
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Shift must be a number!")
            continue

        caesar(original_text=text, shift_amount=shift, direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
        if restart != "yes":
            should_continue = False
            print("Goodbye")


if __name__ == "__main__":
    main()