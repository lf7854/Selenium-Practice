from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.get("https://testautomationpractice.blogspot.com/")
browser.switch_to.frame("frame-one1434677811")
browser.find_element("id","RESULT_FileUpload-11").send_keys("C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")

time.sleep(2)
browser.quit()
