def count(s):
  u=0
  l=0
  for i in s:
    if i.isupper():
      u=u+1
    elif i.islower():
      l=l+1
    else:
      pass
  print("upper case",u)
  print("lower case",l)

# count("Hey")

s=str(input("Enter the string: "))

count(s)



