def main():
    speed_of_light = 300000 # in meter/second
    mass_in_kg = float(input('Enter the mass in Kg to convert. '))

    energy_in_joules = mass_in_kg * (speed_of_light ** 2)
    print(f'Calculating the Energy .... ')
    print(f'{energy_in_joules} Joules.')


if __name__ == '__main__':
    main()