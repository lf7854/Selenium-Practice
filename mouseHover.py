from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.maximize_window()
browser.get("https://opensource-demo.orangehrmlive.com")

browser.find_element("id","txtUsername").send_keys("Admin")
browser.find_element("id","txtPassword").send_keys("admin123")
browser.find_element("xpath","/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click()
time.sleep(2)

firstLevel = browser.find_element("xpath","/html/body/div[1]/div[2]/ul/li[1]/a")
secondLevel = browser.find_element("xpath","/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a")
thirdLevel = browser.find_element("xpath","/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a")

actions = ActionChains(browser)
actions.move_to_element(firstLevel).move_to_element(secondLevel).move_to_element(thirdLevel).click().perform()

time.sleep(10)
browser.quit()
