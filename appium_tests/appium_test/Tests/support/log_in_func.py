from appium import webdriver
from unittest import TestCase
from support import log_in_mapping

desiredcap = {
    "platformName": "Android",
    "platformVersion": "10.0",
    "deviceName": "Nada",
    "automationName": "Appium"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcap)

def invaled_email(email, msg):
    """it tests invalid emails 
    Parameters
    -----------
    email : str
        input email to be tested
    msg : str
        expected message that will appear
    """
    driver.find_element_by_xpath(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys(email)
    driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_BUTTON_ID).click()
    driver.implicitly_wait(30)
    text = driver.find_element_by_id(log_in_mapping.ERROR_MESSAGE_FOR_EMAIL_ID).text 
    assert msg, text
    return 

def false_password(password, msg):
    """it tests false passwards with a valid email 
    Parameters
    -----------
    password : str
        input password to be tested
    msg : str
        expected message that will appear
    """
    # driver.find_element_by_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    # driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys("nadaelsayed163@gmail.com")
    driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(log_in_mapping.CHOOSE_PASSWARD_BUTTON_ID).click()
    driver.implicitly_wait(50)
    driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH).send_keys(password)
    driver.implicitly_wait(50)
    driver.find_element_by_id(log_in_mapping.INPUT_PASSWORD_BUTTON_ID).click()
    driver.implicitly_wait(50)
    text = driver.find_element_by_xpath(log_in_mapping.ERROR_MESSAGE_FOR_EMAIL_XPATH).text
    assert msg, text
    text = driver.find_element_by_xpath(log_in_mapping.ERROR_MESSAGE_FOR_PASSWORD_XPATH).text
    assert msg, text
    return


def working_log_in(email, password):
    """it tests ideal case to log in with correct email and password 
    Parameters
    -----------
    email : str
        input email to be tested
    password : str
        input password to be tested
    """
    # driver.find_element_by_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys(email)
    # driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_BUTTON_ID).click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_id(log_in_mapping.CHOOSE_PASSWARD_BUTTON_ID).click()
   
    driver.implicitly_wait(50)
    driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH).send_keys(password)
    driver.implicitly_wait(50)
    driver.find_element_by_id(log_in_mapping.INPUT_PASSWORD_BUTTON_ID).click()
    return