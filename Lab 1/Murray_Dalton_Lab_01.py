#####################
## Dalton Murray    #
## 02/15/20201      #
## Lab 01           #
#####################

#Defines variables and sets them equal to none so I can pass variables globally (Bad method of doing it but it works if trying
# I am trying to keep the program simple and small for this class)
billAmount = None
tipPercentage = None
taxRate = None

#Tip percentage options
tipPercentageOption = None

#Defines variables for calculations
taxAmount = None
tipAmount = None
totalAmount = None

#Defines main function
def __main__():
    
    #Calls get information function
    __getInformation__()
    
    #Calls general calculations function
    __generalCalculations__()
    
    #Calls print informationf unction
    __printInformation__()
    
#Defines get information function to get information from user
def __getInformation__():
    #Linking global variables
    global billAmount
    global tipPercentage
    global taxRate
    global tipPercentageOption
    
    #Gets information and validates
    #Gets bill amount 
    billAmount = float(input("Please enter the total amount of the bill: \n(Format: xxx, example: 20)\n"))
    #Validates data for bill amount to be non-negative
    while billAmount < 0.01:
        print("You have enetered a invalid bill amount, please ensure you have entered a positive number")
        billAmount = float(input("Please enter the total amount of the bill: \n(Format: xxx, example: 20)\n"))
    
    #Gets tip percentage
    tipPercentageOption = input("Please choose an option for your tip percentage:\
        \n1 = No tip \
        \n2 = 0.10% \
        \n3 = 0.15% \
        \n4 = 0.20% \
        \nCustom = Enter your own amount\n")

    #Validates tip percentage option and sets custom amount
    if tipPercentageOption == "1":
        tipPercentage = 0
    elif tipPercentageOption == "2":
        tipPercentage = 0.10
    elif tipPercentageOption == "3":
        tipPercentage = 0.15
    elif tipPercentageOption == "4":
        tipPercentage = 0.20
    else:
        tipPercentage = float(input("Please enter your custom tip percentage:\nFormatting is: 0.xx Example: 0.20 for 20%\n"))
    
    #Gets tax rate
    taxRate = float(input("Please enter your tax rate: \n(Format: 0.xx)\n"))
    #Validates data for tax rate to be non-negative
    while taxRate < 0.01:
        print("You have enetered a invalid tax rate amount, please ensure you have entered a positive number")
        taxRate = float(input("Please enter your tax rate: \n(Format: 0.xx Example: 0.06 for 6% tax rate. Or whole number, example: 6 for 6%)\n"))
    #Ensures proper conversion if user entered whole number
    if taxRate > 1:
        taxRate = taxRate / 100
    print(taxRate)

#Defines general calculations function to perform calculations
def __generalCalculations__():
    #Linking global variables
    global taxAmount
    global tipAmount
    global totalAmount
    
    #Performs calculation to get tax amount
    #Total amount of taxes are equal to the bill amount times the tax rate
    taxAmount = billAmount * taxRate
    
    #Performs calculation to get tip amount
    #Tip amount is equal to the bill amount times the tip percentage
    tipAmount = billAmount * tipPercentage
    
    #Calculates total amount
    #The total amount is equal to the bill amount plus the tax amount and the tip amount
    totalAmount = billAmount + taxAmount + tipAmount

#Defines print information function to print out the information
def __printInformation__():
    #Formatting (not the best way to do it but simple and it works)
    format_billAmount = "${:,.2f}".format(billAmount)
    format_taxAmount = "${:,.2f}".format(taxAmount)
    format_tipAmount = "${:,.2f}".format(tipAmount)
    format_totalAmount = "${:,.2f}".format(totalAmount)
    
    print("\nDear Customer,\nYour bill amount is: ", format_billAmount, \
     "\nYour tax amount is:  ", format_taxAmount, \
     "\nYour tip amount is:  ", format_tipAmount, \
     "\n\n*********************************************************", \
     "\nYour total bill, including sales tax and tip is:", format_totalAmount, \
     "\n*********************************************************")

#Calls main function
__main__()

#I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own.
#Dalton Murray