import random

def guess_the_number():
    print("Welcome to 'Guess the Number' Game! 🎲")
    
    # Random number selection between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Taking user input
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            # Checking conditions
            if guess < secret_number:
                print("Too low! Try again ⬆️")
            elif guess > secret_number:
                print("Too high! Try again ⬇️")
            else:
                print(f"🎉 Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                break  # Exiting the loop when correct guess is made
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Running the game function
if __name__ == "__main__":
    guess_the_number()
