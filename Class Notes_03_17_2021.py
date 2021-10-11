#####################
## Dalton Murray    #
## 03/17/20201      #
## Class notes      #
#####################

#line = "This is just an example!"
line = "Seyed Mojab, 45, 88, 25, 100"

print(line.split(", "))

myString = "Hello World!"
myList = list(myString)

print(myList[0:])

myList.reverse()
print(myList)

fruits = ['banana', 'orange', 'apple']
numbers = [30, 10, 25, 55]
objects = [10, 'banana', [12, 45]]
#print(len(objects))
print(objects[-1][-1])

fruits1 = ["banana", "orange", "apple"]
fruits2 = ["lychee"]

#fruits1.pop(0)
#fruits1.remove('apple')
del fruits1[1:3]

fruits = fruits1+fruits2
print(fruits)