import time

def countdown_timer(seconds):
    """Starts a countdown timer from the given seconds."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end="\r")  # Overwrites the previous output
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("⏰ Time's up! 🚀")

# Get input from user
if __name__ == "__main__":
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print("❌ Please enter a valid number!")
