#####################
## Dalton Murray    #
## 04/19/20201      #
## Class notes      #
#####################

import tkinter

class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Application")
        self.label1 = tkinter.Label(self.main_window, text="My Label",\
                                    borderwidth=1, relief="solid", fg="blue",\
                                    bg="yellow")
        self.btn1 = tkinter.Button(text="Click me!", width=30, height=10)
        self.btn1.pack()
        self.label1.pack(side="left", ipady=20, ipadx=20, padx=20, pady=20)

        tkinter.mainloop()

if __name__ == "__main__":
    myGUI = MyGUI()