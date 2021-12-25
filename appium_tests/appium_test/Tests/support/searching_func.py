from appium import webdriver
from unittest import TestCase
from support import searching_mapping, desiredcapabilities


driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)
def is_there_placeholder():
    """it tests placeholder existance 
    Parameters
    -----------
    placeholder : str
        expected placeholder that will appear
    """
    driver.find_element_by_id(searching_mapping.HOME_SEARCH_ICON_ID).click()
    driver.implicitly_wait(30)
    text = driver.find_element_by_xpath(searching_mapping.SERCH_BAR_TEXT_XPATH).text
    # assert placeholder, text
    return text

def test_empty_search():
    """it tests empty searching """
    driver.find_element_by_id(searching_mapping.HOME_SEARCH_ICON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(searching_mapping.SERCH_BAR_TEXT_XPATH).click()
    driver.implicitly_wait(30)
    recent = driver.find_element_by_xpath(searching_mapping.RECENT_TAGS_XPATH).text
    driver.implicitly_wait(30)
    recommended = driver.find_element_by_xpath(searching_mapping.RECOMMENDED_TAGS_XPATH).text
    return [recent, recommended]


def test_only_spaces():
    """it tests empty searching """
    driver.find_element_by_id(searching_mapping.HOME_SEARCH_ICON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(searching_mapping.SEARCH_BAR_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(searching_mapping.SEARCHABLE_BAR_ID).send_keys(" ")
    driver.implicitly_wait(30)
    recent = driver.find_element_by_xpath(searching_mapping.RECENT_TAGS_XPATH).text
    driver.implicitly_wait(30)
    recommended = driver.find_element_by_xpath(searching_mapping.RECOMMENDED_TAGS_XPATH).text
    return [recent, recommended]
    
# def test_text_with_spaces_in(email, msg):
#     """it tests invalid emails 
#     Parameters
#     -----------
#     email : str
#         input email to be tested
#     msg : str
#         expected message that will appear
#     """
#     driver.find_element_by_xpath(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
#     driver.implicitly_wait(30)
#     driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
#     driver.implicitly_wait(30)
#     driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys(email)
#     driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_BUTTON_ID).click()
#     driver.implicitly_wait(30)
#     text = driver.find_element_by_id(log_in_mapping.ERROR_MESSAGE_FOR_EMAIL_ID).text 
#     assert msg, text
#     return 

# def unknowen_tag(password, msg):
#     """it tests false passwards with a valid email 
#     Parameters
#     -----------
#     password : str
#         input password to be tested
#     msg : str
#         expected message that will appear
#     """
#     # driver.find_element_by_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
#     # driver.implicitly_wait(30)
#     # driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
#     # driver.implicitly_wait(30)
#     driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys("nadaelsayed163@gmail.com")
#     driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_BUTTON_ID).click()
#     driver.implicitly_wait(30)
#     driver.find_element_by_id(log_in_mapping.CHOOSE_PASSWARD_BUTTON_ID).click()
#     driver.implicitly_wait(50)
#     driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH).send_keys(password)
#     driver.implicitly_wait(50)
#     driver.find_element_by_id(log_in_mapping.INPUT_PASSWORD_BUTTON_ID).click()
#     driver.implicitly_wait(50)
#     text = driver.find_element_by_xpath(log_in_mapping.ERROR_MESSAGE_FOR_EMAIL_XPATH).text
#     assert msg, text
#     text = driver.find_element_by_xpath(log_in_mapping.ERROR_MESSAGE_FOR_PASSWORD_XPATH).text
#     assert msg, text
#     return


# def knowen_tag(email, password):
#     """it tests ideal case to log in with correct email and password 
#     Parameters
#     -----------
#     email : str
#         input email to be tested
#     password : str
#         input password to be tested
#     """
#     # driver.find_element_by_id(log_in_mapping.FIRST_LOG_IN_BUTTON_ID).click()
#     # driver.implicitly_wait(30)
#     # driver.find_element_by_id(log_in_mapping.LOG_IN_WITH_EMAIL_ID).click()
#     # driver.implicitly_wait(30)
#     # driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_ID).send_keys(email)
#     # driver.find_element_by_id(log_in_mapping.INPUT_EMAIL_BUTTON_ID).click()
#     # driver.implicitly_wait(30)
#     # driver.find_element_by_id(log_in_mapping.CHOOSE_PASSWARD_BUTTON_ID).click()
   
#     driver.implicitly_wait(50)
#     driver.find_element_by_xpath(log_in_mapping.INPUT_PASSWORD_XPATH).send_keys(password)
#     driver.implicitly_wait(50)
#     driver.find_element_by_id(log_in_mapping.INPUT_PASSWORD_BUTTON_ID).click()
#     return