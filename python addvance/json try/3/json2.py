import json

jsonfile = json.load(open("json1.json"))

word  = input("enter a word ")

def check(d):
    d = d.lower()
    if d in jsonfile: 
        return jsonfile[d]
    else:
        return "this word is not found , enter correct word"

print(check(word))