"""
Band Name Generator
-------------------
Simple program that suggests a band name based on the user's city and pet name.
"""


def generate_band_name():
    """Ask the user for city and pet name, then return a suggested band name."""

    print("🎵 Welcome to the Band Name Generator 🎵\n")

    city = input("What's the name of the city you grew up in?\n").strip()
    pet = input("What's your pet's name?\n").strip()

    # Handle empty input gracefully
    if not city or not pet:
        print("\n⚠️  You must enter both a city and a pet name to generate a band name.")
        return

    band_name = f"{city} {pet}"
    print(f"\nYour band name could be: {band_name}")


if __name__ == "__main__":
    generate_band_name()

