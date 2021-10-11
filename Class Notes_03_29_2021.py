#####################
## Dalton Murray    #
## 03/29/20201      #
## Class notes      #
#####################

mySet = set(["apple", "orange", 10])
mySet.add("cucumber")
mySet.update([1, 2, "door"])

# mySet.remove("apple")
mySet.discard("fighter")

print(mySet)
print(len(mySet))

for item in mySet:
    print(item)

mySet.clear()
print(mySet)

set1 = set(["apple", "orange", 10])
set2 = {"orange", 10}

# new_set = set1.union(set2)
# new_set = set1 | set2
# new_set = set1.difference(set2)
# new_set = set1 - set2


# print(set2.issubset(set1))
# print(set1.issubset(set2))
# print(set1.symmetric_difference(set2))
# print(set1 >= set2)

myList = [1, 2, 3, 4, 5]
# squares_set = {item**2 for item in myList if item%2!=0}
squares_set = {item**2 for item in myList if item%2==0}
print(squares_set)

import pickle