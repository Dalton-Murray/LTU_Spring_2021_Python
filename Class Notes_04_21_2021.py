#####################
## Dalton Murray    #
## 04/21/20201      #
## Class notes      #
#####################

import tkinter
import tkinter.messagebox
# from tkinter import *

class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        # Sets window title
        self.main_window.title("Application")
        # Sets window dimensions
        self.main_window.geometry("400x400")
        self.name_var = tkinter.StringVar()

        # Creates a callable method to open a message box
        def myFunc():
            # tkinter.messagebox.showinfo("Message Box", "Welcome")
            name = self.name_var.get()
            print("The user name is: " + name)

        self.name1 = tkinter.Entry(self.main_window, font=("Arial", 12, "bold"), textvariable=self.name_var)
        self.name1.pack()

        # Creates a label with the set information
        self.label1 = tkinter.Label(self.main_window, text="My Label",\
                                    borderwidth=1, relief="solid", fg="blue",\
                                    bg="yellow")

        # Creates a button that on click runs the "myFunc" method
        self.btn1 = tkinter.Button(text="Click me!", command=myFunc, width=30, height=10)

        # Packs btn1
        self.btn1.pack()

        # Packs label1 with specific information
        self.label1.pack(side="left", ipady=20, ipadx=20, padx=20, pady=20)

        tkinter.mainloop()

# Ensures that the GUI opens
if __name__ == "__main__":
    myGUI = MyGUI()