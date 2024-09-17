# tuple => ( )

# ex 1

a=(1,2,3,4,5)         # this is simple tuple prog
print(a)
  
# ex 2

a=(1,2,3,4,5)         # if you run this ex 2 program 
a[0]=10               # then add index to insrt any value
print(a)              # it show tuple connot support any object to show

# ex 3

a=(1,2,3,4,5)
b=list(a)           # we casting the tuble object 
b.pop(3)             # then pop the index values
print(a)
print(b)