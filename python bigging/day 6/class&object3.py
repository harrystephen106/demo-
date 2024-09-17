# constroctor & function

# ex 1

class laptop:
    def __init__(self):
        print("demo")
    def display(self):
        print("display")

hp=laptop()

# ex 2

class laptop:
    def __init__(self):
        self.prize=0
        self.proc=" "
        self.ram=" "
    def display(self):
        print("ram",self.ram)
        print("prize",self.prize)

hp=laptop()
dell=laptop()

hp.prize=50000
hp.proc="i5"
hp.ram="16gb"

dell.prize=70000
dell.proc="i7"
dell.ram="16gb"

print(hp.prize)
hp.display()        
dell.display()