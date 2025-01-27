def fun (a=2,b=3,c=4):
  print(a,b,c)

fun(1)    #-> defual argument autometacally 



print("-----------------------------------")

def scores(Bigdata,haddop=45,spark=50):
  print(Bigdata,haddop,spark)


scores(71,77)
scores(65,spark=55)
scores(Bigdata=70,haddop=80,spark=90)