from appium import webdriver
from unittest import TestCase
from support import searching_mapping, desiredcapabilities

driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)

def is_there_placeholder(email, msg):
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

def test_empty_search(password, msg):
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


def test_only_spaces(email, password):
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

def test_text_with_spaces_in(email, msg):
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

def unknowen_tag(password, msg):
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


def knowen_tag(email, password):
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