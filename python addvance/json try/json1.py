import json

jsonfile = json.load(open("json1.json"))

word  = input("enter a word ")

def check(d):
    return jsonfile[d]

print(check(word))  