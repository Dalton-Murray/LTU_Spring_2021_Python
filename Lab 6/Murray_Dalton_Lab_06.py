#####################
## Dalton Murray    #
## 04/27/20201      #
## Lab 06           #
#####################

############################################################################################################
# ! This program has approximately 96% of the work complete, however, due to time restraints of me working,#
# ! and finals before and after this assignment I won't be able to fully complete it, not due to a lack of #
# ! this is not due to time management or a lack of planning.                                              #
# ! However, a majority of the code to make it fully functioning is in place, just not completely set up,  #
# ! the only thing really missing is changing difficulties lively and inputting text                       #
############################################################################################################


# Imports required library so we can exit try/except loop directly
# Checks in place to make sure if it can't be imported where used to have an alternative
import sys
# The random library is required for .shuffle
import random
# The RegEx library we use to combine splits into a single line
import re
# Imports the tkinter library for creating the gui
# This also sets it to just tk so we don't have to tyype tkinter everytime
import tkinter as tk
    # Imports messagebox from the tkinter library
import tkinter.messagebox

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
guessCount = 0

# Begins adaptation to gui
class Gui():
    def __init__(self):
        # Sets gui to tkinter.TK
        self.gui = tkinter.Tk()
        # Sets the title of the application
        self.gui.title("Word Scramble")
        # Sets the dimensions of the window to 500 x 500
        self.gui.geometry("500x250")
        self.userGuess = tk.StringVar()

        # Defines the "introduction" function which shows a messagebox which shows the introduction with proper formatting
        def introduction():
            tk.messagebox.showinfo("Word Scramble Instructions",\
                                        63*"*"+\
                                        "\n\nHello and welcome to this word scramble guessing game!"+\
                                        "\n\nFirstly you will need to choose a difficulty level:"+\
                                        "\n  Easy: 30 points for a correct guess"+\
                                        "\n  Normal: 40 points for a correct guess"+\
                                        "\n  Difficult: 70 points for a correct guess"+\
                                        "\n\nFor each difficulty level you only have 3 chances to guess the word correctly!\n\n"\
                                        +63*"*")

        # Defines the "difficultyLevel" function
        def easyDifficultyLevel():
            # Sets the "userDifficultyLevel" variable to be global instead of continuously passing it
            global userDifficultyLevel
            userDifficultyLevel = "easy"
            guessesLeft = 3
            guessesRemaining["text"] = "Guesses left: " + str(guessCount)

            wordScramble()

        def normalDifficultyLevel():
            # Sets the "userDifficultyLevel" variable to be global instead of continuously passing it
            global userDifficultyLevel
            userDifficultyLevel = "normal"
            guessesLeft = 3
            guessesRemaining["text"] = "Guesses left: " + str(guessCount)

            wordScramble()

        def difficultDifficultyLevel():
            # Sets the "userDifficultyLevel" variable to be global instead of continuously passing it
            global userDifficultyLevel
            userDifficultyLevel = "difficult"
            guessesLeft = 3
            guessesRemaining["text"] = "Guesses left: " + str(guessCount)

            wordScramble()

        # Defines the "additionalLine" function
        def additionalLine():
            # Gets the global inputFile
            global inputFile

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
        # Calls the "additionalLine" function
        additionalLine()

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

            # Try/Except
            try:
                # If the user's difficulty level word is in the list is removes it
                lineSplitTemp.remove(userDifficultyLevel)
                # If the user's difficulty level word is not in the list is causes a ValueError which we then pass on so we
                # Know it isn't there or was already removed
            except ValueError:
                pass
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
            difficultyLength = len(scrambledWords)

            # Calls the "guessingGame" function to continue
            guessingGame()


        # Defines the "guessingGame" function used for the actual game itself
        def guessingGame():
            # Sets global variables
            global correctCount
            global wrongCount
            global userScore
            global guessCount
            # Sets local variables
            passedLevel = None
            userAnswer = self.userGuess.get()

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
                        scrambledWord["text"] = value
                        # Ensures the users answer is in lowercase
                        userAnswer = userAnswer.lower()
                        # If the users answer is equal to the unscrambled word
                        if userAnswer == key:
                            # Adds to the correct count and keeps a running total
                            correctCount += 1
                            # Adds to the user score and keeps a running total
                            userScore += 30
                            score["text"] = "Score: " + userScore
                            # Tells them congratulations and their current total score
                            userEntry["text"] = "Congratulations! Correct!"
                            # Sets "passedLevel" to true so they move to the next word
                            passedLevel = True
                        # If the users guess count is below 3 it tells them not correct and their current amount of guesses remaining
                        elif guessCount < 3:
                            userEntry["text"] = "Sorry, incorrect"
                        # If the users guess count is equal to 3
                        if guessCount == 3:
                            # Print they have run out of guesses
                            userEntry["text"] = "Sorry, no more guesses"
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
                        scrambledWord["text"] = value
                        # Ensures the users answer is in lowercase
                        userAnswer = userAnswer.lower()
                        # If the users answer is equal to the unscrambled word
                        if userAnswer == key:
                            # Adds to the correct count and keeps a running total
                            correctCount += 1
                            # Adds to the user score and keeps a running total
                            userScore += 30
                            score["text"] = "Score: " + userScore
                            # Tells them congratulations and their current total score
                            userEntry["text"] = "Congratulations! Correct!"
                            # Sets "passedLevel" to true so they move to the next word
                            passedLevel = True
                        # If the users guess count is below 3 it tells them not correct and their current amount of guesses remaining
                        elif guessCount < 3 and guessCount != 3:
                            userEntry["text"] = "Sorry, incorrect"
                        # If the users guess count is equal to 3
                        if guessCount == 3:
                            # Print they have run out of guesses
                            userEntry["text"] = "Sorry, no more guesses"
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
                        scrambledWord["text"] = value
                        # Ensures the users answer is in lowercase
                        userAnswer = userAnswer.lower()
                        # If the users answer is equal to the unscrambled word
                        if userAnswer == key:
                            # Adds to the correct count and keeps a running total
                            correctCount += 1
                            # Adds to the user score and keeps a running total
                            userScore += 30
                            score["text"] = "Score: " + userScore
                            # Tells them congratulations and their current total score
                            userEntry["text"] = "Congratulations! Correct!"
                            # Sets "passedLevel" to true so they move to the next word
                            passedLevel = True
                        # If the users guess count is below 3 it tells them not correct and their current amount of guesses remaining
                        elif guessCount < 3 and guessCount != 3:
                            userEntry["text"] = "Sorry, incorrect"
                        # If the users guess count is equal to 3
                        if guessCount == 3:
                            # Print they have run out of guesses
                            userEntry["text"] = "Sorry, no more guesses"
                            # Moves to the next word
                            passedLevel = True
                            # Adds to the wrong count running total
                            wrongCount += 1

        # Title label
        titleLabel = tk.Label(self.gui, text="Welcome to this word scramble guessing game!", font="Arial 11 bold")
        titleLabel.place(x=100, y=10, width=334, height=37)

        # Guesses left label
        guessesRemaining = tk.Label(self.gui, text="Guesses left: 0", font="Arial 11")
        guessesRemaining.place(x=30, y=50, width=100, height=25)

        # Score label
        score = tk.Label(self.gui, text="Score: 0", font="Arial 11")
        score.place(x=175, y=50, width=55, height=25)

        # Scrambled word - static
        scrambledWordStatic = tk.Label(self.gui, text="Your scrambled word is:", font="Arial 11")
        scrambledWordStatic.place(x=32, y=85, width=155, height=25)

        # Scrambled word - changing
        scrambledWord = tk.Label(self.gui, text="", font="Arial 11", fg="green")
        scrambledWord.place(x=210, y=85, width=80, height=25)

        # Enter guess label
        enterGuess = tk.Label(self.gui, text="Enter your guess:", font="Arial 11")
        enterGuess.place(x=10, y=115, width=155, height=25)

        # Guess entry
        userEntry = tk.Entry(self.gui, font="Arial 11", textvariable=self.userGuess)
        userEntry.place(x=30, y=140, width=155, height=25)

        # Submit button for entry
        userEntrySubmit = tk.Button(self.gui, text="Guess!", font="Arial 11")
        userEntrySubmit.place(x=200, y=140, width=80, height=25)

        # Easy difficulty
        easyDifficulty = tk.Button(self.gui, text="Easy", font="Arial 11", fg="green", command=easyDifficultyLevel)
        easyDifficulty.place(x=30, y=175, width=70, height=25)

        # Normal difficulty
        normalDifficulty = tk.Button(self.gui, text="Normal", font="Arial 11", fg="blue", command=normalDifficultyLevel)
        normalDifficulty.place(x=120, y=175, width=70, height=25)

        # Difficult difficulty
        difficultDifficulty = tk.Button(self.gui, text="Difficult", font="Arial 11", fg="red", command=difficultDifficultyLevel)
        difficultDifficulty.place(x=210, y=175, width=70, height=25)

        # Ensires that the window stays open
        tk.mainloop()









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

# Ensures the gui runs
if __name__ == "__main__":
    myGui = Gui()

fileClose()

# I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own.
# Dalton Murray