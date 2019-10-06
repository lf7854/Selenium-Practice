from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.maximize_window()
browser.get("http://demo.automationtesting.in/Windows.html")
browser.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

handles = browser.window_handles

for handle in handles:
    browser.switch_to.window(handle)
    time.sleep(3)

browser.quit()
