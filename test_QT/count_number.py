n=int(input("enter the number "))

cnt=0


while n>0:
  digit=n%10
  n=n//10
  cnt=cnt+1

print(cnt)
