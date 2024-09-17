# super keywords

# method 1

class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class A")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("you are in class B")

a1=b()

# method 2

class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class A")

class b():
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("you are in class B")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("c")

    def display(self):
        print("you are in class C")

obj1=c()
