# set =>{ }

# ex 1

a={1,2,3,4,5,1,2}          # if run is it show {1,2,3,4,5}
print(a)                  # it is not show nay duplicate value

# ex 2

a={1,2,3,4,5}
a.add(6)              # the add() function to add any valuse in set  
a.add(7)
print(a)

# ex 3

a={1,2,3,4,5,6,7,8}
a.remove(5)              # the remove() function to remove any valuse in set  
a.remove(7)
print(a)

# ex 4

a={1,2,3,4,5,6,7,8}     # the pop() function to delete any valuse in set
a.pop()                # if you type pop() only it delete first value only
print(a)                # becouse set is un-ordered  

# ex 5

a={1,2,3,4,5}
b={5,6,3,2}   
a.update(b)
print(a) 