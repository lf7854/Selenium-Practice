from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchResult:
    def __init__(self, master):
        root = master

        self.labelLink = Label(root, text="Link:")
        self.entryLink = Entry(root)
        self.entryLink.focus()
                
        self.labelSearch = Label(root, text="Search:")
        self.entrySearch = Entry(root)

        self.searchButton = Button(root, text="Search", command=self.openBrowser)

        self.labelLink.grid(row=0, column=0, pady=(25,5), padx=(10))
        self.entryLink.grid(row=0, column=1, pady=(25,5), padx=(10))

        self.labelSearch.grid(row=1, column=0, pady=(5), padx=(10))
        self.entrySearch.grid(row=1, column=1, pady=(5), padx=(10))
        self.searchButton.grid(row=2, columnspan=2, pady=(10), padx=(10))


    def openBrowser(self):
        browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
        browser.get(self.entryLink.get())
        txtSearch = browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
        txtSearch.send_keys(self.entrySearch.get())
        txtSearch.send_keys(Keys.RETURN)
        browser.quit()


def centerAlign(root):
    positionRight = int(((root.winfo_screenwidth() / 2) - (root.winfo_reqwidth() / 2)))
    positionDown = int(((root.winfo_screenheight() / 2) - (root.winfo_reqheight() / 2)))
    return f'+{positionRight}+{positionDown}'


rootWindow = Tk()
searchResult = SearchResult(rootWindow)
rootWindow.geometry(centerAlign(rootWindow))
rootWindow.mainloop()
