from appium import webdriver
from unittest import TestCase
import desiredcapabilities

driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)

def valid_log_out():
    """it to log out from app"""
    driver.find_element_by_accessibility_id("ACCOUNT").click()
    driver.implicitly_wait(30)
    driver.find_element_by_accessibility_id("Account").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/account_settings").click()
    driver.implicitly_wait(30)
    while True:
        driver.swipe(150, 400, 150, 200, 1000)
        try:
            driver.find_element_by_id("com.tumblr:id/log_out")
        except:
            continue
        break
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/log_out").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("android:id/button1").click()
    return 
