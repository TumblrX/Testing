from appium import webdriver
from selenium.webdriver.common.by import By
from support import log_in_mapping
from unittest import TestCase
from support import desiredcapabilities


    
def invalid_email(email, msg):
    """it tests invalid emails 
    Parameters
    -----------
    email : str
        input email to be tested
    msg : str
        expected message that will appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities.desired_cap)
    driver.find_element_by_accessibility_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(10)
    driver.find_element_by_accessibility_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_EMAIL_XPATH)
    element.click()
    element.send_keys(email)
    driver.implicitly_wait(30)
    
    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    driver.find_element_by_xpath(log_in_mapping.LOGIN_BUTTON_XPATH).click()
    driver.implicitly_wait(30)
      
    text = driver.find_element_by_accessibility_id(log_in_mapping.ERROR_MESSAGE_FOR_EMAIL_ACC_ID).get_attribute('content-desc')
    
    # assert msg, text
    return text

def empty_email(email,password, msg):
    """it tests false passwards with a valid email 
    Parameters
    -----------
    password : str
        input password to be tested
    msg : str
        expected message that will appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities.desired_cap)

    driver.find_element_by_accessibility_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(10)
    driver.find_element_by_accessibility_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_EMAIL_XPATH)
    element.click()
    element.send_keys(email)
    driver.implicitly_wait(30)
    
    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH)
    element.click()
    element.send_keys(password)
    driver.implicitly_wait(30)

    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    driver.find_element_by_xpath(log_in_mapping.LOGIN_BUTTON_XPATH).click()
    driver.implicitly_wait(30)

    driver.find_element_by_xpath(log_in_mapping.EMAIL_XPATH_AFTER_ERROR).click()
    text = driver.find_element_by_accessibility_id(log_in_mapping.EMPTY_EMAIL_EROR_MSG_ACC_ID).get_attribute('content-desc')
    assert msg, text
    return text

def empty_password(email,password, msg):
    """it tests false passwards with a valid email 
    Parameters
    -----------
    password : str
        input password to be tested
    msg : str
        expected message that will appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities.desired_cap)
    driver.find_element_by_accessibility_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(10)
    driver.find_element_by_accessibility_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_EMAIL_XPATH)
    element.click()
    element.send_keys(email)
    driver.implicitly_wait(30)
    
    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH)
    element.click()
    element.send_keys(password)
    driver.implicitly_wait(30)

    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    driver.find_element_by_xpath(log_in_mapping.LOGIN_BUTTON_XPATH).click()
    driver.implicitly_wait(30)

    driver.find_element_by_xpath(log_in_mapping.EMAIL_XPATH_AFTER_ERROR).click()
    text = driver.find_element_by_accessibility_id(log_in_mapping.ERROR_MESSAGE_FOR_PASSWORD_ACC_ID).get_attribute('content-desc')
    assert msg, text
    return text

def wrong_email_or_pass(email,password, msg):
    """it tests false passwards with a valid email 
    Parameters
    -----------
    password : str
        input password to be tested
    msg : str
        expected message that will appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities.desired_cap)

    driver.find_element_by_accessibility_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(10)
    driver.find_element_by_accessibility_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_EMAIL_XPATH)
    element.click()
    element.send_keys(email)
    driver.implicitly_wait(30)
    
    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH)
    element.click()
    element.send_keys(password)
    driver.implicitly_wait(30)

    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    driver.find_element_by_xpath(log_in_mapping.LOGIN_BUTTON_XPATH).click()
    driver.implicitly_wait(30)

    driver.find_element_by_xpath(log_in_mapping.EMAIL_XPATH_AFTER_ERROR).click()
    text = driver.find_element_by_accessibility_id(log_in_mapping.WRONG_EMAIL_OR_PASS_ACC_ID).get_attribute('content-desc')
    assert msg, text
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
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities.desired_cap)
    driver.find_element_by_accessibility_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
    driver.implicitly_wait(10)
    driver.find_element_by_accessibility_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
    driver.implicitly_wait(50)
    
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_EMAIL_XPATH)
    element.click()
    element.send_keys(email)
    driver.implicitly_wait(50)
    
    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    element = driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH)
    element.click()
    element.send_keys(password)
    driver.implicitly_wait(30)

    driver.find_element_by_xpath(log_in_mapping.SCROLL_VIEW_XPATH).click()
    try:
        driver.find_element_by_xpath(log_in_mapping.LOGIN_BUTTON_XPATH).click()
    except:
        return "An exception occurred"

    driver.implicitly_wait(30)

    return True