#####################
## Dalton Murray    #
## 03/29/20201      #
## Lab 04           #
#####################

# Imports required library so we can exit try/except loop directly
# Checks in place to make sure if it can't be imported where used to have an alternative
import sys
# The random library is required for .shuffle
import random
# The RegEx library we use to combine splits into a single line
import re

# Sets variables
userDifficultyLevel = None
userScore = None
scrambledWords = {}
inputFile = None
fileLine = None
lineSplitTemp = []
correctCount = 0
wrongCount = 0
userScore = 0

# Defines the "__main__" function
def __main__():

    # Calls the "gameIntroduction" function
    gameIntroduction()
    # Calls the "difficultyLevel" function
    difficultyLevel()

    # Calls the "fileOpen" function
    fileOpen()

    # Calls the "additionalLine" function
    additionalLine()

    # Calls the "wordScramble" function
    wordScramble()

    # Calls the "guessingGame" function
    guessingGame()

    # Calls the "userStats" function
    userStats()

    # Calls the "fileClose" function
    fileClose()

# Defines the "gameIntroduction" function
def gameIntroduction():
    # Prints out basic instructions for the game and creates separators so that it is more easily read
    print(100*"*"+"\nHello and welcome to this word scramble guessing game!\
    \nFirstly you will need to choose a difficulty level:\
    \n  Easy: 30 points for a correct guess\
    \n  Normal: 40 points for a correct guess\
    \n  Difficult: 70 points for a correct guess\
    \n\nFor each difficulty level you only have 3 chances to guess the word correctly!\n"+100*"*")

# Defines the "difficultyLevel" function
def difficultyLevel():
    # Sets the "userDifficultyLevel" variable to be global instead of continuously passing it
    global userDifficultyLevel

    # Asks the user to choose their difficulty level
    userDifficultyLevel = input("Please enter your difficulty level: (Easy, Normal, Difficult) ")
    # Converts the difficulty level to all lowercase
    userDifficultyLevel = userDifficultyLevel.lower()
    # Ensures that the user has typed in a valid difficulty level
    # Doing this while loop prevents us from needing a harsher data validation such as a try/except and catches anything which
    # may not be a valid difficulty levelghj
    # We are able to set a local variable to false and use it to run a while loop, if the condition is meant in the if statement
    # in the while loop, we then change the local variable to true so the whiel loop exits
    userTrueDifficulty = False
    while userTrueDifficulty == False:
        # This is a cleanily way of doing the if statement so we don't have to do a lot of elif's
        if userDifficultyLevel == "easy" or userDifficultyLevel == "normal" or userDifficultyLevel == "difficult":
            userTrueDifficulty = True
        else:
            print("\nPlease choose a valid difficulty level")
            userDifficultyLevel = input("Please enter your difficulty level: (Easy, Normal, Difficult) ")
            # Ensures that if they didn't enter a valid difficulty level the first time to lowercase it on the next continuous
            # times they input something.
            userDifficultyLevel = userDifficultyLevel.lower()

# Defines the function "fileOpen" making sure the file opens properly
def fileOpen():
    # Sets global variables
    global inputFile

    # This ensures that we are able to properly open the words file
    try:
        # Tries the first time to find the file "words.txt" and if we can open it as read-only
        inputFile = open("words.txt", "r")
    # If we can't find the file "words.txt" or open it as read-only we get FileNotFoundError and continue
    except FileNotFoundError:
        try:
            # This prints to the terminal/output that the file is missing and then exits directly
            # Exiting directly with sys.exit(1) ends the program and raises a error rather than continuing on without
            # the file and catching every exception as well as exiting without a raised error
            print("Missing file, exiting directly")
            sys.exit(1)
        # This is if for some reason we can't import the system library and exit directly we print out an error
        # and the program continues without the file
        except NameError:
            print("Missing file, system library couldn't be imported.")

