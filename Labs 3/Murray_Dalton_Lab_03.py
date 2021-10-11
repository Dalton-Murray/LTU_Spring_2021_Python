#####################
## Dalton Murray    #
## 03/16/20201      #
## Lab 03           #
#####################

#Imports required library so we can exit try/except loop directly
#Checks in place to make sure if it can't be imported where used to have an alternative
import sys

#Sets global variable
inputFile = None
inFileContents = None
average = None
lineSplitTemp = None
classMaxHigh = 0
averageSum = 0
totalPersons = 0

#Defines the main function
def __main__():
    
    #Calls the openFile function
    openFile()
    
    #Calls the outputFile function
    outputFile()

#Defines the openFile functoin
def openFile():
    #Sets global variables
    global inputFile
    
    #Ensures that the file we're looking for is the correct file and can be opened in read-mode
    #The requirements for the assignment says to look for a file called "input.txt" however, the provided file is "inputs.txt"
    #as the provided file is different, I've made sure to look for both files.
    try:
        #Tries the first time to find the file "input.txt" and if we can open it as read-only
        inputFile = open("input.txt", "r")
    #If we can't find the file "input.txt" or open it as read-only we get FileNotFoundError and continue
    except FileNotFoundError:
        #Once we've gotten the FileNotFoundError we try again
        try:
            #We search for the next file, "inputs.txt" and if we can open it as read-only
            inputFile = open("inputs.txt", "r")
        #If we can't find either the "input.txt" or the "inputs.txt" files and we can't open either as read-only we then go to
        #the catching of this exception 
        except FileNotFoundError:
            #Required from the imported library sys, allows us to exit directly out and stop running
            try:
                print("Missing file, exiting directly")
                sys.exit(1)
            except NameError:
                print("Missing file, system library couldn't be imported.")

#Defines the outputFile function
#This will handle most of the processing      
def outputFile():
    #Sets global variables
    global average
    global averageSum
    global lineSplitTemp
    global totalPersons
    global classMaxHigh
    
    #Sets local variable
    classAverageHighLow = []
    classHighStep = 0
    classLowStep = 0
    
    #Prepares output file for write and creates file
    try:
        outputFile = open("output.txt", "w")
    except:
        #Tries to directly exit
        try:
            print("Error creating a writable output file, exiting directly")
            sys.exit(1)
        #If can't directly exit, print error
        except:
            print("Error creating a writable output file, system library couldn't be imported.")
            
    #Writes starter information for output file
    outputFile.write(100*"*")
    #Closes output file
    outputFile.close()
    #Opens output file as appending
    outputFile = open("output.txt", "a")
    
    #Starts the for loop, running across every line in the file "inputFile"
    try:
        for line in inputFile:
            #Ensures we get successful splits in grades and names, as it is a CSV inputted file
            lineSplitTemp = line.split(",")
            #Sets local individualTotal value
            individualTotal = 0
            #Steps through each value to get total
            for i in range(1, len(lineSplitTemp)):
                individualTotal = individualTotal + float(lineSplitTemp[i])
            #Calculates average
            average = individualTotal/(len(lineSplitTemp) - 1)
            #Ensures that we store the averages and adds them all together
            averageSum += average
            #Keeps total person count
            totalPersons += 1
            
            #Records student name and then their average score in a list to be used later for highest lowest
            classAverageHighLow += [lineSplitTemp[0], average]
            
            #Begins output to file
            #Has to be converted to string because Python doesn't like directly writing non-strings
            outputFile.write("\nStudent "+str(totalPersons)+": "+ lineSplitTemp[0])
            outputFile.write("\nAverage score: "+ str(average) +"\n")

        #Gets class highest average score with persons name
        #Improper way of doing it, but for a short list is less resource intensive than a dictionary, proven by a trace
        #This for loop goes through the classAverageHighLow list and gets every other in the list, making it skip
        #the persons names, and only get the numbers
        for maxHighLow in classAverageHighLow[1::2]:
            if classMaxHigh < maxHighLow:
                classMaxHigh = maxHighLow
                #This sets the max low to the max high so that we know that the max low is lower than or equal to the max
                #high, as well, when defining we can't set it to None as it is invalid and if we set it to 0
                #then it will likely not work properly as the scores will unlikely be below 0
                classMaxLow = classMaxHigh
        for maxHighLow in classAverageHighLow[1::2]:
            if classMaxLow > maxHighLow:
                classMaxLow = maxHighLow
       
        #########################################################
        ## Disclaimer:                                         ##
        ## We're not checking if they're equal to each other   ##
        ## If it happens that averages are equal to each other ##
        ## then the average highest and lowest tend to choose  ##
        ## the first person, as this is not a requirement      ##
        #########################################################
       
        #Creates line at the end of student list to move to overall information    
        outputFile.write(100*"-")
        outputFile.write("\nTotal number of students: "+str(totalPersons))
        #Calculates class average score
        classAverage = averageSum / totalPersons
        #Outputs class average
        outputFile.write("\nThe class average is: "+str(classAverage))
        #Outputs class high and low
        #High
        #Gets the classAverageHighlow list and indexes the classMaxHigh and subtracts one so we get the persons name
        studentHighestScoreValue = classAverageHighLow.index(classMaxHigh) - 1
        #Sets the studentHighestScore variable to the index of the students name
        studentHighestScore = classAverageHighLow[studentHighestScoreValue]
        outputFile.write("\nThe student with the highest average score is: "+studentHighestScore)
        #Low
        studentLowestScoreValue = classAverageHighLow.index(classMaxLow) - 1
        studentLowestScore = classAverageHighLow[studentLowestScoreValue]
        outputFile.write("\nThe student with the lowest average score is: "+studentLowestScore)
        outputFile.write("\n"+100*"*")
        print("Outputted successfully!")
        
    #Exception for TypeError because file issues may be present and no other logical error involved
    except TypeError:
        try:
            #Tries to direcly exit
            sys.exit(1)
            print("Cannot continue, file error")
         #If can't directly exit prints error
        except:
            print("Cannot continue, file error, system library couldn't be imported")
    #The inputted data file may not be correctly separated
    except ValueError:
        try:
            #Tries to directly exit
            sys.exit(1)
            print("Cannot continue, data is corrupt or in an incorrect format")
        #If can't direcly exit prints error
        except:
            print("Cannot continue, data is corrupt or in an incorrect format, system library couldn't be imported")
    #In case the input file as no data and only names, or tries to make us error out by dividing by 0
    except ZeroDivisionError:
        try:
            #Tries to directly exit
            sys.exit(1)
            print("Cannot continue, data is corrupt or in an incorrect format")
        #If can't direcly exit prints error
        except:
            print("Cannot continue, data is corrupt or in an incorrect format, system library couldn't be imported")
    
    #Ensures that we close the open inputFile and output file
    try:
        inputFile.close()
        outputFile.close()
    except:
        #Tries to directly exit
        try:
            print("Error closing the running file, exiting directly")
            sys.exit(1)
        #If can't directly exit prints error
        except:
            print("Error closing the running file, system library couldn't be imported")
        

#Calls the main function
__main__()

#I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own.
#Dalton Murray
