#####################
## Dalton Murray    #
## 04/18/20201      #
## Lab 05           #
#####################

############################################################################################################
# ! This program has a majority of the work complete, however, due to time restraints of me working        #
# ! On my final project for a few of my courses, I don't have the time to make it fully functioning        #
# ! However, a majority of the code to make it fully functioning is in place, just not completely set up   #
############################################################################################################

# Defines the class "class"
class Class():

    # Defines the initializer which tells it what to set variables to as well as what it's looking for when it's ran
    # The way this is set up it also allows an inputted instructor name for the class, however, it isn't required
    def __init__(self, term, section, subject, courseNumber, crn, title, creditHours, instructorName=None, students=None):
        self.term = term
        self.section = section
        self.subject = subject
        self.courseNumber = courseNumber
        self.crn = crn
        self.title = title
        self.creditHours = creditHours
        self.instructorName = instructorName
        self.students = students

    # Defines the "setTerm" function and sets a variable "term" to the first input of the "Class" class
    def setTerm(self, newTerm):
        self.term = newTerm
    # Defines the "getTerm" function and sets it to return the current "term" variable
    def getTerm(self):
        return self.term

    # Defines the "setSection" function and sets a variable "section" to the second input of the "Class" class
    def setSection(self, newSection):
        self.section = newSection
    # Defines the "getSection" function and sets it to return the current "section" variable
    def getSection(self):
        return self.section

    # Defines the "setSubject" function and sets a variable "subject" to the third input of the "Class" class
    def setSubject(self, newSubject):
        self.subject = newSubject
    # Defines the "getSubject" function and sets it to return the current "subject" variable
    def getSubject(self):
        return self.subject

    # Defines the "setCourseNumber" function and sets a variable "courseNumber" to the fourth input of the "Class" class
    def setCourseNumber(self, newCourseNumber):
        self.courseNumber = newCourseNumber
    # Defines the "getCourseNumber" function and sets it to return the current "courseNumber" variable
    def getCourseNumber(self):
        return self.courseNumber

    # Defines the "setCRN" function and sets a variable "crn" to the fifth input of the "Class" class
    def setCRN(self, newCRN):
        self.crn = newCRN
    # Defines the "getCRN" function and sets it to return the current "crn" variable
    def getCRN(self):
        return self.crn

    # Defines the "setTitle" function and sets a variable "title" to the sixth input of the "Class" class
    def setTitle(self, newTitle):
        self.title = newTitle
    # Defines the "getTitle" function and sets it to return the current "title" variable
    def getTitle(self):
        return self.title

    # Defines the "setCreditHours" function and sets a variable "creditHours" to the seventh input of the "Class" class
    def setCreditHours(self, newCreditHours):
        self.creditHours = newCreditHours
    # Defines the "getCreditHours" function and sets it to return the current "creditHour" variable
    def getCreditHours(self):
        return self.creditHours

