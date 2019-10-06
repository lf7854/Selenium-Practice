from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

dragElement = browser.find_element("xpath","/html/body/div[2]/div[2]/div/div[12]")
dropElement = browser.find_element("xpath","/html/body/div[2]/div[3]/div[1]")

actions = ActionChains(browser)
actions.drag_and_drop(dragElement,dropElement).perform()

time.sleep(5)
browser.quit()
