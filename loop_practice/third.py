
cnt=0
cnt1=0

for i in range(1,10):
    print(i,end="")
    if i%2==0:
        cnt+=1
    else:
        cnt1+=1
print("Number of even numbers: ",cnt)
print("Number of odd numbers: ",cnt1)


