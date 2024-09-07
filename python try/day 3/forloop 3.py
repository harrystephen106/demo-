# program 7

sum=0
for i in range(1,6):
    sum=sum+i
print(sum) 

# program 8

a=[]
print("enter 5 numbers")
for i in range(5):
    b=int(input("Enter num "+str(i+1)+":"))
    a.append(b)
print(a)

# program 9

a=[]
print("enter 5 numbers")
for i in range(5):
    b=int(input("Enter num "+str(i+1)+":"))
    a.append(b)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum) 

# program 10

for i in range(1,6):      # find cube value of i
    print("the cube value of "+str(i)+":",i*i*i)