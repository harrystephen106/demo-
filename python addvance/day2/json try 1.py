# ex 1

import json
a = '{"name":"steve","age":20}'

print(a)

b = json.loads(a)

print(b)
print(type(b))

# ex 2

import json
a = """{"name":"steve","age":20}"""

print(a)

b = json.loads(a)

print(b)
print(type(b))
print(b["name"])

# ex3

import json
a = """{"name":"steve","age":20}"""

print(a)

b = json.loads(a)

print(b)
print(type(b))

c = json.dumps(b)
print(c)
print(type(c))

# ex 4

import json
a = {"key1":(10,20,30)}
print(a)
b = json.dumps(a)
print(b)
print(type(b))