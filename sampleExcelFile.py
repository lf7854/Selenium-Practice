from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from zipfile import ZipFile
import os

chromeOption = Options()
chromeOption.add_experimental_option("prefs",{"download.default_directory" : "C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\downloadFiles"})
browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe", options = chromeOption)
browser.get("https://www.contextures.com/xlSampleData01.html")
browser.find_element_by_link_text("Excel sample data workbook").click()
time.sleep(3)
while True:
    if os.path.exists("C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\downloadFiles\\SampleData.zip"):
        with ZipFile("C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\downloadFiles\\SampleData.zip",'r') as zip:
            os.chdir("C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\downloadFiles")
            zip.extractall()
            break
os.remove("C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\downloadFiles\\SampleData.zip")
browser.quit()
