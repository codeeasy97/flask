# Python Inheritance


# Create a Parent Class

class Person:#parent class
    def __init__(self, fname, lname):
        print("parent")
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)


class Student(Person):#child class
    def __init__(self, fname, lname, year):
        print("Student")
        # Person.__init__(self,fname, lname)
        super().__init__(fname, lname)
        self.year = year
    
    def printname(self):
        print(self.firstname,self.lastname,self.year)

# obj = Person("john", "doe")
# obj.printname()

obj = Student("john", "doe", 2022)
obj.printname()




# Create a Child Class
