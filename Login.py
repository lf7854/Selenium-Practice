from tkinter import *


class LoginSSO:
    def loginUser(self):
        pass

    def resetFields(self):
        pass

    def createForm(self):
        self.labelName = Label(self.frame, text="Name")
        self.labelPassword = Label(self.frame, text="Password")
        self.entryName = Entry(self.frame)
        self.entryName.focus()
        self.entryPassword = Entry(self.frame)
        self.checkLoggedIN = Checkbutton(self.frame, text="Keep me logged in")

        self.loginButton = Button(self.frame, text="Login", command=self.loginUser)
        self.resetButton = Button(self.frame, text="Reset", command=self.resetFields)
        self.exitButton = Button(self.frame, text="Exit", command=self.frame.quit)

        self.labelName.grid(row=0, column=0, sticky=E, pady=(50,10), padx=(25,10))
        self.labelPassword.grid(row=1, column=0, sticky=E, padx=(25,10))
        self.entryName.grid(row=0, column=1, columnspan=2, pady=(50,10), padx=(10,25))
        self.entryPassword.grid(row=1, column=1, columnspan=2, padx=(10,25))
        self.checkLoggedIN.grid(row=2, columnspan=3, sticky=W, padx=(20))
        self.loginButton.grid(row=3, column=0, columnspan=3, pady=(10,25))
        self.resetButton.grid(row=3, column=1, columnspan=3, pady=(10,25))
        self.exitButton.grid(row=3, column=2, columnspan=3, pady=(10,25))
    
    def __init__(self, master):
        self.frame = Frame(master)
        self.createForm()

rootWindow = Tk()
positionRight = int(((rootWindow.winfo_screenwidth() / 2) - (rootWindow.winfo_reqwidth() / 2)))
positionDown = int(((rootWindow.winfo_screenheight() / 2) - (rootWindow.winfo_reqheight() / 2)))
rootWindow.geometry(f'+{positionRight}+{positionDown}')

loginSSO = LoginSSO(rootWindow)