# Defines the "additionalLine" function
def additionalLine():
    # Gets the global inputFile
    global inputFile

    # Closes the inputFile so we are able to open it in appending
    inputFile.close()
    # Attempts to open the inputFile in appending
    try:
        inputFile = open("words.txt", "a")
    except FileNotFoundError:
        try:
            # This prints to the terminal/output that the file is missing and then exits directly
            # Exiting directly with sys.exit(1) ends the program and raises a error rather than continuing on without
            # the file and catching every exception as well as exiting without a raised error
            print("Missing file, exiting directly")
            sys.exit(1)
        # This is if for some reason we can't import the system library and exit directly we print out an error
        # and the program continues without the file
        except NameError:
            print("Missing file, system library couldn't be imported.")

    # Writes a single space at the end of the inputFile so we don't have the issue with using the
    # difficult difficulty level
    # The only issue we should consider here is deleting the additional spaces later on, however, this is a quick patch
    inputFile.write(" ")

    # This ensures that we are able to properly close the words file
    try:
        # Tries to close the file properly
        inputFile.close()
    # If we can't close the file
    except:
        try:
            # This prints to the terminal/output that we can't properly close the file
            # Exiting directly with sys.exit(1) ends the program and raises a error rather than continuing on without
            # the file and catching every exception as well as exiting without a raised error
            print("File close error, exiting directly")
            sys.exit(1)
        # This is if for some reason we can't import the system library and exit directly we print out an error
        # and the program continues without the file
        except NameError:
            print("File close error, system library couldn't be imported.")

    # This ensures that we are able to properly open the words file
    try:
        # Tries the first time to find the file "words.txt" and if we can open it as read-only
        inputFile = open("words.txt", "r")
    # If we can't find the file "words.txt" or open it as read-only we get FileNotFoundError and continue
    except FileNotFoundError:
        try:
            # This prints to the terminal/output that the file is missing and then exits directly
            # Exiting directly with sys.exit(1) ends the program and raises a error rather than continuing on without
            # the file and catching every exception as well as exiting without a raised error
            print("Missing file, exiting directly")
            sys.exit(1)
        # This is if for some reason we can't import the system library and exit directly we print out an error
        # and the program continues without the file
        except NameError:
            print("Missing file, system library couldn't be imported.")


# Defines the main function we will use to scramble the words, save scores, read lines
def wordScramble():
    # Sets global variables
    global userScore
    global scrambledWords
    global fileLine
    global lineSplitTemp

    # The requirements of the work doesn't say if we need to check if the difficulty level word
    # is in the list of words,  however, if it is it will create an issue with the line detection and the
    # variable will be set to the wrong line
    # This entire thing is not even in the requirements and we could just assume that each category is its own line,
    # however, it's not really stated, and I like to do this anyways to be sure
    # The rest of the program also assumes that the input follows a difficulty: word, word1, word2 format
    for activeFileLine, line in enumerate(inputFile, 1):
        # This ensures that we're on the line of the users difficulty level
        if userDifficultyLevel in line:
            # Strips the line so we don't have to deal with \n later
            line = line.strip()
            for word in inputFile:
                # Splits each word so it can be added to the list later on to converted to the dictionary
                lineSplitTemp = re.split("[:, ]", line)

    # This removes the first item in the list as it will always be the difficulty level
    lineSplitTemp.pop(0)
    # This removes the empty values in the list so we are only working with the true words
    while("" in lineSplitTemp):
        lineSplitTemp.remove("")

    # Sets the scrambledWords dictionary keys to the elements in the lineSplitTemp list
    scrambledWords = dict.fromkeys(lineSplitTemp)

    # This iterates through each of the items in the scrambledwords
    for key, value in scrambledWords.items():
        # If the value in the dictionary is equal to none
        if value is None:
            # We then set chrs to a list, the list being the key, as random.shuffle doesn't work on strings and works on lists
            chrs = list(key)
            # We then shuffle the list of characters
            random.shuffle(chrs)
            # We recombine the characters into words and not lists
            scrambled = ''.join(chrs)
            # If the scrambled word is equal to the key we re-scramble until it's not equal
            while scrambled == key:
                chrs = list(key)
                random.shuffle(chrs)
                scrambled = ''.join(chrs)
            # This sets the key of the dictionary to the key and the value to the scrambled word
            scrambledWords.update({key:scrambled})

