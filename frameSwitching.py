from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
browser.switch_to.frame("packageListFrame")
browser.find_element_by_link_text("com.thoughtworks.selenium").click()

browser.switch_to.default_content()
browser.switch_to.frame("packageFrame")
browser.find_element_by_link_text("CommandProcessor").click()

browser.switch_to.default_content()
browser.switch_to.frame("classFrame")
browser.find_element_by_link_text("Deprecated".upper()).click()
