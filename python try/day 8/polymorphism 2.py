# program 1

# method 1
class animal():
    def sound(self):
        print("animal makes sound")
                                        # this is useed method override function
class dog(animal):                        # like " def sound(self) " used in two classes
    def sound(self):
        print("dog barks")

a1=animal()
a1.sound()

b1=dog()
b1.sound()

# method 2

class animal():
    def sound(self):
        print("animal makes sound")
    
class dog(animal):                       
    def sound(self):                         # this is method over-riding
        print("dog barks")                 # repeat use of method in the class

class bird(animal):
    def sound(self):
        print("birds sing")

a1=animal()
a1.sound()

d1=dog()
d1.sound()

b1=bird()
b1.sound()