#####################
## Dalton Murray    #
## 04/28/20201      #
## Class notes      #
#####################

import tkinter

class Gui():
    def __init__(self):
        self.gui = tkinter.Tk()

        def myFunc():
            if self.btn["state"] == "normal":
                self.btn["state"] = "disable"
                self.btn["text"] = "disabled"

        self.btn = tkinter.Button(self.gui, text="Click", command=myFunc)
        self.btn.pack()

        tkinter.mainloop()

if __name__ == "__main__":
    myGui = Gui()