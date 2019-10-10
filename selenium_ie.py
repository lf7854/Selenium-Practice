from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
from datetime import timedelta
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.ie.options import Options

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import winreg

class eventClass:
    def __init__(self, browser):
        self.browser = browser

    def clickEvent(self, element):
        self.browser.execute_script("arguments[0].click()",element)

    def setValue(self, element, value):
        self.browser.execute_script("arguments[0].setAttribute('value','" + value + "')", element)


commonPath = r"Software\Microsoft\Internet Explorer"
regPath = commonPath + r"\Zoom"
registryKey = "ZoomFactor"
registryVal = 100000

winreg.CreateKey(winreg.HKEY_CURRENT_USER, regPath)
registry = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regPath, 0 ,winreg.KEY_WRITE)
winreg.SetValueEx(registry, registryKey, 0, winreg.REG_DWORD, registryVal)
winreg.CloseKey(registry)

regPath = commonPath + r"\Geolocation"
registryKey = "BlockAllWebsites"
registryVal = 1

winreg.CreateKey(winreg.HKEY_CURRENT_USER, regPath)
registry = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regPath, 0 ,winreg.KEY_WRITE)
winreg.SetValueEx(registry, registryKey, 0, winreg.REG_DWORD, registryVal)
winreg.CloseKey(registry)
    
commonPath = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones"

for i in range(1,5):
    regPath = commonPath + "\\" + str(i)
    registryKey = "2500"
    registryVal = 3
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, regPath)
    registry = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regPath, 0 ,winreg.KEY_WRITE)
    winreg.SetValueEx(registry, registryKey, 0, winreg.REG_DWORD, registryVal)
    winreg.CloseKey(registry)
    
print("Completed")


capability = DesiredCapabilities().INTERNETEXPLORER

capability['nativeEvents'] = False
capability['unexpectedAlertBehaviour'] = 'accept'

capability['se:ieOptions'] = {}
capability['se:ieOptions']['ie.ignore_protected_mode_settings'] = True
capability['se:ieOptions']['ie.ignore_zoom_level'] = True
capability['se:ieOptions']['ie.require_window_focus'] = True
capability['se:ieOptions']['ie.ensureCleanSession'] = True

capability['disable-popup-blocking'] = True
capability['enablePersistentHover'] = True
capability['ignoreZoomSetting'] = True
capability['enableElementCacheCleanup'] = True

browser = webdriver.Ie(capabilities=capability,executable_path=r"C:\Vipul Singh DF\Drivers\IEDriverServer_Win32_3.14.0\IEDriverServer.exe")
browser.maximize_window()
browser.get("https://www.expedia.co.in/")

events = eventClass(browser)

time.sleep(5)
flightElement = browser.find_element("id","tab-flight-tab-hp")
print(flightElement)
events.clickEvent(flightElement)

flyingFrom = browser.find_element("id","flight-origin-hp-flight")
events.setValue(flyingFrom, "Mumbai")

flyingTo = browser.find_element("id","flight-destination-hp-flight")
events.setValue(flyingTo, "Delhi")

departingDate = browser.find_element("id","flight-departing-hp-flight")
events.setValue(departingDate, (datetime.now() + timedelta(days = 1)).strftime("%d/%m/%Y"))

returnDate = browser.find_element("id","flight-returning-hp-flight")
events.setValue(returnDate, (datetime.now() + timedelta(days = 2)).strftime("%d/%m/%Y"))

travelElement = browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/button")
events.clickEvent(travelElement)

adult = browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button")
events.clickEvent(adult)

child = browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[2]/div[1]/div[4]/button")
events.clickEvent(child)

Select(browser.find_element("xpath","//*[@id='flight-age-select-1-hp-flight']")).select_by_visible_text("16")

infant = browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[3]/div[1]/div[4]/button")
events.clickEvent(infant)

Select(browser.find_element("xpath","//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[3]/div[2]/label[1]/select")).select_by_index(2)

childSeat = browser.find_element("id","flight-children-in-seat-hp-flight-sa")
events.clickEvent(childSeat)

searchButton = browser.find_element("xpath","//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button")
events.clickEvent(searchButton)

cheapElement = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(("xpath","//*[@id='flightModuleList']/li[1]/div[1]/div[1]/div[2]/div/div[2]/button")))
events.clickEvent(cheapElement)

time.sleep(10)
browser.quit()

commonPath = r"Software\Microsoft\Internet Explorer"
regPath = commonPath + r"\Geolocation"
registryKey = "BlockAllWebsites"
registryVal = 0

winreg.CreateKey(winreg.HKEY_CURRENT_USER, regPath)
registry = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regPath, 0 ,winreg.KEY_WRITE)
winreg.SetValueEx(registry, registryKey, 0, winreg.REG_DWORD, registryVal)
winreg.CloseKey(registry)
    
commonPath = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones"

for i in range(1,5):
    regPath = commonPath + "\\" + str(i)
    registryKey = "2500"
    registryVal = 0
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, regPath)
    registry = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regPath, 0 ,winreg.KEY_WRITE)
    winreg.SetValueEx(registry, registryKey, 0, winreg.REG_DWORD, registryVal)
    winreg.CloseKey(registry)
    
print("Completed")
