# Lec - 16 Python Lambda

#sum of two function
# lambda arg: expression

result = lambda a,b: a+b
print(result(2,3))

#why and whrere to use lambda

def myfunc(n):
    return lambda a: a*n

mul = myfunc(2)
print(mul(4))

#lambda vs normal function

def sum(a,b):
    return a+b

print(sum(2,3))

sum = lambda a,b:a+b
print(sum(4,5))

#use filter() with lambda vs normal function

ages = [5,6,7,8,9,22,26,30,90]
def myage(x):
    if x < 18:
        return False
    else:
         return True

adult = filter(myage, ages)
print(list(adult))

adult = list(filter(lambda x : x > 18, ages))
print(adult)

#use map() with lambda vs normal function

def addition(n):
    return n + n

number = (1,2,3,4,5)
result = map(addition, number)
print(list(result))

add_list = list(map(lambda n: n + n, number ))
print(add_list)

#use lambda with if..else

minimum = lambda x, y: x if x < y else y 
print(minimum(2,3))

def minimum1(a,b):
    if a < b:
        return a
    else:
        return b

print(minimum1(4,5))