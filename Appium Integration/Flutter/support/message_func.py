from appium import webdriver
from unittest import TestCase
from support import message_mapping, desiredcapabilities
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)

def test_search_for_new_chat(driver, friend_name, msg):
    """it searching for new chats"""
    # element = driver.find_elements_by_xpath(message_mapping.BAR_XPATH)
    # element.find_elements_by_accessibility_id(message_mapping.HOME_MESSAGE_ICON_ACCESSE_ID).click()
    TouchAction(driver).tap(None, 600, 2130, 1).perform()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(message_mapping.NEW_MESSAGE_BUTTON_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(message_mapping.SEARCH_FOR_NEW_FRIND_XPATH).send_keys(friend_name)
    driver.implicitly_wait(50)
    driver.find_element_by_accessibility_id(friend_name).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(message_mapping.SAY_SOMETHING_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(message_mapping.SAY_SOMETHING_XPATH).send_keys(msg)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(message_mapping.SEND_BUTTON_XPATH).click()
    driver.implicitly_wait(30)
    text = driver.find_element_by_accessibility_id(msg).text
    assert text, msg
    driver.find_element_by_accessibility_id(message_mapping.BACK_BUTTON_ACCESSE_ID).click()
    return True

def access_first_chat(driver):
    """it access first chat in my chats"""    
    # driver.find_element_by_accessibility_id(message_mapping.HOME_MESSAGE_ICON_ACCESSE_ID).click()
    # driver.implicitly_wait(30)
    try:
        driver.find_element_by_accessibility_id(message_mapping.A_FRIEND_ACCESSE_ID).click()
        return True
    except:
        return False

def delete_conversation(driver):
    boolean= access_first_chat(driver)
    if boolean: 
        driver.find_element_by_accessibility_id(message_mapping.MORE_OPTIONS_ACCESSE_ID).click()
        driver.implicitly_wait(30)
        driver.find_element_by_accessibility_id(message_mapping.DELETE_CONVE_ACCESSE_ID).click()
        driver.implicitly_wait(30)
        driver.find_element_by_accessibility_id(message_mapping.DELETE_BUTTON_TO_CONFIRM_ACCESSE_ID).click()
        driver.implicitly_wait(30)
    boolean1 = access_first_chat(driver)
    return boolean1^boolean


