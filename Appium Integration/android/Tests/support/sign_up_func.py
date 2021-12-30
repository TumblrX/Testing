from appium import webdriver
from selenium.webdriver.common.by import By
from support import sign_up_mapping
from unittest import TestCase
from support import desiredcapabilities

def invalid_email(email):
    """it tests invalid emails 
    Parameters
    -----------
    email : str
        input email to be tested
    Return
    -----------
    msg : str
        the error message that appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(sign_up_mapping.FIRST_SIGN_UP_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.SIGN_UP_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.INPUT_EMAIL_ID).send_keys(email)
    driver.find_element_by_id(sign_up_mapping.INPUT_PASSWORD_ID).send_keys("123456789")
    driver.find_element_by_id(sign_up_mapping.INPUT_USER_NAME_ID).send_keys("blablaa")
    driver.find_element_by_id(sign_up_mapping.INPUT_AGE_ID).send_keys("20")
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.DONE_BUTTON_ID).click()
    driver.implicitly_wait(50)
    text = driver.find_element_by_id(sign_up_mapping.ERROR_WRONG_MESSAGE_ID).text
    return text

def invalid_password(password):
    """it tests false passwords with a valid email 
    Parameters
    -----------
    password : str
        input password to be tested
    Return
    -----------
    msg : str
        the error message that appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(sign_up_mapping.FIRST_SIGN_UP_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.SIGN_UP_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.INPUT_EMAIL_ID).send_keys("nada@test.com")
    driver.find_element_by_id(sign_up_mapping.INPUT_PASSWORD_ID).send_keys(password)
    driver.find_element_by_id(sign_up_mapping.INPUT_USER_NAME_ID).send_keys("blablaa")
    driver.find_element_by_id(sign_up_mapping.INPUT_AGE_ID).send_keys("20")
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.DONE_BUTTON_ID).click()
    driver.implicitly_wait(50)
    text = driver.find_element_by_id(sign_up_mapping.ERROR_WRONG_MESSAGE_ID).text
    return text


def invalid_blog_name(blog_name):
    """it tests ideal case to log in with correct email and password 
    Parameters
    -----------
    email : str
        input blog_name to be tested
    Return
    -----------
    msg : str
        the error message that appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(sign_up_mapping.FIRST_SIGN_UP_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.SIGN_UP_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.INPUT_EMAIL_ID).send_keys("nada@test.com")
    driver.find_element_by_id(sign_up_mapping.INPUT_PASSWORD_ID).send_keys("123456789")
    driver.find_element_by_id(sign_up_mapping.INPUT_USER_NAME_ID).send_keys(blog_name)
    driver.find_element_by_id(sign_up_mapping.INPUT_AGE_ID).send_keys("20")
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.DONE_BUTTON_ID).click()
    driver.implicitly_wait(50)
    text = driver.find_element_by_id(sign_up_mapping.ERROR_WRONG_MESSAGE_ID).text
    return text

def invalid_age(age):
    """it tests ideal case to log in with correct email and password 
    Parameters
    -----------
    email : str
        input email to be tested
    Return
    -----------
    msg : str
        the error message that appear
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(sign_up_mapping.FIRST_SIGN_UP_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.SIGN_UP_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.INPUT_EMAIL_ID).send_keys("nada@test.com")
    driver.find_element_by_id(sign_up_mapping.INPUT_PASSWORD_ID).send_keys("123456789")
    driver.find_element_by_id(sign_up_mapping.INPUT_USER_NAME_ID).send_keys("blablaa")
    driver.find_element_by_id(sign_up_mapping.INPUT_AGE_ID).send_keys(age)
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.DONE_BUTTON_ID).click()
    driver.implicitly_wait(50)
    text = driver.find_element_by_id(sign_up_mapping.ERROR_WRONG_MESSAGE_ID).text
    return text

def working_sign_up(email, password, blogname, age):
    """it tests ideal case to sign up with correct email and password 
    Parameters
    -----------
    email : str
        input email to be tested
    password : str
        input password to be tested
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
    driver.find_element_by_id(sign_up_mapping.FIRST_SIGN_UP_BUTTON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.SIGN_UP_WITH_EMAIL_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.INPUT_EMAIL_ID).send_keys(email)
    driver.find_element_by_id(sign_up_mapping.INPUT_PASSWORD_ID).send_keys(password)
    driver.find_element_by_id(sign_up_mapping.INPUT_USER_NAME_ID).send_keys(blogname)
    driver.find_element_by_id(sign_up_mapping.INPUT_AGE_ID).send_keys(age)
    driver.implicitly_wait(30)
    driver.find_element_by_id(sign_up_mapping.DONE_BUTTON_ID).click()
    return True