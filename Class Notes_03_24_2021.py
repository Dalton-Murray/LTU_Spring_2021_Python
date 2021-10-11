#####################
## Dalton Murray    #
## 03/24/20201      #
## Class notes      #
#####################

student = {
    "name": "John Smith",
    "age": "25",
    "grades": [87, 90]
}

# Dictionary is mutable
# Can't have duplicate keys

print(student["name"])
print(10*"*")

# One type of dictionary has index and one doesn't
# One also has order and one doesn't

print(type(student))
print(10*"*")

student["name"] = "Rose Davidson"
print(student)

student.update({"age":48})
print(student["age"])

student["id"] = 110
student.update({"email":"John@gmail.com"})

print(student)

# student.popitem()
# print(student)

# del student["age"]
# print(student)

# student.clear()
# print(student)

print(10*"*")
for i in student:
    print(i, student[i])
print(10*"*")

print(student.keys())
print(list(student.values()))

print(10*"*")
for i in student.keys():
    print(i)
print(10*"*")

print(list(student.items()))

for k, v in student.items():
    print(k, v)
print(10*"*")

# Must use .copy in order to make a real copy
# and not just a reference
new_student = student.copy()
new_student = dict(student)

student = {
    "name":"John Smith",
    "age":"25",
    "grades":{"math":87, "art":100}
}
print(student["grades"]["math"])

print(student.get("grades"))

student.pop("name")
print(student.pop("name", "Key does not exist"))
print(student)

# Updating a dictionary
numbers = [1, 2, 3, 4, 5]
squares = {
    "numbers":numbers
}
print(squares)

numbers2 = []
for i in range(1, 10):
    numbers2.append(i)
squares["numbers"] = numbers2
print(squares)
print(10*"*")

# Notes
numbers = [1, 2, 3, 4, 5]

# Gets square if the number is divided by 2 
# and remainder is 0 then it is even
squares = {i: i**2 for i in numbers if i % 2 == 0}
print(squares)

objects = ["door", "pen", "board", "orange"]
str_length = {i: len(i) for i in objects}
print(str_length)

dict1 = {
    "A": 10,
    "B": 20
}
dict2 = {
    "A": 50,
    "C": 30,
    "D": 40
}

dict1.update(dict2)
print(dict1)