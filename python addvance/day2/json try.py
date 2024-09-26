# ex 1
import json 
x = '{"name":"steve","age":"26","ip":"192.168.23.104"}'
y = json.loads(x)
print(y["ip"])

# ex 2

import json 
x = {
    "name":"steve",
    "age":"26",
    "ip":"192.168.23.104"
}
y = json.dumps(x)
print(y)
print(type(y))

# ex 3

import json
x={
    "name":"steve",
    "age":20,
    "married":False,
    "pets":3,
    "cars":[
        {"models":"bmw 230"},
        {"models":"ford edge"}
    ]
}

y=json.dumps(x,indent=5,separators=(" . "," = "))

print(y)

# ex 4

import json
x={
    "name":"steve",
    "age":20,
    "married":False,
    "pets":3,
    "cars":[
        {"models":"bmw 230"},
        {"models":"ford edge"}
    ]
}

y=json.dumps(x,indent=5,sort_keys=True)

print(y)