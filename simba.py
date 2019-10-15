from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
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

driver = webdriver.Ie(capabilities=capability,executable_path=r"C:\Users\mflor181\Downloads\Python Files\Drivers\IEDriverServer.exe")
time.sleep(2)
driver.quit()
driver = None

browser = webdriver.Ie(r"C:\Users\mflor181\Downloads\Python Files\Drivers\IEDriverServer.exe")
browser.maximize_window()
browser.get("http://10.235.10.205/")

events = eventClass(browser)
browser.switch_to.frame("bot")
browser.find_element("link text","International Solutions").click()
browser.switch_to.default_content()
browser.switch_to.frame("bot")
browser.find_element("link text","AVG").click()
Select(browser.find_element("css selector","select[name=username]")).select_by_visible_text("2206")
browser.find_element("css selector","input[name=password]").send_keys("ball@12345")
browser.find_element("css selector","input[name=submit]").click()

browser.switch_to.default_content()
browser.switch_to.frame("bot")
browser.switch_to.frame("leftspdwcsp.asp")
browser.find_element("link text","Bye").click()
browser.switch_to.default_content()

time.sleep(5)
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
