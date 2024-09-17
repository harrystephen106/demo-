# function

# ex 1

def painter():
    print("painting")   # def function to call the painter

painter()

# program 1

def add():
    print("Additional")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a+b)
add()

def sub():
    print("Substraction")
    a=int(input("enter a:"))
    b=int(input("enter b:"))           # the sub(),add(),mul() funtion call on any place
    print(a-b)
sub()

def mul():
    print("Multiplication")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a*b)
mul()

def div():
    print("Divition")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)
div()
 
# ex 2

def painter(msg):
    print("message:",msg)     # this contition to "msg" have "painter" statment 

painter("paint my house")     # to print the variable 