# IF ELSE Statement
a = 10
b = 12
c = 10

if a >= b:
    print("yes")
else:
    print("NO")


if a == b:
    print("a == b")
elif a > b:
    print("a>b")
elif a<b:
    print("a<b")
else:
    print("above cond not match")

if a == c:
    if a < b:
        if a  == b:
            print("hello")
        else:
            print("NO")

if a == b or a == c:
    print("yes")
else:
    print("NO")

if a == b and a == c:
    print("yes")
else:
    print("NO")

print("yessssssss") if a == c else print("No")