#   List In Python

list1 = ["hello", "hye" , "bye", "teacher"]
print(list1)
n = len(list1)
print(list1[-2])

print(list1[0:4])
print(list1[0:]) #[start:end]

list2 = [1,2,3,4,5]
# list2[1] = 9
# print(list2)

# list2[1:3] = [100,101]
# print(list2)

# list2[1:3] = [6]
# print(list2)

# list2.insert(1, 19)
# print(list2)

# list2.append(12)

# list2.remove(1)
# list2.remove(2)

# list2.pop()
# del list2[2]

# list2.clear()

# for item in list2:
#     print(item, end=" ")

for item in range(len(list2)):
    print(list2[item], end=" ")

#while loop
# [1,2,3,4,5]
# n = len(list2)
# i = 0
# while i < n:
#     print(list2[i], end=" ")
#     i = i + 1

#list comprehension
# [print(item, end=" ") for item in list2 if item%2 == 0]

#sorting
list3 = ["boy", "alice", "nice", "car", "easy", "code"]
list3.sort()
list4 = [1,2,3,4,5]
list4.sort(reverse=True)
print(list4)




#copy

list6 = [1,2,3,4,5]
list7 = list6
print(list7)
list6.append(8)
print("list6",list6)
print("list7",list7)

list8 = list6.copy()
print("list8", list8)
list6.append(9)
print("list6", list6)
print("list8", list8)


list_1 = [1,2,3]
list_2 = list(list_1)
print(list_2)
list_1.append(5)
print("list_1",list_1)
print("list_2",list_2)

#join list

list_a = [1,1,2,3]
list_b = [4,5,6]

list_c = list_a+list_b
print(list_c)

# for item in list_b:
#     list_a.append(item)

# print("append method",list_a)

list_a.extend(list_b)
print("extend method", list_a)

print(list_a.index(3))