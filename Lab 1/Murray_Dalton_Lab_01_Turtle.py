#####################
## Dalton Murray    #
## 02/16/20201      #
## Lab 01 Turtle    #
#####################

#Imports turtle library for use
import turtle

#Begins startup process
win = turtle.Screen()
#Sets background color to white
win.bgcolor("white")
#Sets the window title to "House"
win.title("House")
#Sets turtle
Turtle = turtle.Turtle()

#Defines main function for running other functions
def __main__():
    
    #Trees
    __farRightTree__()
    __midLeftTree__()
    __frontRightTree__()
    
    #House
    __houseBottomBox__()
    __houseRoofMain__()
    __houseRoofChimney__()
    __houseLeftWindow__()
    __houseRightWindow__()
    __houseDoor__()
    __houseDoorKnob__()
    
    #Sun
    __sun__()

def __houseBottomBox__():
    #Main house
    #Pulls up the turtle's pen so it isn't drawing
    Turtle.penup()
    #Makes the turtle go to the bottom left of the house to start
    Turtle.goto(-300, -250)
    #Sets down the turtle pen so it can draw
    Turtle.pendown()
    #Sets brush thickness
    Turtle.pensize(5)

    #Starts drawing basic shape of house
    Turtle.fillcolor("#e1c699")
    #Begins filling house bottom box
    Turtle.begin_fill()
    Turtle.fd(300)
    Turtle.lt(90)
    Turtle.fd(250)
    Turtle.lt(90)
    Turtle.fd(300)
    Turtle.lt(90)
    Turtle.fd(250)
    Turtle.end_fill()

def __houseRoofMain__():
    #Starts Roof
    #Gets in position
    Turtle.penup()
    Turtle.lt(180)
    Turtle.fd(250)
    Turtle.lt(90)
    Turtle.pendown()
   
    #Begins filling house roof
    Turtle.begin_fill()
    Turtle.fd(50)
    Turtle.rt(140)
    Turtle.fd(260)
    Turtle.rt(80)
    Turtle.fd(260)
    Turtle.rt(140)
    Turtle.fd(49)
    Turtle.end_fill()

def __houseRoofChimney__():
    #Get turtle in position
    Turtle.penup()
    Turtle.goto(-230, 75)
    Turtle.pendown()
    
    #Begins filling in chimney
    #Sets pen size
    Turtle.pensize(3)
    #Sets fill color
    Turtle.fillcolor("#996666")
    Turtle.begin_fill()
    Turtle.rt(90)
    Turtle.fd(80)
    Turtle.rt(90)
    Turtle.fd(30)
    Turtle.rt(90)
    Turtle.fd(80)
    Turtle.rt(90)
    Turtle.fd(30)
    Turtle.end_fill()

def __houseLeftWindow__():
    #Get turtle in position
    Turtle.penup()
    Turtle.goto(-250,-100)
    Turtle.pendown()
    
    #Begins filling window
    #Sets fill color
    Turtle.fillcolor("white")
    Turtle.begin_fill()
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.end_fill()
    #Cross pattern
    Turtle.rt(180)
    Turtle.fd(25)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.lt(90)
    Turtle.fd(25)
    Turtle.lt(90)
    Turtle.fd(25)
    Turtle.lt(90)
    Turtle.fd(50)

def __houseRightWindow__():
    #Get turtle in position
    Turtle.penup()
    Turtle.goto(-70,-50)
    Turtle.pendown()
    
    #Begins filling window
    Turtle.begin_fill()
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.end_fill()
    #Cross pattern
    Turtle.rt(180)
    Turtle.fd(25)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.lt(90)
    Turtle.fd(25)
    Turtle.lt(90)
    Turtle.fd(25)
    Turtle.lt(90)
    Turtle.fd(50)

def __houseDoor__():
    #Get in position
    Turtle.penup()
    Turtle.goto(-180,-250)
    Turtle.pendown()
    #Begins filling door
    #Sets fill color
    Turtle.fillcolor("#009dc4")
    Turtle.begin_fill()
    Turtle.rt(90)
    Turtle.fd(100)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
    Turtle.fd(100)
    Turtle.end_fill()

def __houseDoorKnob__():
    #Get in position    
    Turtle.penup()
    Turtle.rt(180)
    Turtle.fd(45)
    Turtle.lt(90)
    Turtle.fd(10)
    Turtle.dot(8)

def __sun__():
    #Get in position
    Turtle.penup()
    Turtle.goto(-250, 275)
    Turtle.pendown()
    #Sun dot
    Turtle.dot(95, "#FFFF00")
    
