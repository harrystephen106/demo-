# polymorphism

# ex 1
# method 1

def add(a=10):
    print(a)

add()

# method 2

def add(a=10):
    print(a)

add(50)

# method 3

def add(a,b,c=0):
    print(a+b+c)

add(2,3)
add(5,3,4)

# my own example

def add(a=0,b=0,c=0):
    print(a+b+c)
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
add(a,b)
add(b)
add(a,b,c)