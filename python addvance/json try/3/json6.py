import json
from difflib import get_close_matches

jsonfile = json.load(open("json1.json")) 

word  = input("enter a word ")

def check(d):
    d = d.lower()
    if d in jsonfile: 
        return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys())) > 0:
        Choice = input(" did you mean %s , enter y for yes n for no " %get_close_matches(d,jsonfile.keys())[0])
        if Choice == "Y" or "y":
            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
        elif Choice == "N" or "n":
            return "this word is not found , enter correct word"
        else:
            return " please enter the wrong choice"
    else:
        return "this word is not found , enter correct word"

result = (check(word))

if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)