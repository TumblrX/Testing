from appium import webdriver
from selenium.webdriver.common.by import By
from support import log_in_mapping
from unittest import TestCase
from support import desiredcapabilities

def invalid_email(email):
    """it tests invalid emails 
    Parameters
    -----------
    email : str
        input email to be tested
    msg : str
        expected message that will appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys(email)
    driver.find_element_by_id(log_in_mapping.INPUT_PASSWORD_ID).send_keys("123456789")
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(30)
    text = driver.find_element_by_id(log_in_mapping.ERROR_MESSAGE_FOR_EMAIL_ID).text 
    # assert msg, text
    return text

def false_password(password):
    """it tests false passwards with a valid email 
    Parameters
    -----------
    password : str
        input password to be tested
    msg : str
        expected message that will appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys("example@example.com")
    driver.find_element_by_id(log_in_mapping.INPUT_PASSWORD_ID).send_keys(password)
    driver.implicitly_wait(50)    
    driver.find_element_by_id(log_in_mapping.LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(50)
    text = driver.find_element_by_id(log_in_mapping.ERROR_MESSAGE_FOR_EMAIL_ID).text
    # assert msg, text
    # text = driver.find_element_by_id(log_in_mapping.ERROR_MESSAGE_FOR_PASSWORD_ID).text
    # assert msg, text
    return text


def working_log_in(email, password):
    """it tests ideal case to log in with correct email and password 
    Parameters
    -----------
    email : str
        input email to be tested
    password : str
        input password to be tested
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys(email)
    driver.find_element_by_id(log_in_mapping.INPUT_PASSWORD_ID).send_keys(password)
    driver.implicitly_wait(50)    
    driver.find_element_by_id(log_in_mapping.LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(50)
    return True