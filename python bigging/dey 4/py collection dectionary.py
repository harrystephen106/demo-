# dictionary => { }

# ex 1 
# 1

a={"name":"steve"}
print(a)

#2

a={
    "name":"steve",
    "age":1,
    "students":["pattu","jaffin"]
}
print(a.keys())
print(a.values())

# ex 2     update and add

# method 1
a={
    "name":"steve",
    "age":1,
    "students":["pattu","jaffin"]
}
a["age"]=2
print(a)

# method 2

a={
    "name":"steve",
    "age":1,
    "students":["pattu","jaffin"]
}
a.update({"age":2})
print(a)

# ex 3    delete
# method 1

a={
    "name":"steve",
    "age":1,
    "students":["pattu","jaffin"]
}
a.pop("age")
print(a)

# method 2

a={
    "name":"steve",
    "age":1,
    "students":["pattu","jaffin"]
}
del a["age"]               # we can delete complet dictiony with "del a" only
print(a)                   # but error will come because we delete all the dictionry to print the "a"

# ex 4

a={
    "name":"steve",
    "age":1,
    "students":["pattu","jaffin"]
} 
a.clear()                 # it used to clesr all the iteams in the dictionary
print(a)

# ex 5 
a={
    "name":"steve",
    "age":20,
    "students":["pattu","jaffin"]
}
print(a.get("age"))