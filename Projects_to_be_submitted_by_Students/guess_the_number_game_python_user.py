import random

def computer_guesses():
    print("Welcome to 'Guess the Number' Game! 🎲")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    
    low, high = 1, 100
    attempts = 0

    while True:
        # Computer guesses a number in the range
        guess = random.randint(low, high)
        attempts += 1
        
        # Asking user for feedback
        print(f"Is your number {guess}?")
        user_feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        # Processing user response
        if user_feedback == "h":
            high = guess - 1  # Adjust range
        elif user_feedback == "l":
            low = guess + 1  # Adjust range
        elif user_feedback == "c":
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts.")
            break  # Exit loop
        else:
            print("❌ Invalid input! Please enter 'h', 'l', or 'c'.")

# Running the game function
if __name__ == "__main__":
    computer_guesses()
