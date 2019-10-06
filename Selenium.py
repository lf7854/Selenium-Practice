from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.get('https://www.amazon.in/')
print(browser.title)

txtSearch = browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
txtSearch.send_keys("iPhone")
txtSearch.send_keys(Keys.RETURN)

browser.close()
