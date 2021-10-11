#####################
## Dalton Murray    #
## 03/22/20201      #
## Class notes      #
#####################

myString = "Hello World!"

print(len(myString))

for c in myString:
    if c in "aeiou":
        print(c)

# Strings are immutable, can't assign      
# myString[0] = "X"

print(myString[0])
print(myString[-1])
print(myString[:3])

string1 = "Hello"
string2 = "World!"
string3 = "2384723"

# Combines strings
# string1 = string1+" "+string2
# print(string1)

print(string1.islower())
print(string1.isupper())
print(string1.isdigit())
print(string3.isalnum())
print(string3.isalpha())

answer = input("Please enter your answer: ")
user_answer = answer.lower()
if user_answer == "yes":
    print("Yes")
elif user_answer == "no":
    print("No")
    
string4 = " 24 3248  dfgfgbfhg \n"
string5 = string4.strip()
print(string5)
string5 = string4.lstrip()
print(string5)
string5 = string4.rstrip()
print(string5)

string6 = "Hello big World"
print(string6.endswith("orld"))
print(string6.startswith("Hel"))

string7 = "John J. Johnson#55, 100, 89"
print(string7[:string7.find("#")])

string7 = string7.replace("John", "David", 1)
print(string7)

print(string1*10)

string7 = "John Smith, 55, 100, 89"
print(string7.split(", "))

string8 = "1;2;3;4;5;6"
print(string8.split(";"))