def __farRightTree__():
    #Get in position
    Turtle.penup()
    Turtle.goto(180, 110)
    Turtle.pendown()
    #Begins filling tree
    #Sets fill color
    Turtle.lt(90)
    Turtle.fillcolor("#765c48")
    Turtle.pensize(3)
    Turtle.begin_fill()
    Turtle.fd(75)
    Turtle.lt(90)
    Turtle.fd(25)
    Turtle.lt(90)
    Turtle.fd(75)
    Turtle.lt(90)
    Turtle.fd(25)
    Turtle.end_fill()
    
    #Tree leaves
    #Get in position
    Turtle.penup()
    Turtle.goto(168, 180)
    Turtle.pendown()
    #Fill leaves
    Turtle.fillcolor("#288b22")
    Turtle.begin_fill()
    Turtle.circle(30)
    Turtle.end_fill()
    
    #Tree fruits
    #Get in position
    Turtle.penup()
    Turtle.goto(170,190)
    Turtle.pendown()
    #FIll fruits
    Turtle.dot(8,"#9b870c")
    Turtle.penup()
    Turtle.goto(185,205)
    Turtle.pendown()
    Turtle.dot(8,"#9b870c")
    Turtle.penup()
    Turtle.goto(190, 215)
    Turtle.pendown()
    Turtle.dot(8,"#9b870c")
    Turtle.penup()
    Turtle.goto(155, 225)
    Turtle.pendown()
    Turtle.dot(8,"#9b870c")
    Turtle.penup()
    Turtle.goto(155, 195)
    Turtle.pendown()
    Turtle.dot(8,"#9b870c")

def __midLeftTree__():
    #Get in position
    Turtle.penup()
    Turtle.goto(75, -40)
    Turtle.pendown()
    #Begins filling tree
    #Sets fill color
    Turtle.lt(90)
    Turtle.fillcolor("#765c48")
    Turtle.begin_fill()
    Turtle.fd(160)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.lt(90)
    Turtle.fd(160)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.end_fill()
    
    #Tree leaves
    #Get in position
    Turtle.penup()
    Turtle.goto(50, 100)
    Turtle.pendown()
    #Fill leaves
    Turtle.fillcolor("#288b22")
    Turtle.begin_fill()
    Turtle.circle(50)
    Turtle.end_fill()
    
    #Tree fruits
    #Get in position
    Turtle.penup()
    Turtle.goto(50, 130)
    Turtle.pendown()
    #FIll fruits
    Turtle.dot(11,"#9b870c")
    Turtle.penup()
    Turtle.goto(70, 160)
    Turtle.pendown()
    Turtle.dot(11,"#9b870c")
    Turtle.penup()
    Turtle.goto(20, 180)
    Turtle.pendown()
    Turtle.dot(11,"#9b870c")
    Turtle.penup()
    Turtle.goto(38, 160)
    Turtle.pendown()
    Turtle.dot(11,"#9b870c")
    Turtle.penup()
    Turtle.goto(49, 175)
    Turtle.pendown()
    Turtle.dot(11,"#9b870c")
    Turtle.penup()
    Turtle.goto(60, 180)
    Turtle.pendown()
    Turtle.dot(11,"#9b870c")
    Turtle.penup()
    Turtle.goto(85, 190)
    Turtle.pendown()

def __frontRightTree__():
    #Get in position
    Turtle.penup()
    Turtle.goto(150, -120)
    Turtle.pendown()
    #Begins filling tree
    #Sets fill color
    Turtle.lt(90)
    Turtle.fillcolor("#765c48")
    Turtle.begin_fill()
    Turtle.fd(180)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.lt(90)
    Turtle.fd(180)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.end_fill()
    
    #Tree leaves
    #Get in position
    Turtle.penup()
    Turtle.goto(125, 50)
    Turtle.pendown()
    #Fill leaves
    Turtle.fillcolor("#288b22")
    Turtle.begin_fill()
    Turtle.circle(60)
    Turtle.end_fill()
    
    #Tree fruits
    #Get in position
    Turtle.penup()
    Turtle.goto(125, 75)
    Turtle.pendown()
    #FIll fruits
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    Turtle.goto(160, 120)
    Turtle.pendown()
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    Turtle.goto(150, 136)
    Turtle.pendown()
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    Turtle.goto(110, 160)
    Turtle.pendown()
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    Turtle.goto(95, 140)
    Turtle.pendown()
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    Turtle.goto(120, 125)
    Turtle.pendown()
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    Turtle.goto(80, 110)
    Turtle.pendown()
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    Turtle.goto(100, 100)
    Turtle.pendown()
    Turtle.dot(13,"#9b870c")
    Turtle.penup()
    
#Calls main function
__main__()

#Ensures the windows doesn't close when it is finished drawing
turtle.done()

#I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own.
#Dalton Murray