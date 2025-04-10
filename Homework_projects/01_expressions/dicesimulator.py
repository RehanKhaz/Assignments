from random import randint

sides = 6

def roll_dice():
    die1: int = randint(1, sides)
    die2: int = randint(1, sides)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()