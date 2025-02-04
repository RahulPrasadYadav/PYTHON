s="Rahul"
new=""

for i in s:
  if i.isupper():
    new+=i.lower()
  else:
    new+=i.upper()
print(new)
