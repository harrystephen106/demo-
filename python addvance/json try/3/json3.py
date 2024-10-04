import json
from difflib import get_close_matches

jsonfile = json.load(open("json1.json")) 

word  = input("enter a word ")

def check(d):
    d = d.lower()
    if d in jsonfile: 
        return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys())) > 0:
        return " did you mean %s " %get_close_matches(d,jsonfile.keys())
    else:
        return "this word is not found , enter correct word"

print(check(word))