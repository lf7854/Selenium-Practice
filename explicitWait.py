from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from datetime import timedelta
import time


browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.maximize_window()
browser.get("https://www.expedia.co.in/")
browser.find_element("id","tab-flight-tab-hp").click()

flyingFrom = browser.find_element("id","flight-origin-hp-flight")
flyingFrom.send_keys("Mumbai")
time.sleep(1)
flyingFrom.send_keys(Keys.TAB)

flyingTo = browser.find_element("id","flight-destination-hp-flight")
flyingTo.send_keys("Delhi")
time.sleep(1)
flyingTo.send_keys(Keys.TAB)

departingDate = browser.find_element("id","flight-departing-hp-flight")
departingDate.send_keys((datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"))

returnDate = browser.find_element("id","flight-returning-hp-flight")
returnDate.clear()
print(returnDate.get_attribute("value"))
for i in range(10):
    returnDate.send_keys(Keys.BACKSPACE)
returnDate.send_keys((datetime.now() + timedelta(days=2)).strftime("%d/%m/%Y"))

browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/button").click()

adult = browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button").click()

child = browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[2]/div[1]/div[4]/button").click()
browser.find_element("xpath","//*[@id='flight-age-select-1-hp-flight']/option[16]").click()

infant = browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[3]/div[1]/div[4]/button").click()
browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[3]/div[2]/label[1]/select/option[2]").click()

browser.find_element("id","flight-children-in-seat-hp-flight-sa").click()

browser.find_element("xpath","//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

wait = WebDriverWait(browser, 10)
cheapElement = wait.until(ec.element_to_be_clickable(("xpath","//*[@id='flightModuleList']/li[1]/div[1]/div[1]/div[2]/div/div[2]/button")))
cheapElement.click()

time.sleep(5)
browser.quit()
