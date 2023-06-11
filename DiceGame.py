import random

name=input("What is your name? ")
print("Hello, ",name,"!")

print("Rolling dice...")
x=random.randint(1,6)
y=random.randint(1,6)

print("Die 1:",x)
print("Die 2:",y)

print("Total value:",x+y)

if x+y>7:
    print(name," won!")
else:
    print(name," lost.")