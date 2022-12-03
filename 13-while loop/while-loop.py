# While Loop

i = 0
while i < 5:
    print(i)
    if i == 3:
        print("cond match")
        break
    i = i + 1

i = 0
while i < 5:
    
    i = i + 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print("===",str(i))
    i+=1
else:
    print("hello i")