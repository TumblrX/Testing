from appium import webdriver
from support.settings_mapping import settings_var
from support.desiredcapabilites import DESIRED_CAP
driver = webdriver.Remote("http://localhost:4723/wd/hub",DESIRED_CAP)


def navigate_to_settings():
    try:
       driver.find_element_by_id(settings_var.ACCOUNT_ICON).click()
       driver.find_element_by_id(settings_var.ACTION_BLOG_ICON).click() 
       driver.find_element_by_xpath(settings_var.ACCOUNT_SETTINGS_XPATH).click()
       return True
    except:
        return False

def change_email(new_email,password):
    driver.implicitly_wait(30)
    try:
        driver.find_element_by_id(settings_var.CHANGE_EMAIL_BUTTON_ID).click()
        driver.find_element_by_id(settings_var.NEW_EMAIL_TEXTBOX_ID).send_keys(new_email)
        driver.find_element_by_id(settings_var.SAVE_CHANGE_BUTTON_ID).click()
        # Confirm password for email change 
        driver.find_element_by_id(settings_var.CONFIRM_PASSWORD_FOR_EMAIL_CHANGE_ID).send_keys(password)
        driver.find_element_by_id(settings_var.CONFIRM_BUTTON_ID).click()
        driver.implicitly_wait(30)
        # then log out and check log in with the new email
        # driver.find_element_by_id(settings_var.LOG_OUT_BUTTON_ID).click()
        # log_in_func.working_log_in(new_email,password)
        return True
    except:
        return False

def change_password_with_old(new_password,old_password,msg):
    driver.implicitly_wait(20)
    driver.find_element_by_id(settings_var.CHANGE_PASSWORD_BUTTON_ID).click()
    driver.find_element_by_id(settings_var.CHANGE_PASSWORD_TEXTBOX_ID).send_keys(new_password)
    driver.find_element_by_id(settings_var.SAVE_CHANGE_BUTTON_ID).click()
    # Confirm old password for password change 
    driver.implicitly_wait(20)
    driver.find_element_by_id(settings_var.CONFIRM_PASSWORD_FOR_EMAIL_CHANGE_ID).send_keys(old_password)
    driver.find_element_by_id(settings_var.CONFIRM_BUTTON_ID).click()
    text = driver.find_element_by_id(settings_var.ERROR_MESSAGE_ID).text
    assert text , msg
    return text

def change_password_weak(new_password,old_password,msg):
    driver.implicitly_wait(20)
    driver.find_element_by_id(settings_var.CANCEL_BUTTON).click()
    driver.find_element_by_id(settings_var.CHANGE_PASSWORD_BUTTON_ID).click()
    driver.find_element_by_id(settings_var.CHANGE_PASSWORD_TEXTBOX_ID).send_keys(new_password)
    driver.find_element_by_id(settings_var.SAVE_CHANGE_BUTTON_ID).click()
    # Confirm old password for password change 
    driver.implicitly_wait(20)
    driver.find_element_by_id(settings_var.CONFIRM_PASSWORD_FOR_EMAIL_CHANGE_ID).send_keys(old_password)
    driver.find_element_by_id(settings_var.CONFIRM_BUTTON_ID).click()
    text = driver.find_element_by_id(settings_var.ERROR_MESSAGE_ID).text
    assert text , msg

    return text

def change_password_working(email,new_password,old_password):
    driver.implicitly_wait(20)
    try:
        driver.find_element_by_id(settings_var.CANCEL_BUTTON).click()
        driver.find_element_by_id(settings_var.CHANGE_PASSWORD_BUTTON_ID).click()
        driver.find_element_by_id(settings_var.CHANGE_PASSWORD_TEXTBOX_ID).send_keys(new_password)
        driver.find_element_by_id(settings_var.SAVE_CHANGE_BUTTON_ID).click()
        # Confirm old password for password change 
        driver.implicitly_wait(20)
        driver.find_element_by_id(settings_var.CONFIRM_PASSWORD_FOR_EMAIL_CHANGE_ID).send_keys(old_password)
        driver.find_element_by_id(settings_var.CONFIRM_BUTTON_ID).click()
        # then log out and check log in with the new email
        # driver.find_element_by_id(settings_var.LOG_OUT_BUTTON_ID).click()
        # log_in_func.working_log_in(email,new_password)
        return True
    except:
        return False

def change_messaging_settings(option): # toggle whatever it was
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(settings_var.MESSAGEING_CHANGE_SETTING_XPATH).click()
    driver.implicitly_wait(20)
    driver.find_element_by_id(settings_var.CURRENT_STATE_ID).click()
    #toggle
    if option == "everyone":
        driver.find_element_by_xpath(settings_var.EVERY_ONE_OPTION_XPATH).click()
        state =driver.find_element_by_xpath(settings_var.EVERY_ONE_OPTION_XPATH).is_enabled()
        assert state ,True
    else:
        driver.find_element_by_xpath(settings_var.ONLY_TUMBLRS_OPTION_XPATH).click()
        state =driver.find_element_by_xpath(settings_var.ONLY_TUMBLRS_OPTION_XPATH).is_enabled()
        assert state ,True

    return state

# navigate_to_settings()
# change_email("mennaahmedali77@gmail.com","211257menna")
# change_password_with_old("211257menna","211257menna","Sorry, you've used that password before. You must choose a new password.")
# change_password_weak("2112","211257menna","The password must be at least 8 characters.")
# change_password_working("mennaahmedali77@gmail.com","211257mennamenna","211257menna")
# change_messaging_settings("onlytumblrs")