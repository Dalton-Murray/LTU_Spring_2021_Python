#####################
## Dalton Murray    #
## 02/24/20201      #
## Lab 02           #
#####################

#Imports required library
import random

#Defines variables
difficultyLevel = None

#Creates the main function
def __main__():
    
    #Calls the greeting function
    greeting()
    
    #Calls the tutortial and difficulty function
    tutorial_Difficulty()
    
    #Calls the game start function
    gameStart()

#Creates the greeting function
def greeting():
    #Assigns the variable 'greeting' to the users input of their name
    greeting = input("What is your name?: ")
    #Prints out 'Welcome' followed by the users input
    print("\nWelcome",greeting)

#Creates the tutorial difficulty function
def tutorial_Difficulty():
    #Sets the difficulty level to a global variable (instead of having to individually pass it around)
    global difficultyLevel
    
    print("\nThis is a number guessing game!\nA random number will be generated which you have to guess\nEach time you guess it'll tell you if you're too high, too low, or if you got it right!\
        \n\nYou will start by choosing a level of difficulty\
        \n\nThe levels of difficulty are:\
        \nLevel One (Easy): This will generate a random number 1-10 and you will only have 5 chances to guess the number\
        \nLevel Two (Normal) This will generate a random number 1-20 and you will only have 4 chances to guess the number\
        \nLevel Three (Hard) This will generate a random number 1-30 and you will only have 3 chances to guess the number")
    
    #Gets the difficulty level from the user and converts it to a integer
    difficultyLevel = int(input("\nWhat level of difficulty would you like? (1, 2, 3) "))
    
    #Ensures that the user only picks a number above 0 and below 4
    while difficultyLevel > 3 or difficultyLevel < 1:
        print("Please pick a valid difficulty level")
        difficultyLevel = int(input("What level of difficulty would you like? (1, 2, 3) "))
        
#Creates the game start function
def gameStart():
    #Defines the guess count variable for what we will use to count the chances
    guessCount = 0
    
    #Checks the difficulty level and runs the game accordingly
    if difficultyLevel == 1:
        print("\nYou have chosen Level One (Easy)\nThe game will now begin!")
        #Generates a random number between 1 and 10, including both 1 and 10
        secretNumber = random.randint(1,10)
        #Starts a loop while the guess count is below 5
        while guessCount < 5:
            #Adds 1 to the guess count everytime it gets ran
            guessCount += 1
            #Gets the users guess and converts it into an integer
            userGuess = int(input("What is your guess? "))
            #Checks if the users guess is equal to the secret number, if it is they've won!
            if userGuess == secretNumber:
                print("Congratulations! You have guessed correctly!")
                #Makes sure to exit the while loop as they've already won
                break
            #If the users number is less than the secret number then it's too low
            elif userGuess < secretNumber:
                print("Your guess is too low!")
            else:
                #If it's not equal to the secret number and it's not less than the secret number than it has to be greater than the equal number, so it's too high
                print("Your guess is too high!")
            #If the guess count is equal to 5 then they've run out of guesses!
            if guessCount == 5:
                print("Sorry, you've run out of guesses!")
    #Checks to make sure that the difficulty level is equal to 2
    elif difficultyLevel == 2:
        print("\nYou have chosen Level Two (Normal)\nThe game will now begin!")
        #Generates a random number between 1 and 20, including both 1 and 20
        secretNumber = random.randint(1,20)
        #Starts a loop while the guess count is below 5
        while guessCount < 4:
            #Adds 1 to the guess count everytime it gets ran
            guessCount += 1
            #Gets the users guess and converts it into an integer
            userGuess = int(input("What is your guess? "))
            #Checks if the users guess is equal to the secret number, if it is they've won!
            if userGuess == secretNumber:
                print("Congratulations! You have guessed correctly!")
                #Makes sure to exit the while loop as they've already won
                break
            #If the users number is less than the secret number then it's too low
            elif userGuess < secretNumber:
                print("Your guess is too low!")
            else:
                #If it's not equal to the secret number and it's not less than the secret number than it has to be greater than the equal number, so it's too high
                print("Your guess is too high!")
            #If the guess count is equal to 4 then they've run out of guesses!
            if guessCount == 4:
                print("Sorry, you've run out of guesses!")
    #Checks to make sure that the difficulty level is equal to 3 
    elif difficultyLevel == 3:
        print("\nYou have chosen Level Three (Hard)\nThe game will now begin!")
        #Generates a random number between 1 and 30, including both 1 and 30
        secretNumber = random.randint(1,30)
        #Starts a loop while the guess count is below 5
        while guessCount < 3:
            #Adds 1 to the guess count everytime it gets ran
            guessCount += 1
            #Gets the users guess and converts it into an integer
            userGuess = int(input("What is your guess? "))
            #Checks if the users guess is equal to the secret number, if it is they've won!
            if userGuess == secretNumber:
                print("Congratulations! You have guessed correctly!")
                #Makes sure to exit the while loop as they've already won
                break
            #If the users number is less than the secret number then it's too low
            elif userGuess < secretNumber:
                print("Your guess is too low!")
            else:
                #If it's not equal to the secret number and it's not less than the secret number than it has to be greater than the equal number, so it's too high
                print("Your guess is too high!")
            #If the guess count is equal to 4 then they've run out of guesses!
            if guessCount == 3:
                print("Sorry, you've run out of guesses!")
   #Just in-case somehow a number got through the previous validations, highly unlikely
    else:
        print("Invalid difficulty level")

#Calls the main function
__main__()