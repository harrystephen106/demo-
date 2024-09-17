# inheritance and polymorphism used example

# program 1

class Shape():
    def area(self):
        return 0
    
class rectangle(Shape):
    def area(self):
        l=10
        b=20
        print(l*b)

r1=rectangle()
r1.area()

# program 2

class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grad):
        super().__init__(name)
        self.grade=grad

    def display(self):
        print(self.name,self.grade)

s1=student("steve","A")
s1.display()

# program 3

class vehical():
    def start(self):
        print("vehical start")

class car(vehical):
    def start(self):
        print("car started")
    
v1=vehical()
v1.start()

c1=car()
c1.start()

# program 4

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.department=dep
    def display(self):
        print(self.name,self.salary,self.department)

m1=manager("steve","30000","debuging")
m1.display()