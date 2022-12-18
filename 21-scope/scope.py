# Python Scope
#Local Scope

def myfunc():
    x = 200
    print(x)
myfunc()

def myfunc():
    x = 1000
    def my2():
        print(x)
    my2()
myfunc()

#Global Scope
x = 100
def muglobal():
    print(x)
print(x)
muglobal()

#Global Keyword
def myf():
    global x
    x = 300
myf()
print(x)