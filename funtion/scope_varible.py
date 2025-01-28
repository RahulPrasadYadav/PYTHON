#local varible

def hello():
  a=1   #local varible 
  print(a)

hello()

# print(a)  # error becose a is local varible cant print 




#global varible 


b=1   #global varible 


def hi():
  print(b)

hi()

print(b)   #this is print why ... becose its a global  varible 




x=1000

def scope():
  x=12
  print(type(x))
  print(x+x)

scope()

def scope1():
  y=200
  print(type(y))
  print(x+y)

scope1()


z=1
def compute():
  global z
  for i in (1,2,3):
    print(i,end=" ")
    z+=1

compute()
print(z)


