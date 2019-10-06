from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.maximize_window()
browser.get("https://testautomationpractice.blogspot.com/")
copyText = browser.find_element("xpath","/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")
actions = ActionChains(browser)
actions.double_click(copyText).perform()
time.sleep(2)
browser.quit()
