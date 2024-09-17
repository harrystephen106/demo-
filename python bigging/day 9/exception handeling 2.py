# program 1

try:
    a=int(input())
    b=int(input())
    c=input()
    print(c/a)
except ValueError as e:
    print("value error",e)
except TypeError as e:
    print("type error",e)

