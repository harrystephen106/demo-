# list => []

# ex 1

a=[1,2,3,4,5]
a.append(True)           # if you add any type of data in list type append condition
a.append("steve")        # type any type of data in list 
print(a)

# ex 2

a=[1,2,3,4,5]
a.insert(0,11)         # if you insert (0,11) 0-> is index no  11-> is insert number
print(a)

# ex 3

a=[1,2,3,4,5]          # if you need replace any number in list
a[0]=11                #  the a[0] -> is index num  11 -> is add number
print(a)

# ex 4

a=[1,2,3,4,5]        # if you delete any nummber in list
a.pop(4)             # the  pop -> is deleted condition   4 -> is index num
print(a)             # if you type a.pop() only it delete last value in list another 
                                #if two a.pop() type it delete last two value

# ex 5

a=[1,2,3,4,5]          # this condition is a and b 
b=[9,10,11,12]          # the extend condition is add or merge the two list on one list
a.extend(b)              # the b list is merged to a list 
print(a)