# program 2

# findevenorodd() use

def findevenorodd(b):
    if(b%2==0):
        print("even")
    else:
        print("odd")
a=int(input("enter a:"))
findevenorodd(a)

# program 3

def findpassorfail(b):
    if(b>=35):
        print("pass")
    else:
        print("fail")     # the "a" value of input take to findevenorodd to "b" to store it  input a=45
a=int(input("enter a:"))    # then b=45 change it then find the values
findpassorfail(a)

# program 4

def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)

a=int(input("enter a:"))   # the a , b value get from user
b=int(input("enter b:"))    # and "a" value go to r1  and "b" value go to r2
printrange(a,b)              # them fiind the range values