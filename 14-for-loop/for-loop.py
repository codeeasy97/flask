#For Loop

list_1 = [1,2,3,4,5]
for x in list_1:
    print(x)

str_1 = "hello"
for x in str_1:
    if x == "e":
        break
    print(x, end=" ")

for x in list_1:
    if x == 3:
        continue
    print(x, end=" ")

for x in range(0,len(list_1)):
    print(list_1[x], end=" ")
print("\n")
for x in range(0,6, 2):
    print(x)
else:
    print("end loop")

for x in range(0,6):
    for y in range(0,2):
        print(x, y)

for x in range(0,6):
    pass

if 1 == 1:
    pass