from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
actions = ActionChains(browser)
time.sleep(2)
rightClickElement = browser.find_element("xpath","/html/body/div/section/div/div/div/p/span")
actions.context_click(rightClickElement).perform()
time.sleep(2)
browser.find_element("xpath","/html/body/ul/li[1]").click()
time.sleep(2)
browser.switch_to.alert.accept()
time.sleep(2)
browser.quit()