# ! Need to do students and grades
# ! Incomplete/Not Working
    # Defines the "addStudent" function and sets a variable equal to the students
    # ! Not currently fully functional
    def addStudent(self, Students):
        self.students = Students
    # Defines the "addStudent" function and sets a variable equal to the student
    # ! Not currently fully functional
    def addStudents(self, Students):
        self.students = Students
    # Defines the "getStudents" function and returns the information on the students
    # ! Untested
    def getStudents(self):
        return self.students

    # Defines the "getStudentsList" function and currently passes
    # ! Not functional
    def getStudentsList(self):
        pass
    # Defines the "getStudentsNum" function and currently passes
    # ! Not functional
    def getStudentsNum(self):
        pass

    # Defines the "setGrades" function and currently passes
    # ! Not functional
    def setGrades(self):
        pass
    # Defines the "getGrades" function and currently passes
    # ! Not functional
    def getGrades(self):
        pass

    # Defines the "getAverage" function to get the average of a specific student
    # ! Not functioning/untested due to not being able to add students/grades
    def getAverage(self, studentName):
        # Sets the local variable "average" to be equal to the sum of the grades of a student divided by the total number of
        # the grades which they have/length of it
        self.average = sum(self.grades(studentName)) / len(self.grades(studentName))
        # Returns the student name has an average score of and then their average score
        return studentName + " has an average score of: " + self.average
    # Defines the "getClassAverage" which calculates the class average
    # ! Not currently fully functional due to not being able to add students/grades
    def getClassAverage(self):
        self.classAverage = None
        return "The class average is: " + self.classAverage

    # Defines the "getClassStudentsTotal" which calculates how many students are in the course
    # ! Not currently functional due to not being able to add students
    def getClassStudentsTotal(self):
        self.classStudentsTotal = None
        return "There are " + classStudentsTotal + "students in this class."

    # Defines the "setInstructorName" function and sets a variable "instructorName" to the eigth input of the "Class" class
    def setInstructorName(self, newInstructorName):
        self.instructorName = newInstructorName
    # Defines the "getInstructorName" function and sets it to return the current "instructorName" variable
    def getInstructorName(self):
        return self.instructorName

# Defines the class "Student"
class Student():
    def __init__(self, firstName, lastName, gender, id, email):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.email = email
        self.id = id

    # Defines the "setFirstName" function and sets a variable "firstName" to the first input of the "Student" class
    def setFirstName(self, newFirstName):
        self.firstName = newFirstName
    # Defines the "getFirstName" function and sets it to return the current "firstName" variable
    def getFirstName(self):
        return self.firstName

    # Defines the "setLastName" function and sets a variable "lastName" to the second input of the "Student" class
    def setLastName(self, newLastName):
        self.lastName = newLastName
    # Defines the "getLastName" function and sets it to return the current "lastName" variable
    def getLastName(self):
        return self.lastName

    # Defines the "setGender" function and sets a variable "gender" to the third input of the "Student" class
    def setGender(self, newGender):
        self.gender = newGender
    # Defines the "getGender" function and sets it to return the current "gender" variable
    def getGender(self):
        return self.gender

    # Defines the "setID" function and sets a variable "id" to the fourth input of the "Student" class
    def setID(self, newID):
        self.id = newID
    # Defines the "getID" function and sets it to return the current "id" variable
    def getID(self):
        return self.id

    # Defines the "setEmail" function and sets a variable "email" to the fifth input of the "Student" class
    def setEmail(self, newEmail):
        self.email = newEmail
    # Defines the "getEmail" function and sets it to return the current "email" variable
    def getEmail(self):
        return self.email

    # Defines the "getFullName" function and returns a concatenation of the student's first name and last name
    def getFullName(self):
        return self.getFirstName() + " " +self.getLastName()

    # If the class "Student" is printed as a specific student for example "print(student1)" it returns what's in "__str__"
    def __str__(self):
        # We detect if the gender is equal to male
        if self.getGender() == "male":
            # If the gender is equal to male their pronoun is "His"
            pronoun = "His"
        # If the gender is not equal to male we make sure the gender is equal to female
        elif self.getGender() == "female":
            # If the gender is then equal to female their pronoun is "Her"
            pronoun = "Her"
        # Returns a concatenated list of the students first name, their email and their pronoun with their id
        return self.getFirstName() + " " + self.getLastName() + ", has the following email address: " + self.getEmail() + ". " + str(pronoun) + " id is " + str(self.getID())

# I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own.
# Dalton Murray


# Testing code copy and paste from assignment
python = Class('Fall 2021', '01', 'IT', 2114, 1234, 'Fundamentals of programming', 3)

student1 = Student('John', 'Smith', 'male', 123, 'john.smith@gmail.com')
student2 = Student('Sara', 'Hamid', 'female', 124, 'sara.hamid@gmail.com')
student3 = Student('Lu', 'Zhang', 'male', 125, 'lu.zhang@gmail.com')

python.addStudents([student1, student2])
python.addStudent(student3)

print(student1)
print(student2)