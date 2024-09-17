# encapsulation 

# publice encapsulation variable

class company():
    def __init__(self):
        self.company="google"      # error will occur  becouse this line is privat variable to changed

c1=company()
print(c1.company)

# privat encapsulation variable

class company():
    def __init__(self):
        self.__company="google"
    def companyname(self):
        print(self.__company)  # this will get o/p  becouse this class method to call the variable

c1=company()
c1.companyname()

# proteted encapsulation variable

class company():
    def __init__(self):
        self._company="google"

class b(company):
    pass

b1=company()
print(b1._company)