#Tuple Introduction
t = (1,2,3)
print(t[-3])

print(t[0:2])

#update Tuple

t = (1,2,3,4)
list_1 = list(t)
list_1.append(5)
t = tuple(list_1)
print(t)





#Add Item

#1.Convert to list

#2. Add tuple to tuple
t1 = (1,2)
t2=(2,4)
t1+=t2
print(t1)

# Unpack Tuples:
t = (1,2,3)

# (t1,t2,t3) = t
# print(t1,t2,t3)

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

n = len(t)
i=0
while i< n:
    print(t[i])
    i = i + 1

    t1 = (1,1,2)
    t2 = (4,5)
    t3 = t1+t2
    print(t3.count(1))
    print(t1.index(2))
