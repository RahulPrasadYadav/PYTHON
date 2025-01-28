def outer():   #outer function 
  print("hello wolrd")
  def inner():   #inner funtion 
    print("hiii")
    # print("hiii")
  inner()
outer()
outer()



print("********************************************************************")


def outer_fun():
  print("hey outer")

  def inner_fun():
    print("hi inner ")
  print("outer Returns inner ")

  return inner_fun()

outer_fun()



def hi():
  pass
hi



print("-----------------------------------------------------------------------------")
def sum():
  x=1

  def inner_sum(a):
   print(a+x)
  inner_sum(2)

sum()


print("------------------------------------------------------------------")


def outerr():
  x=1
  def innerr(a):
    x=4
    print(a+x)
  print(x)
  innerr(2)
outerr()

