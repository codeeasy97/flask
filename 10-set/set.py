s = set()

s1 = {1,2,3,4}

for i in s1:
    print(i)

print(5 in s1)

s1.add(5)
print(s1)
s1.add(5)

print(s1)

s1={1,2}
s2={3,4}
# s1.update(s2)
# print(s1)

list_1 = [6,7]
s1.update(list_1)
print(s1)

s1 = {1,2,3,4}
# s1.remove(2)
# print(s1)

# s1.remove(5)
# print(s1)

s2 = {1,2,3,4}
# s2.pop()
# del s2
# print(s2)

for i in s2:
    print(i)

# while i < len(s2):
#     print()


s1 = {1,2}
s2 = {3,4}
# s3 = s1.union(s2)
# print(s3)

s1.update(s2)
print(s1)