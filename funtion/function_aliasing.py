def Hello_world(name):
  print("great ",name)

My_world=Hello_world    #alias convention 
Hello_world("cachine Learning")   #orginal name 

My_world("cython")   #alias name 

print(id(My_world))
print(id(Hello_world))


del Hello_world

