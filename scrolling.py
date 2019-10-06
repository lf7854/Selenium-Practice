from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.maximize_window()

browser.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
browser.execute_script("window.scroll(0,500)","")
time.sleep(2)
element = browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
browser.execute_script("arguments[0].scrollIntoView()",element)
time.sleep(2)
browser.execute_script("window.scroll(0,document.body.scrollHeight)","")

time.sleep(5)
browser.quit()
