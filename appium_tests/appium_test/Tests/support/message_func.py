from appium import webdriver
from unittest import TestCase
from support import message_mapping, desiredcapabilities

driver = webdriver.Remote("http://localhost:4723/wd/hub",desiredcapabilities.desiredcap)

def test_search_for_new_chat(friend_name, msg):
    """it searching for new chats"""
    driver.find_element_by_id(message_mapping.HOME_MESSAGE_ICON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(message_mapping.NEW_MESSAGE_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(message_mapping.SEARCH_FOR_NEW_FRIND_ID).send_keys(friend_name)
    driver.implicitly_wait(50)
    driver.find_element_by_xpath(message_mapping.MY_NEW_FRIEND_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(message_mapping.SAY_SOMETHING_ID).send_keys(msg)
    driver.implicitly_wait(30)
    driver.find_element_by_id(message_mapping.SEND_BUTTON_ID).click()
    driver.implicitly_wait(30)
    text = driver.find_element_by_id(message_mapping.LAST_MESSAGE_ID).text
    assert text, msg
    driver.find_element_by_accessibility_id(message_mapping.BACK_BUTTON_ACCESSE_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_accessibility_id(message_mapping.BACK_BUTTON_ACCESSE_ID).click()
    return True

def access_first_chat():
    """it access first chat in my chats"""
    driver.find_element_by_id(message_mapping.HOME_MESSAGE_ICON_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(message_mapping.A_FRIEND_XPATH).click()
    return True

def test_send_photo(type):
    """it sends photos"""
    assert(access_first_chat(), True)
    driver.find_element_by_id(message_mapping.CAMERA_ID).click()
    driver.implicitly_wait(30)
    if(type == "camera"):
        driver.find_element_by_id(message_mapping.PHOTO_FROM_CAMERA_ID).click()
        driver.implicitly_wait(30)
        driver.find_element_by_id(message_mapping.TAKE_PHOTO_BUTTON_ID).click()
        driver.implicitly_wait(30)
        driver.find_element_by_id(message_mapping.SEND_TAKED_PHOTO_BUTTON_ID).click()
    else:
        driver.find_element_by_xpath(message_mapping.PHOTO_FROM_GALLERY_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(message_mapping.SEND_BUTTON_ID).click()
    driver.implicitly_wait(50)
    driver.find_element_by_id(message_mapping.NEW_MESSAGE_IMAGE_ID)
    driver.implicitly_wait(30)
    driver.find_element_by_accessibility_id(message_mapping.BACK_BUTTON_ACCESSE_ID).click()
    return True

def test_send_GIF(type):
    """it sends gif"""
    assert(access_first_chat(), True)
    driver.find_element_by_id(message_mapping.GIF_ID).click()
    driver.implicitly_wait(30)
    if(type == "top"):
        driver.find_element_by_accessibility_id(message_mapping.TOP_ACCESSE_ID).click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath(message_mapping.CHOOSE_GIF_TOP_XPATH).click()
    else:
        driver.find_element_by_accessibility_id(message_mapping.RECENT_ACCESSE_ID).click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath(message_mapping.CHOOSE_GIF_RECENT_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(message_mapping.SEND_BUTTON_ID).click()
    driver.implicitly_wait(50)
    driver.find_element_by_id(message_mapping.NEW_MESSAGE_GIF_ID)
    driver.implicitly_wait(30)
    driver.find_element_by_accessibility_id(message_mapping.BACK_BUTTON_ACCESSE_ID).click()
    return True

def find_chat_with_name(name):
    """it find spacific chat with name"""
    found = False
    driver.find_element_by_id(message_mapping.HOME_MESSAGE_ICON_ID).click()
    driver.implicitly_wait(30)
    i = 0
    while True:
        i = i + 1
        map_var = message_mapping.A_FRIEND_XPATH + "[" + str(i) + "]" + "/android.widget.TextView[1]"
        try:
            text = driver.find_element_by_xpath(map_var).text
            if(text == name):
                found = True
                break
            continue
        except:
            break
    return found, map_var

def delete_conversation(name):
    boolean, map_var = find_chat_with_name(name)
    driver.find_element_by_xpath(map_var).click()
    driver.implicitly_wait(30)
    driver.find_element_by_accessibility_id(message_mapping.MORE_OPTIONS_ACCESSE_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(message_mapping.DELETE_CONVE_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_id(message_mapping.DELETE_BUTTON_TO_CONFIRM_ID).click()
    driver.implicitly_wait(30)
    boolean1, map_var1 = find_chat_with_name(name)
    return boolean1


