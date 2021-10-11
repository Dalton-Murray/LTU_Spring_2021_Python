#####################
## Dalton Murray    #
## 04/26/20201      #
## Class notes      #
#####################

import tkinter

class Gui():
    def __init__(self):
        self.gui = tkinter.Tk()
        self.gui.title("Calculator")
        self.gui.geometry("250x250")
        self.mathType = tkinter.StringVar()
        self.firstVar = tkinter.StringVar()
        self.secondVar = tkinter.StringVar()
        self.thirdVar = tkinter.StringVar()

        self.entry1 = tkinter.Entry(self.gui, textvariable=self.mathType)
        self.entry1.pack()

        self.entry2 = tkinter.Entry(self.gui, textvariable=self.firstVar)
        self.entry2.pack()

        self.entry3 = tkinter.Entry(self.gui,textvariable=self.secondVar)
        self.entry3.pack()

        self.entry4 = tkinter.Entry(self.gui, textvariable=self.thirdVar)
        self.entry4.pack()

        def myFunc():
            firstNum = self.firstVar.get()
            secondNum = self.secondVar.get()
            mathType = self.mathType.get()
            mathType = mathType.lower()

            if mathType == "add":
                thirdVar = float(firstNum) + float(secondNum)
            elif mathType == "subtract":
                thirdVar = float(firstNum) - float(secondNum)
            elif mathType == "divide":
                thirdVar = float(firstNum) / float(secondNum)
            elif mathType == "multiply":
                thirdVar = float(firstNum) * float(secondNum)

            self.label1.config(text=thirdVar)

            self.thirdVar.set(thirdVar)

        self.label1 = tkinter.Label(self.gui, text="")
        self.label1.pack()

        self.btn1 = tkinter.Button(self.gui, text="Click me", command=myFunc, width=15, height=5)
        self.btn1.pack()

        tkinter.mainloop()


if __name__ == "__main__":
    myGui = Gui()