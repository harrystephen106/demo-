# ex 2

# multi level inheritence

class grandpa():
    def phone(self):
        print("greandpa phone")

class dad(grandpa):
    def money(self):
        print("dads money")

class son(dad):
    def laptop(self):
        print("sons laptop")

ram=son()
ram.laptop()
ram.money()
ram.phone()
 
d1=dad()
d1.phone()

# ex 3

# hararical inhertance

class dad():
    def money(self):
        print("dads money")

class son1(dad):
    pass                 # the pass is empty class 

class son2(dad):
    pass

class son3(dad):
    pass

s2=son2()
s2.money()