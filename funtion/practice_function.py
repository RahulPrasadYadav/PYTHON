def myFun(*args):
  pylist=[]
  for i in args:
    pylist.append(i*2)
  return pylist

input_num=[1,2,3,4,5]

print(myFun(*input_num))