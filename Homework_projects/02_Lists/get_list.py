def main():
  lst = []

  val = input("Enterr the value: ")
  while val:
    lst.append(val)
    val = input("Enter the value: ")

  print("Here's the list:", lst)  
if __name__ == '__main__':
  main()    
