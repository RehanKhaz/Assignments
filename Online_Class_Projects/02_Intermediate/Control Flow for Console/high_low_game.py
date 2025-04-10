import random

NUM_ROUNDS = 5
score = 0 

def main():
    global score 

    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    for i in range(NUM_ROUNDS):
        print("Round:", i + 1)
        comp_num = random.randint(1, 100)
        my_num = random.randint(1, 100)

        print("Your number is", my_num)
        print("Computer's number is ??? (Hidden)",comp_num) 

        choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        higher_and_correct = choice == "higher" and my_num > comp_num
        lower_and_correct = choice == "lower" and my_num < comp_num

        if lower_and_correct  or  higher_and_correct:
            score += 1
            print("You have got 1 point! Your score is:", score)
            print("You were right! The computer's number was", comp_num)
        else:
            print("Aww, that's incorrect. The computer's number was", comp_num)  
            print("Your score is:", score)

    print("\nGame Over! Your final score is:", score) 

if __name__ == '__main__':
    main()