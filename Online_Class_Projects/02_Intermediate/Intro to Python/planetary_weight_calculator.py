# Constants for planetary gravity multipliers
GRAVITY_CONSTANTS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    # Get weight and planet input from user
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

    # Get gravity constant for the selected planet
    if planet in GRAVITY_CONSTANTS:
        planetary_weight = earth_weight * GRAVITY_CONSTANTS[planet]
        rounded_weight = round(planetary_weight, 2)
        print(f"The equivalent weight on {planet}: {rounded_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
