from random import randint;
def main():
    num_sides = 6;
    first_dice = randint(1, num_sides)
    second_dice = randint(1, num_sides)
    total = first_dice + second_dice ;
    
    print(f'Dice have {num_sides} sides each.')
    print(f'First Dice is {first_dice}.')
    print(f'Second Dice is {second_dice}.')
    print(f"Total is {total}.")
    

if __name__ == '__main__':
    main()