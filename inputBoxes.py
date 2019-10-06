from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def findAllInput(browser):
    textBox = browser.find_elements("css selector","input[type=text]")
    dropDown = browser.find_elements("css selector","select")
    textArea = browser.find_elements("css selector","textarea")
    fileUploader = browser.find_elements("css selector","input[type=file]")
    radioButton = browser.find_elements("css selector","input[type=radio]")
    checkBox = browser.find_elements("css selector","input[type=checkbox]")
    
browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")

browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
findAllInput(browser)

element = browser.find_element("tag name","select")
dropdown = Select(element)

time.sleep(5)
browser.quit()
