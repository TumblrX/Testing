from appium import webdriver
from support.dashboard_mapping import DASHBOARD_VARIABLES
from support.desiredcapabilites import DESIRED_CAP

driver = webdriver.Remote("http://localhost:4723/wd/hub",DESIRED_CAP)


def navigate_to_dashboard():
    driver.find_element_by_id(DASHBOARD_VARIABLES.DASHBOARD_BUTTON_ID).click()

def swipe_to_top ():
    navigate_to_dashboard()
    count = 3
    while count > 0:
      print(count)
      driver.swipe(150,200,150,800,9000)
      count = count - 1

## this function is search for post with specific text , added seperatly as I need ot to return false incase of error not to terminate.
def find_specific_text():
    try:
        txt = driver.find_element_by_id(DASHBOARD_VARIABLES.BLOG_TEXT_ID).text
        return True , txt
    except:
        return False , ""

def add_like(text):

        navigate_to_dashboard()
        txt = " "
        count = 0
        while text != txt:
            count = count +1
            driver.swipe(150,470,150,200,2000)
            state,txt = find_specific_text()
            print(text,txt,state)
        count1 = 2
        while count1 != 0:
            print(count1)
            driver.swipe(150,470,150,200,2000)
            count1 = count1 - 1
        driver.find_element_by_id(DASHBOARD_VARIABLES.LIKE_BUTTON_ID).click()
        # act as a refresher
        navigate_to_dashboard()


def add_comment(text,comment):

        navigate_to_dashboard()
        count = 0
        txt =" "
        while text != txt:
            print(count)
            state,txt = find_specific_text()
            driver.swipe(150,470,150,200,2000)
            count = count + 1
            print(text,txt)
        count = 1
        while count != 0:
            print(count)
            driver.swipe(150,470,150,200,2000)
            count = count - 1
        driver.find_element_by_id(DASHBOARD_VARIABLES.COMMENT_BUTTON_ID).click()
        driver.implicitly_wait(50)
        driver.find_element_by_id(DASHBOARD_VARIABLES.REPLY_MESSAGE_ID).send_keys(comment)
        driver.find_element_by_id(DASHBOARD_VARIABLES.REPLY_BUTTON_ID).click()

def create_post(text):

       navigate_to_dashboard()
       driver.find_element_by_id(DASHBOARD_VARIABLES.COMPOSE_POST_BUTTON_ID).click()
       driver.implicitly_wait(20)

       driver.find_element_by_xpath(DASHBOARD_VARIABLES.POST_TEXTBOX_XPATH).send_keys(text)
       driver.find_element_by_id(DASHBOARD_VARIABLES.POST_BUTTON_ID).click()
       count = 1
       while count >= 0:
        print(count)
        driver.swipe(150,200,150,800,6000)
        count = count -1
def delete_post(text):
    try :
        navigate_to_dashboard()
        txt = " "
        end = False
        print(end)
        while (text != txt):
            state , txt = find_specific_text()
            driver.swipe(150,1000,150,200,6000)
            print(end,text,txt)
        if text == txt:
            count = 1
            while count >= 0:
                driver.swipe(150,200,150,600,6000)
                count = count -1 
            driver.find_element_by_id(DASHBOARD_VARIABLES.DELETE_BUTTON_ID).click()
            driver.find_element_by_id(DASHBOARD_VARIABLES.CONFIRM_DELETE_POST_BUTTON).click()
        # just to change the page and return back to posts inorder to swipe without throwing error
        navigate_to_dashboard()
        # act as a refresh
        count = 1
        while count >= 0:
            driver.swipe(150,200,150,400,6000)
            count = count -1 
        return True
    except:
        return False

def reblog_post(text,text2):
    try :
        navigate_to_dashboard()
        count = 0
        txt =" "
        while text != txt:
            print(count)
            state,txt =find_specific_text()
            driver.swipe(150,470,150,200,2000)
            count = count + 1
            print(text,txt)
        count = 1
        while count != 0:
            print(count)
            driver.swipe(150,470,150,200,2000)
            count = count - 1

        driver.find_element_by_id(DASHBOARD_VARIABLES.REBLOG_BUTTON_ID).click()
        driver.implicitly_wait(50)
        driver.find_element_by_id(DASHBOARD_VARIABLES.REBLOG_ACTION_BUTTON_ID).click()
        return True 
    except :
        return False
def send_post(text):
    try :
        navigate_to_dashboard()
        count = 0
        txt =" "
        while text != txt:
            print(count)
            state , txt = find_specific_text()
            driver.swipe(150,470,150,200,2000)
            count = count + 1
            print(text,txt)
        count = 1
        while count != 0:
            print(count)
            driver.swipe(150,470,150,200,2000)
            count = count - 1

        driver.find_element_by_id(DASHBOARD_VARIABLES.SEND_AS_MESSAGE_ID).click()
        driver.implicitly_wait(50)
        driver.find_element_by_id(DASHBOARD_VARIABLES.SHAREING_MESSAGE_IN_ID).send_keys("this post is shared by a text script")
        driver.find_element_by_xpath(DASHBOARD_VARIABLES.FIRST_BLOG_NAME_XPATH).click()
        driver.find_element_by_id(DASHBOARD_VARIABLES.SHAREING_SEND_BUTTON_ID).click()
        return True 
    except:
        return False
def upload_image_post():
    
       navigate_to_dashboard()
       driver.find_element_by_id(DASHBOARD_VARIABLES.COMPOSE_POST_BUTTON_ID).click()
       driver.implicitly_wait(20)

       driver.find_element_by_id(DASHBOARD_VARIABLES.ADD_IMAGE_BUTTON_ID).click()
       driver.find_element_by_xpath(DASHBOARD_VARIABLES.IMAGE_XPATH).click()
       driver.find_element_by_id(DASHBOARD_VARIABLES.NEXT_BUTTON_ID).click()
       driver.find_element_by_id(DASHBOARD_VARIABLES.POST_BUTTON_ID).click()
