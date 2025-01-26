s=str(input("Enter a string: "))

d=l=0

for i in s:
  if i.upper():
    d=d+1
  elif i.lower():
    l=l+1
  else:
    pass

print("digit",d)
print("letter",l)