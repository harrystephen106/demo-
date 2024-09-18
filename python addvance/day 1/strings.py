# strings

# ex 1

word1="steve is good boy"
word2="im really good boy"
print(word1)
print(word2)

#ex 2

para="""
hi im the steve 
im data scientist
im studied 
bye folks
"""
print(para)

#ex 3

word="hello"
print(word[3])     # this print the index value of array form
print(word[0])

# ex 4   slicing

# method 1

word3="hello world"
print(word3[1:5])
print(word3[3:7])

# method 2

word3="hello world"
print(word3[-5:-1])
print(word3[-9:-1])
print(word3[-10:-1])

# ex 5

# length calculat

word3="hello world this is new file word"
print(len(word3))

# ex 6

# strip 

word3="   hello world is my world     "
print(word3.strip())

# ex 7 (upper (),lower ())

w1="Im VERY good StudenT"
print(w1.upper())
print(w1.lower())

# ex 8 ( replace())

a="steven"
print(a.replace("ven","phen"))

# ex 9 (splite)

a="stephen"
print(a.split("e"))

# ex 10

n="hey in the main hey of hey of tha main page"
print("hey" in n)
print("hi" in n)