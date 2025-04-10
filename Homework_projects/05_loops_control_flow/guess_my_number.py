import random 

def main():
    secret_number = random.randint(1, 99)


    guess = int(input('Enter the number you guessed: '))


    while guess != secret_number:
        if guess < secret_number:
            print('Too Low!')
        if guess > secret_number:
            print('Too High!')
        guess = int(input('Enter the number you guessed: '))
    print('You got it! The number was', secret_number)
        
if __name__ == '__main__':
    main()   