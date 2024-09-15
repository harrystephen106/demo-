# own examble

class phone():
    def __init__ (self,brand,prize,chargtype):
        self.brand=brand
        self.price=prize                 # self = lava , brand = lava , price = 19000, charger = type-c
        self.chargertype=chargtype        # this metod to get the value
    def display(self):
        print("brand :",self.brand)
        print("prize :",self.price)
        print("chargertype :",self.chargertype)      

a=input("enter your phone brand : ")
b=int(input("enter your phone price : "))
c=input("enter your phone charger-type : ")

lava=phone(a,b,c)
lava.display()