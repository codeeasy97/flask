# 1. Python Data Types

# a = "hello" sting
# b = 1 int
# c = 1.01 float

# list_number = [1,2,3,4,5] l = []

# tuple_number = (1,2,3,4,5) t = ()

# dict_number = {1:1,"y":"hello", 2:456} dict = {}

# set_number = {1,2,3,4,5} s = set()

#List

l = []
l.append(2)
l.append(3)
l.append(20)
l.append(22)
print(l)

l.pop()
print(l)

# SET
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

s.add(1)
print(s)

s.remove(1)
print(s)

#tuple

t = (1,2,3,4,5)
print(t)


#dict
d = {}
d[3] = "value"
d[2] = "value2"
print(d)

d.update({1:"value3"})
print(d)
print(d.get(3))