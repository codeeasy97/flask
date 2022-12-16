#python function
print("hello")
print("wow")

def my_function():
    print("bye")

my_function()
#Arguments / parameter

def my_function_1(p1,p2):
    print(p1, p2)
my_function_1("john", "doe")
#Arbitrary Arg
def my_function_1(*args):
    print(args[0], args[1],args[2], args[3])
my_function_1("john", "doe","john", "doe")
#Keywords Arg
def my_function_1(**kargs):
    print(kargs["name"])
    print(kargs["email"])
my_function_1(name="john", email="john@gmail.com", company="google", age="20")

#Default parameter value
def my_func(country="India"):
    print(country)

my_func("USA")
#pass list as args
def my_func_1(my_list):
    for x in my_list:
        print(x)

my_func_1([1,2,3,4,5])

#Return value
def my_func_12(num):
    return 10*num

out = my_func_12(4)
print(out)
print(my_func_12(5))
#pass statement
def my_func_22():
    pass

#recursion
def my_fuc(p1):
    if p1>0:
        print("called")
        my_fuc(p1-1)

res = my_fuc(3)


