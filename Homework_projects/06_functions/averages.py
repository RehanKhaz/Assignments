def average(a:float, b:float):
  sum = a + b
  return sum / 2

def main():
  avg1 = average(0,10) 
  avg2 = average(8,10) 

  final_avg = average(avg1,avg2) 
 
  print("avg_1", avg1)   
  print("avg_2", avg2)   
  print("final", final_avg)  
if __name__ == '__main__':
  main() 