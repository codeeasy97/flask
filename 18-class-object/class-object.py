#Python Classes and Objects

#Create a Class
class MyClass:
    age = 15
    door = 2

#Create Object
obj = MyClass()
print(obj.age)

#The __init__() Function
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name+" ===="+str(self.age)

    def myfunc(self):
        return "hello"

obj1 = Person("ram", 27)
print(obj1)
print(obj1.myfunc())
obj1.name="mohan"
print(obj1.name)
#The __str__() Function

#Object Methods


#The self Parameter


#Modify Object Properties
