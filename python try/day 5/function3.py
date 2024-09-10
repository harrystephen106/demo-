# funtion use return key 

# ex return key
def valueofa():
    return 10
a=valueofa()
print(a)

# program 5
 # 1

s_username="steve"
s_password=1234

name=input("enter username :")
password=int(input("enter password :"))

def validate():
    if(s_username==name and s_password==password):
        print("corrct")
    else:
        print("wronge")

validate()

# 2
s_username="steve"
s_password=1234

name=input("enter username :")
password=int(input("enter password :"))

def validate():
    if(s_username==name and s_password==password):
        return True
    else:
        return False

a=validate()
print(a)

# program 6

def add(n1,n2):
    return n1+n2
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

added=add(a,b)
output=added*c
print(output)