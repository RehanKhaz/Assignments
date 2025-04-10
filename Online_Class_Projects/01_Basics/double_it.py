def main():
  curr_value = int(input("enter the number"))
  while curr_value < 100:
    curr_value = curr_value * 2

    print(curr_value, end=" ")
if __name__ == '__main__':
  main()