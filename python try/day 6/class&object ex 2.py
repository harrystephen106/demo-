# program 2

class Fruit:
    def __init__(self,col):
        self.color=col

apple=Fruit("red")
print(apple.color)

# method 2

class Fruit:
    def __init__(self,col,drow):
        self.color=drow

apple=Fruit("red","blue")
print(apple.color)

# program 3

class teacher:
    def __init__(self,nam,reg):
        self.name=nam
        self.regno=reg
    def display(self):
        print("name:",self.name)
        print("register no:",self.regno)
t1=teacher("amala",1939)
t2=teacher("jevitha",9176)
t1.display()
t2.display()

# program 4

# metod 1

class calculater:
    def __init__(self,a1,b1):
        self.a=a1
        self.b=b1
    def display(self):
        print("add:",self.a+self.b)
        print("sub:",self.a-self.b)
        
c=int(input("enter a: "))
f=int(input("enter b: "))
p1=calculater(c,f)
p1.display()

# method 2

class calculater:
    def add(self,a,b):
        print("add:",a+b)

p1=calculater()
p1.add(10,2)