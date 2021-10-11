#####################
## Dalton Murray    #
## 03/31/20201      #
## Class notes      #
#####################

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def myFunc(self):
        print("My name is: "+self.name)
        
    def getYear(self):
        print(2021 - self.age)

person1 = Person("John Smith", 25, 5)
person2 = Person("Rose Davidson", 26, 5.5)
person1.myFunc()
person1.getYear()

print(person1.name)
print(person1.age)
# del person1.age
print(person1.height)

