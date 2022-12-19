# Python JSON

#JSON in Python
import json

#Parse JSON - Convert from JSON to Python
x = '{"name":"ram", "age":24}'
print(type(x))

y = json.loads(x)
print(y["name"])
#Convert from Python to JSON
x = {"name":"varun", "age":32}
y = json.dumps(x)
print(type(y))

#Format the Result
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x, indent=4)
print(y)
#Order the Result

y = json.dumps(x, indent=4, sort_keys=True)
print(y)