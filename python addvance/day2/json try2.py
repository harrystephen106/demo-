import json

jsonfile = json.load(open("data1.json"))

word = input("enter the word:")

def check(d):
    return jsonfile[d]

print(check(word))   