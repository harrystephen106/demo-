# ex 1

# instance method

class laptop:
    chargertype="C-TYPE"

    def __init__(self):
        self.barnd=""
        self.price= 34
    def setprice(self,price):    # many self function to call the variable is call instance method
        self.price=price
    def getprice(self):
        print(self.price)

hp=laptop()
hp.setprice(20000)
hp.getprice()

# ex 2

# class method

# method 1

class laptop:
    chargertype="C-TYPE"

    def __init__(self):
        self.barnd=""
        self.price=20000
    def getprice(self):
        print(self.price)
    def changeChargerType(cls):
        cls.chargertype="B_type"
        print("change type changed to B")

hp=laptop()
hp.getprice()

laptop.changeChargerType(laptop)

# method 2

class laptop:
    chargertype="C-TYPE"

    def __init__(self):
        self.barnd=""
        self.price= 34
    def setprice(self,price):    # many self function to call the variable is call instance method
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod
    def changeChargerType(cls):
        cls.chargertype="B_type"
        print("change type changed to B")

hp=laptop()
hp.setprice(20000)
hp.getprice()
laptop.changeChargerType()

# ex 3

# static methode

class laptop:
    chargertype="C-TYPE"

    def __init__(self):
        self.barnd=""
        self.price= 34
    def setprice(self,price):    # many self function to call the variable is call instance method
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod
    def changeChargerType(cls):
        cls.chargertype="B_type"
        print("change type changed to B")

hp=laptop()
hp.setprice(20000)
hp.getprice()
laptop.changeChargerType()