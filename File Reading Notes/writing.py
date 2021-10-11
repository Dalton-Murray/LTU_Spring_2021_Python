#####################
## Dalton Murray    #
## 03/15/20201      #
##                  #
#####################


# Appending and creating a new file
outFile = open("new_output.txt", "a")

outFile.write("This is a new test!!\n")

outFile.close()

# Deleting a file
import os
os.remove("new_output.txt")


outFile = open("new_output.txt", "a")

outFile.write("This is a new test!!\n")