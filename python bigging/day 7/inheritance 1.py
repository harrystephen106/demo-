# inheitance

# ex 1 
# mulitple inheritence

# method 1

class dad():
    def phone(self):
        print("dad phone")

class son(dad):
    def laptop(self):
        print("son laptop")
    
ram=son()
ram.phone()
ram.laptop()

# method 2

class dad():
    def phone(self):
        print("dad phone")

class mom():
    def sweet(self):
        print("mom sweet")

class son(dad,mom):
    def laptop(self):
        print("son laptop")
    
ram=son()
ram.phone()
ram.laptop()
ram.sweet()