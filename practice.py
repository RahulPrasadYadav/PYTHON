years=int(input("Enter the Years "))

if (years %4==0 and (years%100!=0 or years%400==0)):
    print("leap years")
else:
    print("not leap  years")