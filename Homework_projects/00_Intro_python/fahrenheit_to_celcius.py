def main() :
    fahrenheit = int(input("Enter Temperature in Fahrenheit : "))
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f'The Temperature conversion is : {fahrenheit}F = {celsius}C')
   

if __name__ == '__main__':
    main()