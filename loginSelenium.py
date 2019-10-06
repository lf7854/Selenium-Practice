import openxlUtility as xl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyodbc

filePath = "C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\downloadFiles\\"
fileName = "Login.xlsx"
sheetName = "LoginDetails"

workbook = xl.createWorkBook()
xl.createWorkSheet(workbook, sheetName)
xl.saveWorkbook(fileName,filePath,workbook)

connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=localhost\\SQLEXPRESS01;Database=Login;Trusted_Connection=yes;')
cursor = connection.cursor()
cursor.execute("select userName, password from loginUsers")

i = 1
xl.writeData(filePath + fileName, sheetName, i, 1, "UserName")
xl.writeData(filePath + fileName, sheetName, i, 2, "Password")
xl.writeData(filePath + fileName, sheetName, i, 3, "Results")
i = i + 1
for row in cursor:
    (userName, password) = row
    xl.writeData(filePath + fileName, sheetName, i, 1, userName)
    xl.writeData(filePath + fileName, sheetName, i, 2, password)
    i = i + 1

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.maximize_window()
browser.get("http://newtours.demoaut.com/")

rows = xl.getRowCount(filePath + fileName, sheetName)
columns = xl.getColumnCount(filePath + fileName, sheetName)

for row in range(2,rows + 1):
    userName = xl.readData(filePath + fileName, sheetName, row, 1)
    password = xl.readData(filePath + fileName, sheetName, row, 2)

    browser.find_element("name","userName").send_keys(userName)
    browser.find_element("name","password").send_keys(password)
    browser.find_element("name","login").click()

    linkText = browser.find_element("partial link text","SIGN-").get_attribute("text")
    linkText = linkText.lower()
    xl.writeData(filePath + fileName, sheetName, row, 3, "Success" if linkText == "sign-off" else "Failure")
    browser.find_element("link text","Home").click()
    
time.sleep(2)
browser.quit()
