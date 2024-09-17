# program 5

a=int(input("enter A value :"))
b=int(input("enter B value :"))
operation=input("add/sub/mul/div:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("invalid value")

# this is elif format used in the execution

# program 6

score=int(input("enter your score percentage :"))
if(score>=70):
    name=input("enter you name: ")
    age=input("enter your age")
    print("you are eligible")
else:
    print("you are not eligible")

# if the if condition is true to execut the name and age input 

# program 7

salary=int(input("enter your salary"))
age=int(input("enter your age"))
if(salary>=20000 or age<=25):
    loan=int(input("requred loan amount"))
    if(loan>50000):
        print("maximum loan ammount is 50000")
    else:
        print("you eligible for loan")
else:
    print("you are not eligible for loan")

# this concept is nested ifelse condition