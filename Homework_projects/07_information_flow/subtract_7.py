def main():
  num:int = 7
  num = subtract_7(num)
  print("this should be zero: ", num)

def subtract_7(num):
  num = num -7
  return num  
if __name__ == '__main__':
  main()   