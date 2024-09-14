# ex 4

# hybret inheritance

class dad():
    def money(self):
        print("dads money")

class land():
    def important(self):
        print("importent land")

class son1(dad,land):
    pass                 # the pass is empty class 

class son2(dad):
    pass

class son3(dad):
    pass

s2=son2()
s2.money()

s1=son1()
s1.important()