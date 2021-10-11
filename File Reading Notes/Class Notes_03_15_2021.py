#####################
## Dalton Murray    #
## 03/15/20201      #
##                  #
#####################

# Reading data from = Process of retrieving data from a file
# Input file = a file from which data is read
# 3 steps when a program uses a file
# Open the file
# file_variable = open("dogs.txt")
# Process the file
# file.readlines()
# Close the file
# file.close()

# Open function
# file_variable = open(filename, mode)
# Mode
# Reading only ('r')
# Writing only ('w')
# Appending ('a') - write at bottom of file

# Writing
# file_variable.write(string)
# Closing
# file_variable.close()

# Text file = data encoded as text
# Binary file = Data no converted to text

# 2 ways to access data stored in file
# Sequential = file read sequentially from beginning to end, can't skip ahead
# Direct = Can jump directly to any piece of data in the file

#Relative path
inFile = open('input.txt', 'r')
# Reads entire file
inFileContents = inFile.read()
# Will only read first 5 characters can do any number
# inFileContents = inFile.read(5) 
# Can read line-by-line, can do multiple lines
# inFileContents = inFile.readline()
# inFileContents = inFile.readline()
# inFileContents = inFile.readline()
# Can read entire line and return in list
# inFileContents = inFile.readlines()
print(inFileContents)

for line in inFile:
    print(line)

inFile.close()

# This is a way to do it in a try with making sure to close
try:
    inFile = open("input.txt", "r")
    inFileContents = inFile.read()
    print(inFileContents)
except: # except exceptionName:
    print("Uh oh")
finally:
    inFile.close()