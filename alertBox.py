from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.get("https://www.google.com/")

browser.execute_script("alert('Please test for OK')","")
time.sleep(1)
browser.switch_to.alert.accept()

browser.execute_script("confirm('Please test for OK')","")
time.sleep(1)
browser.switch_to.alert.accept()

browser.execute_script("confirm('Please test for CANCEL')","")
time.sleep(1)
browser.switch_to.alert.dismiss()

time.sleep(1)
browser.quit()
