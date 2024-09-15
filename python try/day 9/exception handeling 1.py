# exception handeling(error handeling)

# compile time error
# ex

print("hi")
print("bye")
print("hey")    # if you type "printt("hey")" it is call compiler error

# logical error()
# ex

a=10
b=20
print(a+a)        # if of a+a is logical error . we need of a+b it is call logical error

#runtime error
#ex

a=int(input())
b=int(input())
print(a+b)        # if you type any str value in b or a value error will occure this is call runtime error

# program 1

# method 1

try:
    a=int(input())
    b=int(input())
    print(a+b) 
except Exception:
    print("something")
    
# method 2

try:
    a=int(input())
    b=int(input())
    print(a+b) 
except Exception as e:
    print("something",e)