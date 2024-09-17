# program 1

# metod 1
class student:
    def __init__(self):
        self.name="steve harry"
        self.regno=123456
    def display(self):
        print("name:",self.name)
        print("register no:",self.regno)

s1=student()
s2=student()

s1.name="sathis"
s1.regno=82732

print(s1.name)
print(s1.regno)
print(s2.name)
print(s2.regno)

# method 2

class student:
    def __init__(self):
        self.name="steve harry"
        self.regno=123456
    def display(self):
        print("name:",self.name)
        print("register no:",self.regno)

s1=student()
s2=student()

s1.name="sathis"
s1.regno=82732

s2.name="steve"
s2.regno=93843

s1.display()
s2.display()