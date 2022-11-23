"""
1. Indentation
2. How To make Comments
3. variable declaration
4. Assign Many Values to Multiple Variables
5. Output Variables
6. Global Variables
"""

"""
my code is used to show Indentation
my code is used to show Indentation
my code is used to show Indentation
my code is used to show Indentation
my code is used to show Indentation
my code is used to show Indentation
"""


def mycode():
    print("hello")
    if 1 == 1:
        print("YES")
        if 2 ==2:
            print("NO")

def mycode1():
    print("hello 2")


mycode()
mycode1()

def multiply(a,b):
    c = a*b
    return c

def calculate(a,b):
    c = a + b
    return c

result = calculate(2,3)
out = multiply(result,2)
print(out)


# variables
print("hello hi bye")
example = True
print(type(example))



a,b,c = "code","lib", "hello"
print(a,b,c)

a = b = c = "lib"
print(a,b,c)

a = ["1","2","3"]
x,y,z = a
print(x,y,z)


x = 1
def hello():
    global x
    x = 2
    print(x)
hello()
print(x)