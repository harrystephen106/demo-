# ex prog

for i in range(1,6):
    for j in range(1,3):
        print(j,"apple")

# program 1

for i in range(1,3):
    print("week:"+str(i))
    for j in range(1,4):
        print("day :"+str(j))

# program 2

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end="")
    


# program 3

n = 5                       # Number of rows
for i in range(1, n + 1):   # Loop through each row
    for j in range(i):      # In each row, print 'i' stars
        print('*', end='')  # Print stars, stay in the same line
    print()                 # After each row, move to the next line