# Dictionaries

d = {"name":"code easy", "email":"example.com"}

print(d["name"])
print(d.get("name","code"))

print(d.keys())

d["name"] = "John Doe"
print(d)

d.update({"name":"example"})
print(d)

d["salary"] = 10000
print(d)

d.update({"age":30})
print(d)

d.pop("age")
print(d)

d.popitem()
print(d)

del d["email"]
print(d)

d.clear()
print(d)

#loop
d = {"name":"code easy", "email":"example.com"}

for i in d:
    print(i)

for i in d:
    print(d[i])

for i in d.values():
    print(i)

for i in d.keys():
    print(i)

for k,v in d.items():
    print(k,v)

# d2 = d
# print(d2)

d2 = d.copy()
print(d2)

d3 = dict(d)
print(d3)


dict1 = {
   "c1": {"name":"hello"},
   "c2":{"name":"hello"},
   "c3":{"name":"hello"}
}
print(dict1)
print(dict1["c1"]["name"])
