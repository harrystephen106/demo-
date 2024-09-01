# comparition to remainter 0 or not

# program 1

a=int(input())
if(a%3==0):
    print("divisible by 3")
else:
    print("no divisible by 3")

# a=15 then 15%3 remainder 0 == 0 is true.

# program 2

a=int(input())
if(a%3==0 and a%5==0):
    print("divisible by 3 and 5")
else:
    print("no divisible by 3 and 5")

# it divided by 3 and 5 on the condition
# if a=15 and 15%5 and 15%3 => 0==0 and 0==0 => true and true => true
# if a=12 and 12%5 and 12%3 => 2==0 and 0==0 => false and true =>false

