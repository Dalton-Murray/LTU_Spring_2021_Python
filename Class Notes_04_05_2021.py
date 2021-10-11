#####################
## Dalton Murray    #
## 04/05/20201      #
## Class notes      #
#####################


# Object-oriented approach
# Classes
# Create your objects using classes

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def setName(self, newName):
        self.name = newName

    def __str__(self):
        return "I am "+self.name

person1 = Person("John Smith", "dx1234")
person2 = Person("Rose Davidson", "vc1256")

# print(person2.getName(), person2.getID())

# 3 properties of classes
# Encapsulation - Add attributes and functionalities in 1 object
# Inheritance - 2 classes which can inherit/share attributes of a person
# Polymorphism

class Student(Person):
    def __init__(self, name, id):
        Person.__init__(self, name, id)
        self.GPA = 0

    def setGPA(self, gpa):
        self.GPA = gpa

    def getGPA(self):
        return self.GPA

class Employee(Person):
    def __init__(self, name, id, salary):
        Person.__init__(self, name, id)
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setSalary(self, newSalary):
        self.salary = newSalary

student1 = Student("Mohammad", "y123")

student1.setName("Sara")
print(student1.getName())

student1.setGPA(4)
print(student1.getGPA())

employee1 = Employee("Jessica", "gh6789", 50000)
print(employee1.getName(), employee1.getID())
print(employee1.getSalary())
employee1.setSalary(60000)
print(employee1.getSalary())

print(student1)