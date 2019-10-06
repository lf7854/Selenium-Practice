from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOption = Options()
chromeOption.add_experimental_option("prefs",{"download.default_directory" : "C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\downloadFiles"})
browser = webdriver.Chrome(executable_path="C:\\Users\\Manish\\Downloads\\Pendrive Data\\Python Files\\drivers\\chromedriver.exe",options=chromeOption)

browser.get("http://demo.automationtesting.in/FileDownload.html")
browser.find_element("id","textbox").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod. Facilisis magna etiam tempor orci eu lobortis elementum nibh. Lacus vel facilisis volutpat est velit. Tincidunt id aliquet risus feugiat. Diam phasellus vestibulum lorem sed risus. Purus semper eget duis at tellus at urna. Justo nec ultrices dui sapien eget mi proin sed. Vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam. Dictum fusce ut placerat orci nulla pellentesque dignissim enim sit. Mattis ullamcorper velit sed ullamcorper morbi. Sed felis eget velit aliquet sagittis id consectetur purus. Nisi est sit amet facilisis magna etiam tempor. Id faucibus nisl tincidunt eget nullam non nisi est sit. Vitae auctor eu augue ut lectus. Ligula ullamcorper malesuada proin libero nunc consequat. Risus sed vulputate odio ut enim blandit volutpat maecenas.Lorem ipsum dolor sit amet")
browser.find_element("id","createTxt").click()
browser.find_element("id","link-to-download").click()

browser.find_element("id","pdfbox").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod. Facilisis magna etiam tempor orci eu lobortis elementum nibh. Lacus vel facilisis volutpat est velit. Tincidunt id aliquet risus feugiat. Diam phasellus vestibulum lorem sed risus. Purus semper eget duis at tellus at urna. Justo nec ultrices dui sapien eget mi proin sed. Vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam. Dictum fusce ut placerat orci nulla pellentesque dignissim enim sit. Mattis ullamcorper velit sed ullamcorper morbi. Sed felis eget velit aliquet sagittis id consectetur purus. Nisi est sit amet facilisis magna etiam tempor. Id faucibus nisl tincidunt eget nullam non nisi est sit. Vitae auctor eu augue ut lectus. Ligula ullamcorper malesuada proin libero nunc consequat. Risus sed vulputate odio ut enim blandit volutpat maecenas.Lorem ipsum dolor sit amet")
browser.find_element("id","createPdf").click()
browser.find_element("id","pdf-link-to-download").click()

time.sleep(5)
browser.quit()
