def add_three_copies(my_list,data):
  for i in range(3):
    my_list.append(data)

def main():
  message = input("Enter your data:")  
  my_list = []
  print("List Before", my_list)  
  add_three_copies(my_list,message)
  print("list After ", my_list)
if __name__ == '__main__':
    main() 