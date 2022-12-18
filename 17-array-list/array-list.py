# Python Array/List
name1 = "ram"
name2 = "rahul"
name3 = "neeraj"

name = ["ram", "rahul", "neeraj"]
#Access Element of an array/list
print(name[0])
#modify value of first item
name[1] = "ravi"
print(name)

#length of an array/list

print(len(name))

# Loop an array/list

for x in name:
    print(x)

# adding element to array/list

name.append("pawan")
print(name)
# remove element from array/list

name.pop(1)
print(name)

name.remove("ram")
print(name)
#delete element by value

#reverse a list
name.reverse()
print(name)