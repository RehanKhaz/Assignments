def main():
  name : str = input("What's your name? ")
  print(greet_name(name))

def greet_name(name):
   return "Greetings " + name + "!"
if __name__ == '__main__':
    main()     