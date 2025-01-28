def outer():
  a=5
  def inner():
    nonlocal a
    a=10
    print("inner function : ",a)
  inner()
  print("outer function : ",a)

outer()

