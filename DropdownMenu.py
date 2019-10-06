from tkinter import *


class LoginSSO:
    def loginUser(self):
        pass

    def resetFields(self):
        pass

    def createForm(self):
        self.labelName = Label(rootWindow, text="Name")
        self.labelPassword = Label(rootWindow, text="Password")
        self.entryName = Entry(rootWindow)
        self.entryPassword = Entry(rootWindow)
        self.checkLoggedIN = Checkbutton(rootWindow, text="Keep me logged in")

        self.loginButton = Button(rootWindow, text="Login", command=self.loginUser)
        self.resetButton = Button(rootWindow, text="Reset", command=self.resetFields)
        self.exitButton = Button(rootWindow, text="Exit", command=self.frame.quit)

        self.labelName.grid(row=0, column=0, sticky=E)
        self.labelPassword.grid(row=1, column=0, sticky=E)
        self.entryName.grid(row=0, column=1, columnspan=2)
        self.entryPassword.grid(row=1, column=1, columnspan=2)
        self.checkLoggedIN.grid(row=2, columnspan=3)
        self.loginButton.grid(row=3, column=0, sticky=E)
        self.resetButton.grid(row=3, column=1)
        self.exitButton.grid(row=3, column=2, sticky=W)
    
    def __init__(self, master):
        self.frame = Frame(master)
        self.createForm()

rootWindow = Tk()
loginSSO = LoginSSO(rootWindow)
width  = rootWindow.winfo_screenwidth()
height = rootWindow.winfo_screenheight()
rootWindow.geometry(f'{width}x{height}')
rootWindow.mainloop()
