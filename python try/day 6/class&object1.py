# classes & objects

# ex 1

class goa:
    def party(self):
        print("lets party....")      # the class is set of variable or fuctions
    def beach(self):
        print("enjoing beach life")  

ramash=goa()         # ramash is object 
surash=goa()           # goa is class it call the goa use "goa()"

ramash.party()       # and the object of ramash is call party function 
surash.beach()

# ex 2


class goa:
    name=" "
    drink=" "
    def party(self):
        print("lets party....")     
    def beach(self):
        print("enjoing beach life")  

ramash=goa()       
surash=goa()          

ramash.name="ramash"
surash.name="surash"

ramash.drink="yes"
surash.drink="no"

print(ramash.name)
print("drink:",ramash.drink)
print(surash.name)
print("drink:",surash.drink)

ramash.party()
surash.beach()