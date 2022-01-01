from appium import webdriver
from post_mapping import POST_VARIABLES

from desiredcapabilities import desiredcap
driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcap)


def login(email, password):
    
    driver.find_element_by_id(POST_VARIABLES.LOGIN_BUTTON).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(POST_VARIABLES.LOGIN_WITH_EMAIL_BUTTON).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(POST_VARIABLES.EMAIL_TEXT_ID).send_keys(email)
    driver.find_element_by_id(POST_VARIABLES.PASSWORD_TEXT_ID).send_keys(password)
    driver.implicitly_wait(50)    
    driver.find_element_by_id(POST_VARIABLES.SECOND_BUTTON_ID).click()
    driver.implicitly_wait(50)
    return True

def create_post(text):
    try:
    
        driver.find_element_by_id(POST_VARIABLES.ADD_POST_BUTTON).click()
        driver.find_element_by_xpath(POST_VARIABLES.POST_TEXT_XPATH).send_keys(text)
        driver.find_element_by_id(POST_VARIABLES.POST_BUTTON_ID).click()
        driver.find_element_by_xpath(POST_VARIABLES.HOME_BUTTON).click()
        driver.swipe(100,200,100,400,6000) 
        txt = driver.find_element_by_id(POST_VARIABLES.CHECK_CREATED_POST).text
        if (text == text):
            return True
        else: return False
    except:
        return False

