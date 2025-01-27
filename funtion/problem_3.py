#Write a Python function to multiply all the numbers in a list.

def multiple(arr):
  total=1
  for i in arr:
    total*=i
    return total

print(multiple((8, 2,)))  