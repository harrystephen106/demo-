# program 4

score=int(input("enter your score : "))
if(score<35):
    print("poor student")
if(score>35 and score<70):
    print("avarage student")
if(score>70):
    print("good student")

# elif program 

score=int(input("enter your score : "))
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("avarage student")
elif(score>70 and score<100):
    print("good student")
else:
    print("invalid input")