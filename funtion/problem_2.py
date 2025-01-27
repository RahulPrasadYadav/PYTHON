 #Write a Python function to sum all the numbers in a list.

def sum(arr):
  sum1=0
  for i in arr:
    sum1+=i
  return(sum1)

print(sum((8,2,3,0,7)))