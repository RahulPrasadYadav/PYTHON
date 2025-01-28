def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)
  
print(fact(5))


print("------------------")


def counter(c):
  if c<=0:
    return c
  else:
    return c * counter(c-1)

print(counter(5))

