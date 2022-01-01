from appium import webdriver
from support.user_blog_mapping import USER_BLOG_VARIABLES
from support.desiredcapabilites import DESIRED_CAP
driver = webdriver.Remote("http://localhost:4723/wd/hub",DESIRED_CAP)


def navigate_to_user_blog():
    try:
       driver.find_element_by_accessibility_id(USER_BLOG_VARIABLES.USER_ICON_BUTTON_ACC_ID).click()
       return True
    except:
        return False

def edit_appearance_Header_image():
    try:
        driver.find_element_by_id(USER_BLOG_VARIABLES.CUSTOMIZE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.CAHNGE_HEADER_IMAGE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.CHOOSE_IMAGE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(USER_BLOG_VARIABLES.IMAGE_XPATH).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.CONFIRM_ACTION_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.SAVE_BUTTON_ID).click()

        return True
    except :
        return False

def edit_appearance_name(new_title):
    try:
        driver.find_element_by_id(USER_BLOG_VARIABLES.CUSTOMIZE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.TITLE_TEXTBOX_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.TITLE_TEXTBOX_ID).clear()
        driver.find_element_by_id(USER_BLOG_VARIABLES.TITLE_TEXTBOX_ID).send_keys(new_title)
        # confirm action
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.CONFIRM_ACTION_BUTTON_ID).click()
        # save 
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.SAVE_BUTTON_ID).click()
        return True
    except :
        return False

def change_name_color():
    try:
        driver.find_element_by_id(USER_BLOG_VARIABLES.CUSTOMIZE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.TITLE_TEXTBOX_ID).click()
    # change color 
        driver.find_element_by_id(USER_BLOG_VARIABLES.CHANGE_COLOR_BUTTON_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.COLOR_BUTTON_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.COLOR_LEVEL_BUTTON_ID).click()
        # confirm action
        driver.find_element_by_id(USER_BLOG_VARIABLES.CONFIRM_ACTION_BUTTON_ID).click()
        # save 
        driver.find_element_by_id(USER_BLOG_VARIABLES.SAVE_BUTTON_ID).click()
        return True
    except:
        return False


def change_background():
    try:
        driver.find_element_by_id(USER_BLOG_VARIABLES.CUSTOMIZE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.BACKGROUND_BUTTON_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.COLOR_BUTTON_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.COLOR_LEVELB_BUTTON_ID).click()
        # confirm action
        driver.find_element_by_id(USER_BLOG_VARIABLES.CONFIRM_ACTION_BUTTON_ID).click()
        # save 
        driver.find_element_by_id(USER_BLOG_VARIABLES.SAVE_BUTTON_ID).click()
        return True
    except:
        return False
def change_accent():
    try:
        driver.find_element_by_id(USER_BLOG_VARIABLES.CUSTOMIZE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.ACCENT_BUTTON_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.COLOR_ACCENT_BUTTON_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.COLOR_LEVELA_BUTTON_ID).click()
        # confirm action
        driver.find_element_by_id(USER_BLOG_VARIABLES.CONFIRM_ACTION_BUTTON_ID).click()
        # save 
        driver.find_element_by_id(USER_BLOG_VARIABLES.SAVE_BUTTON_ID).click()
        return True
    except:
        return False

def change_description(text):
    try:
        driver.find_element_by_id(USER_BLOG_VARIABLES.CUSTOMIZE_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.DESCRIP_BUTTON_ID).click()
        driver.find_element_by_id(USER_BLOG_VARIABLES.DESCRIP_BUTTON_ID).clear()
        driver.find_element_by_id(USER_BLOG_VARIABLES.DESCRIP_BUTTON_ID).send_keys(text)
        # confirm action
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.CONFIRM_ACTION_BUTTON_ID).click()
        # save 
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.SAVE_BUTTON_ID).click()
        return True
    except :
        return False

def change_avatar(option1,option2):
    try:
        driver.find_element_by_id(USER_BLOG_VARIABLES.AVATAR_BUTTON_ID).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(USER_BLOG_VARIABLES.CHANGE_AVATAR_XPATH).click()
        # option1 if set to true means to change shape to square
        if option1 != "":
            driver.find_element_by_id(USER_BLOG_VARIABLES.SQUARE_SHAPE_ID).click()
        elif option2 != "":
            driver.find_element_by_id(USER_BLOG_VARIABLES.CIRCLE_SHAPE_ID).click()
        else :
            driver.find_element_by_id(USER_BLOG_VARIABLES.CHOOSE_AVATAR_IMAGE_ID).click()
        # confirm action
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.CONFIRM_ACTION_BUTTON_ID).click()
        # save 
        driver.implicitly_wait(10)
        driver.find_element_by_id(USER_BLOG_VARIABLES.SAVE_BUTTON_ID).click()
        return True
    except :
        return False

def following_settings():
    try:
        driver.find_element_by_accessibility_id(USER_BLOG_VARIABLES.FOLLOWING_BUTTON).click()
        # change following settings from the user blog page 
        driver.find_element_by_id(USER_BLOG_VARIABLES.FOLLOWING_CHANGE_BUTTON_ID).click()
        # toggle liks button
        driver.find_element_by_xpath(USER_BLOG_VARIABLES.LIKES_BUTTON_XPATH).click()
        # toggle following button
        driver.find_element_by_xpath(USER_BLOG_VARIABLES.FOLLOWING_BUTTON_XPATH).click()
        # navigate up (back)
        driver.find_element_by_accessibility_id(USER_BLOG_VARIABLES.BACK_BUTTON_ACC_ID).click()
        driver.implicitly_wait(30)
        return True
    except:
        return False

def preview_user_blog_as_guest():
    try:
        driver.find_element_by_accessibility_id(USER_BLOG_VARIABLES.FOLLOWING_BUTTON).click()
        # change following settings from the user blog page 
        driver.find_element_by_id(USER_BLOG_VARIABLES.FOLLOWING_CHANGE_BUTTON_ID).click()
        driver.implicitly_wait(20)
        driver.find_element_by_id(USER_BLOG_VARIABLES.PRIVIEW_BUTTON_ID).click()
        # check button follow exists.
        driver.find_element_by_id(USER_BLOG_VARIABLES.FOLLOW_BUTTON_ID).click()
        # check send message button.
        driver.find_element_by_id(USER_BLOG_VARIABLES.SEND_MESSAGE_ID).click()
        return True
    except:
        return False


# navigate_to_user_blog()
# print(edit_appearance_Header_image())
# edit_appearance_name("MENNA")
# change_name_color()
# change_background()
# change_accent()
# change_description("BUTTERFLIES IMPACT NEVER LOST!!")
# change_avatar("yes","")
# following_settings()
# preview_user_blog_as_guest()