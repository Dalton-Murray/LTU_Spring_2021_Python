#####################
## Dalton Murray    #
## 03/01/20201      #
##                  #
#####################

# All programs are normally stored in ROM and are loaded into RAM as needed for processing
# False | Normally stored in storage and loaded into RAM as needed for processing

# The CPU understands instructions written in a binary machine language.
# True | It must eventually go into binary 

# A bit that is turned off is represented by the value -1
# False | 0 is off 1 is on

# The Python language uses a compiler which is a program that both translates and executes the insutructions
# in a high-level language
# False | Python uses a interpreter

# Where does a computer store a program and the data that the program is working with while
# the program is running?
# A. In the main memory | Correct
# B. In the CPU
# C. In the secondary storage
# D. In the microprocessor

# What is the largest value that can be stored in one byte?
# A. 255 | Correct, 2^8
# B. 128
# C. 8
# D. 65535

# What type of error prevents the program from running?
# A. Syntax | Correct
# B. Human
# C. Grammatical 
# D. Logical

#----------------------------------------------------------------------------------------------#
# Chapter 2

# Comments in Python begin with the # character.
# True

# When using the camelCase naming convention, the first word of the variable name is written in
# lowercase and the first characters of all subsequent words are written in uppercase.
# True

# Python allows programmers to break a statement into multiple lines.
# True | It's \

# In Python, print statements written on separate lines do not necessarily output on separate lines.
# True

# The ____ function reads a piece of data that has been entered at the keyboard and returns that piece
# of data, as a string, back to the program.
# Input

# What is the output of the following statement?
# print('The path is D:\\sample\\test.')
# A. 'The path is D:\\sample\\test.'
# B. The path is D:\\sample\\test.
# C. The path is D\\sample\\test.
# D. The path is D:\sample\test. | Correct
# Adding two \\'s next to each other removes one because of formatting

# What is the output of the following statement?
# print('One'
#       'Two'
#       'Three')
# A. One Two Three
# B. One
# Two
# Three
# C. OneTwoThree | Correct, nothing is adding spaces or new lines
# D. Nothing - This statement contains an error.

# ___ are notes of explanation that document lines or sections of a program.
# Comments

# When applying the .3f formatting specifer to the number 76.15854, the result is ___
# 76.158
# print("{:.3f}".format(75.15844))

# When the + operator is used with two strings, it performs string _____.
# Concatenation

#----------------------------------------------------------------------------------------------#
# Chapter 3

# The if statement causes one or more statements to execute only when a Boolean expression is true.
# True

# Python allows you to compare strings, but it is not case sensitive.
# False

# Python uses the same symbols for the assignment operator as for the equality operator.
# False | X == 2 equality, X = 2 Assignment

# When using the ___ logical operator, one or both of the subexpressions must be true
# for the compound expression to be true.
# A. Or | Correct
# B. And
# C. Not
# D. Maybe


#----------------------------------------------------------------------------------------------#
# Chapter 4

#What will be displayed after this?
# total = 0
# for count in range (4, 6):
#     total += count
#     print(total)
# A. 4 9 | Correct
# B. 4 5 6
# C. 4 5
# D. 9
# It iterates twice, total would then += 4, then the second time it's += 5 making it 9
# After that, it's then out of the range of 6

# The following for loop iterates ____ times to draw a square.
# for x in range(4):
#     turtle.forward(200)
#     turtle.right(90)
# The range(4) equals [0, 1, 2, 3], so it'll iterate 4 times

#----------------------------------------------------------------------------------------------#
# Chapter 5

# Python function names follow the same rules as those for naming variables.
# True

# Different functions can have local variables with the same names.
# True

# Python allows you to pass multiple arguments to a function.
# True

# Unlike other languages, in Python the number of values a function can return is
# limited to one.
# False

# The first line in a function definition is
# Header

# Pass is ignored

# A __ variable is created inside a function
# Local

# Python comes with __ functions that have been prewritten for the programmer
# Standard

# Which of the following will assign a random integer in the range of 1 through 50 to the variable number
# number = random.randint(1, 50)

# The function header begins with the keyword _ and is followe dby the name of the function
# def

