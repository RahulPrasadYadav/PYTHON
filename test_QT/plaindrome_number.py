n=int(input("enter the number: "))
num=n
rev=0
while n>0:
  rev=rev*10+n%10
  n//=10

if num==rev:
  print("yes")
else:
  print("no")



# num=int(str(n)[::-1])

# if num==n:
#   print("palin")
# else:
#   print("Not")




