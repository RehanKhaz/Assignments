def main():
    perpendicular = float(input('Enter the length of Perpendicular : '))
    base = float(input('Enter the length of Base : '))
    hypotenuse = ((perpendicular ** 2) + (base **2))**1/2
    print(f'The Hypotenuse of Right Angle Triangle is {int(hypotenuse)}.')

if __name__ == '__main__':
    main()