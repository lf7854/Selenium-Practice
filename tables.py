from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe")
browser.get("https://testautomationpractice.blogspot.com/")
rows = browser.find_elements("xpath","/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr")
columns = browser.find_elements("xpath","/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr[1]/th")

for row in range(2, len(rows) + 1):
    for column in range(1, len(columns) + 1):
        result = browser.find_element("xpath","/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr[" + str(row) + "]/td[" + str(column) + "]").text
        print(result, end="    ")
    print()

time.sleep(2)
browser.quit()
