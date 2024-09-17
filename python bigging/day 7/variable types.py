# ex 1

# instance variable  => if constracor of __init__ functions is call instance variable

class phone():
    def __init__ (self,brand,prize,chargtype):
        self.brand=brand
        self.price=prize                 # self = lava , brand = lava , price = 19000, charger = type-c
        self.chargertype=chargtype         # this metod to get the value
    def display(self):
        print("brand :",self.brand)
        print("prize :",self.price)
        print("chargertype :",self.chargertype)      

lava=phone("lava","19000","type-b")
lava.display()

# ex 2

# class variable  => we need one object in all the classes is called class variable

class phone():
    chargertype="type-c"   #  this is class variable
    def __init__ (self,brand,prize):   
        self.brand=brand                 # self = lava , brand = lava , price = 19000, charger = type-c 
        self.price=prize                 # this metod to get the value
    def display(self):
        print("brand :",self.brand)
        print("prize :",self.price)
        print("chargertype :",self.chargertype)      

lava=phone("lava","19000")
lava.display()

lenova=phone("lenova","20000")
lenova.display()