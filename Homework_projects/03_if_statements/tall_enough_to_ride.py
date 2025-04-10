MINIMUM_HEIGHT: int = 50  # Minimum required height in cm

def main():
    while True:
        height = input("What is your height in centimeters? (Leaving it empty will exit the program): ")
        
        if height == "":
            print("Program is closed.")
            break
        
        try:
            height = float(height)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride! 🎢")
            else:
                print("You're not tall enough to ride, but maybe next year! 😊")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
      