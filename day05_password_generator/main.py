"""
Usage:
$ python py_password_dict_version.py


You will be asked for how many letters, symbols, and numbers you want and whether you prefer
a shuffled (hard) password or grouped (easy) password.
"""


import random


# --- Data dictionary ---
CHAR_SETS = {
"letters": [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
],
"numbers": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
"symbols": ['!', '#', '$', '%', '&', '(', ')', '*', '+']
}




def get_positive_int(prompt):
"""Ask the user for a positive integer, repeating until valid input."""
while True:
value = input(prompt)
if value.isdigit():
return int(value)
print("Please enter a valid positive number (0, 1, 2, ...). Try again.")




def build_password(counts, shuffle=True):
"""Build a password using the provided counts for each character type.


counts: a dictionary like {'letters': 4, 'symbols': 2, 'numbers': 3}
shuffle: whether to randomize the order of characters (True = hard mode)
"""
password_chars = []


# Go through each category and add random choices
for key, count in counts.items():
if count > 0:
password_chars.extend(random.choices(CHAR_SETS[key], k=count))


# Shuffle if desired (hard mode)
if shuffle:
random.shuffle(password_chars)


# Return as a joined string
return ''.join(password_chars)




def main():
print("Welcome to the PyPassword Generator (dictionary version)!")


# Gather user preferences
counts = {
'letters': get_positive_int("How many letters would you like in your password?\n"),
'symbols': get_positive_int("How many symbols would you like?\n"),
'numbers': get_positive_int("How many numbers would you like?\n"),
}


# Choose mode (easy = grouped, hard = shuffled)
while True:
mode = input("Choose mode: type 'easy' (grouped) or 'hard' (shuffled):\n").strip().lower()
if mode in ('easy', 'hard'):
shuffle_mode = (mode == 'hard')
break
print("Invalid choice. Please type 'easy' or 'hard'.")


password = build_password(counts, shuffle=shuffle_mode)


print(f"Your password is: {password}")




if __name__ == "__main__":
main()
