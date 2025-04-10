import random

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    """Determines the winner based on game rules."""
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    
    if (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors! 🪨📄✂")
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please try again.")
        return  # Stop the game if input is invalid

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)

# Running the game
if __name__ == "__main__":
    play_game()
