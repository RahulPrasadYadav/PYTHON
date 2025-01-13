number=[1,2,3,4,5]   #sum of al number 

sum=0

for var in number:
    sum=sum+var

print(sum)



for a in range(1, 10+1):
     a=a*2
     print("the table of 2 is:",a)



for num in [10,20,30,40,50]:
    if num>=20:
        print("the number is greater than 20:",num)
    else:
        print("the number is less than 20:",num)


dataset={"name":"python","version":3.7,"father":"Guido Van Rossum"}

for a in dataset:
    print(a.upper())



for a in (list(range(1,10))):
    print(a)