# Defines the "guessingGame" function used for the actual game itself
def guessingGame():
    # Sets global variables
    global correctCount
    global wrongCount
    global userScore
    # Sets local variables
    guessCount = 0
    passedLevel = None

    # Scrambles the dictionary and converts into a list for later use
    for key,value in random.sample(list(scrambledWords.items()), len(scrambledWords)):
        # Sets the guess count back to 0 so on the next word they have 3 guesses
        guessCount = 0
        # Sets the "passedLevel" function to False so we may continue properly when it gets set to true later
        passedLevel = False

        # Detects user difficulty
        if userDifficultyLevel == "easy":
            # If the passed level is not true it will not run and thus go to the next word
            while passedLevel != True:
                # Keeps a running score of the guess count
                guessCount += 1
                # Outputs the scrambled word and allows them to answer
                userAnswer = input("\nYour scrambled word is "+value+": ")
                # Ensures the users answer is in lowercase
                userAnswer = userAnswer.lower()
                # If the users answer is equal to the unscrambled word
                if userAnswer == key:
                    # Adds to the correct count and keeps a running total
                    correctCount += 1
                    # Adds to the user score and keeps a running total
                    userScore += 30
                    # Tells them congratulations and their current total score
                    print("\nCongratulations! You have guessed the correct word! Your current score is:",userScore,\
                        "\nYou earned 30 points")
                    # Sets "passedLevel" to true so they move to the next word
                    passedLevel = True
                # If the users guess count is below 3 it tells them not correct and their current amount of guesses remaining
                elif guessCount < 3:
                    print("Sorry, your answer is not correct, you still have",3-guessCount,"tries remaining")
                # If the users guess count is equal to 3
                if guessCount == 3:
                    # Print they have run out of guesses
                    print("Sorry, you've run out of guesses! Please try again later")
                    # Moves to the next word
                    passedLevel = True
                    # Adds to the wrong count running total
                    wrongCount += 1

        # Detects user difficulty
        if userDifficultyLevel == "normal":
            # If the passed level is not true it will not run and thus go to the next word
            while passedLevel != True:
                # Keeps a running score of the guess count
                guessCount += 1
                # Outputs the scrambled word and allows them to answer
                userAnswer = input("\nYour scrambled word is "+value+": ")
                # Ensures the users answer is in lowercase
                userAnswer = userAnswer.lower()
                # If the users answer is equal to the unscrambled word
                if userAnswer == key:
                    # Adds to the correct count and keeps a running total
                    correctCount += 1
                    # Adds to the user score and keeps a running total
                    userScore += 40
                    # Tells them congratulations and their current total score
                    print("\nCongratulations! You have guessed the correct word! Your current score is:",userScore,\
                        "\nYou earned 40 points")
                    # Sets "passedLevel" to true so they move to the next word
                    passedLevel = True
                # If the users guess count is below 3 it tells them not correct and their current amount of guesses remaining
                elif guessCount < 3:
                    print("Sorry, your answer is not correct, you still have",3-guessCount,"tries remaining")
                # If the users guess count is equal to 3
                if guessCount == 3:
                    # Print they have run out of guesses
                    print("Sorry, you've run out of guesses! Please try again later")
                    # Moves to the next word
                    passedLevel = True
                    # Adds to the wrong count running total
                    wrongCount += 1

        # Detects user difficulty
        if userDifficultyLevel == "difficult":
            # If the passed level is not true it will not run and thus go to the next word
            while passedLevel != True:
                # Keeps a running score of the guess count
                guessCount += 1
                # Outputs the scrambled word and allows them to answer
                userAnswer = input("\nYour scrambled word is "+value+": ")
                # Ensures the users answer is in lowercase
                userAnswer = userAnswer.lower()
                # If the users answer is equal to the unscrambled word
                if userAnswer == key:
                    # Adds to the correct count and keeps a running total
                    correctCount += 1
                    # Adds to the user score and keeps a running total
                    userScore += 70
                    # Tells them congratulations and their current total score
                    print("\nCongratulations! You have guessed the correct word! Your current score is:",userScore,\
                        "\nYou earned 70 points")
                    # Sets "passedLevel" to true so they move to the next word
                    passedLevel = True
                # If the users guess count is below 3 it tells them not correct and their current amount of guesses remaining
                elif guessCount < 3:
                    print("Sorry, your answer is not correct, you still have",3-guessCount,"tries remaining")
                # If the users guess count is equal to 3
                if guessCount == 3:
                    # Print they have run out of guesses
                    print("Sorry, you've run out of guesses! Please try again later")
                    # Moves to the next word
                    passedLevel = True
                    # Adds to the wrong count running total
                    wrongCount += 1

# Defines the "userStats" function
def userStats():
    # Prints out a list of the users stats with their amount of words correct, wrong and their total score
    print("\nYou guessed",str(correctCount),"words correctly"\
        "\nYou guessed",str(wrongCount)+" words incorrectly"\
        "\nYour total score is "+str(userScore))

# Defines the "fileClose" function
def fileClose():
    global inputFile

    # This ensures that we are able to properly close the words file
    try:
        # Tries to close the file properly
        inputFile.close()
    # If we can't close the file
    except:
        try:
            # This prints to the terminal/output that we can't properly close the file
            # Exiting directly with sys.exit(1) ends the program and raises a error rather than continuing on without
            # the file and catching every exception as well as exiting without a raised error
            print("File close error, exiting directly")
            sys.exit(1)
        # This is if for some reason we can't import the system library and exit directly we print out an error
        # and the program continues without the file
        except NameError:
            print("File close error, system library couldn't be imported.")

# Calls the main function
__main__()

# I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own.
# Dalton Murray