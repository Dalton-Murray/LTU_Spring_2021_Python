#####################
## Dalton Murray    #
## 04/07/20201      #
## Class notes      #
#####################

# Polymorphism - Different forms
# Can work with different inputs
# print(len("Hello World!"))

# print(len([1, 3, 8]))

# Z=0 means optional/default value
# def myFunc(x, y, z=0):
#     print(x+y+z)

# myFunc(2, 3)
# myFunc(2, 3, 5)

class Person():
    def gender(self):
        print("Person can be male or female")

    def language(self):
        print("People talk in different languages")

class American(Person):
    def language(self):
        print("American people speak English")

class Chinese(Person):
    def language(self):
        print("Chinese people speak Chinese")

A = Person()
# A.language()

B = American()
# B.language()

C = Chinese()
# C.language()

for p in (A, B, C):
    p.language()