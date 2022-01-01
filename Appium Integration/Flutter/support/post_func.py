from appium import webdriver
from post_mapping import POST_VARIABLES

from desiredcapabilities import DESIRED_CAP
driver = webdriver.Remote("http://localhost:4723/wd/hub",DESIRED_CAP)

def login(email, password):
    
    driver.find_element_by_xpath(POST_VARIABLES.LOGIN_BUTTON_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(POST_VARIABLES.LOGIN_WITH_EMAIL_XPATH).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(POST_VARIABLES.EMAIL_INPUT_XPATH).send_keys(email)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(POST_VARIABLES.PASSWORD_INPUT_XPATH).send_keys(password)
    driver.implicitly_wait(50)    
    driver.find_element_by_xpath(POST_VARIABLES.LOGIN_FINAL_BUTTON_XPATH).click()
    driver.implicitly_wait(50)
    return True

def navigate_to_posts():
    # try:
    driver.implicitly_wait(50)
    driver.find_element_by_xpath(POST_VARIABLES.ACCOUNT_ICON_XPATH).click()
    #driver.find_element_by_accessibility_id(POST_VARIABLES.ACCOUNT_ICON_ACC_ID).click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(POST_VARIABLES.POST_ICON_XPATH).click()
    #    return True
    # except:
    #     return False

def search_blog(tag,text):
    # go to home the back to search just to reload posts page 
    driver.find_element_by_id(POST_VARIABLES.DASHBOARD_ICON_ID).click()
    navigate_to_posts()
    driver.find_element_by_id(POST_VARIABLES.SEARCH_BLOG_ID).click()
    driver.implicitly_wait(30)
    if tag != " ":
        driver.find_element_by_id(POST_VARIABLES.TEXT_SEARCH_ID).send_keys(tag)
    else :
        driver.find_element_by_id(POST_VARIABLES.TEXT_SEARCH_ID).send_keys(text)
    driver.find_element_by_id(POST_VARIABLES.VIEW_RESULTS_SECTION_ID).click()
    try:
        txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID).text
        return True
    except :
        return False
    

def delete_post_by_search (text):
    driver.implicitly_wait(30)
    search_blog(" ",text)
    try:
        txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID).text
        if text == txt :
            driver.find_element_by_id (POST_VARIABLES.DELETE_POST_ID).click()
            driver.find_element_by_id(POST_VARIABLES.CONFIRM_DELETION_BUTTON_ID).click()
        return True
    except:
        return False
        

# function to edit the post if it has big text and small one
def edit_tag(text,new_text):
    try:
        count = 0
        txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID).text
        while text != txt:
            txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID).text
            driver.swipe(150,800,150,200,2000)
            count = count + 1
        driver.find_element_by_xpath(POST_VARIABLES.EDIT_POST_XPATH).click()
        driver.implicitly_wait(50)
        driver.find_element_by_xpath(POST_VARIABLES.POST_EDIT_TEXTBOX_XPATH).clear()
        driver.find_element_by_xpath(POST_VARIABLES.POST_EDIT_TEXTBOX_XPATH).send_keys(new_text)
        driver.find_element_by_id(POST_VARIABLES.POST_BUTTON_ID).click()
        navigate_to_posts()
        while count >= 0:
            print(count)
            driver.swipe(150,200,150,800,6000)
            count = count -1 
        tag= " "
        while text != tag:
            print(tag)
            tag = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID).text
            driver.swipe(150,800,150,200,2000)
        return True
    except:
        return False
    

 

# edit post if it has text only
def edit_post(text,new_text):
    try:
        count = 0
        driver.swipe(150,400,150,200,2000)
        txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID).text
        while text != txt:
            txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID).text
            driver.swipe(150,800,150,200,2000)
            count = count + 1
        driver.find_element_by_id(POST_VARIABLES.EDIT_POST_BUTTON_ID).click()
        driver.implicitly_wait(50)
        driver.find_element_by_id(POST_VARIABLES.POST_TEXT_TEXTBOX_ID).clear()
        driver.find_element_by_id(POST_VARIABLES.POST_TEXT_TEXTBOX_ID).send_keys(new_text)
        driver.find_element_by_id(POST_VARIABLES.POST_BUTTON_ID).click()
        navigate_to_posts()
        while count >= 0:
            print(count)
            driver.swipe(150,200,150,800,6000)
            count = count -1 
        return True
    except:
        return False

def loading_progress():
    try:
        driver.find_element_by_id(POST_VARIABLES.LOADING_PAGE_LINE_ID)
        return True
    except:
        return False

# delete post given its text - done #
def delete_post(text):
    try :
        navigate_to_posts()
        txt = " "
        end = False
        print(end)
        while (text != txt) and (not end):
            txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
            end = loading_progress()
            driver.swipe(150,1000,150,200,6000)
            print(end,text,txt)
        if text == txt:
            count = 1
            while count >= 0:
                driver.swipe(150,200,150,600,6000)
                count = count -1 
            driver.find_element_by_id(POST_VARIABLES.DELETE_BUTTON_ID).click()
            driver.find_element_by_id(POST_VARIABLES.CONFIRM_DELETE_POST_BUTTON).click()
        # just to change the page and return back to posts inorder to swipe without throwing error
        navigate_to_posts()
        # act as a refresh
        count = 1
        while count >= 0:
            driver.swipe(150,200,150,400,6000)
            count = count -1 
        return True
    except:
        return False

# add like to post given headline text in it - done #
def add_like_post(text):
    try :
        driver.swipe(150,400,150,200,2000)
        txt = driver.find_element_by_xpath(POST_VARIABLES.TEXT_SEARCH_XPATH).text
        count = 0
        while text != txt:
            count = count +1
            driver.swipe(150,800,150,200,6000)
            txt = driver.find_element_by_id(POST_VARIABLES.TEXT_SEARCH_XPATH).text
            print(text,txt)
        count1 = 2
        while count1 != 0:
            print(count1)
            driver.swipe(150,400,150,200,6000)
            count1 = count1 - 1
        driver.find_element_by_id(POST_VARIABLES.LIKE_BUTTON_ID).click()
        # act as a refresh
        # navigate_to_posts()
        while count >= 0:
            driver.swipe(150,200,150,800,6000)
            count = count -1 
        return True
    except:
        return False

# add comment to post given headline text in it - done #
def add_comment_post(text,comment):
    try :
        navigate_to_posts()
        count = 0
        txt =" "
        while text != txt:
            print(count)
            txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
            driver.swipe(150,400,150,200,6000)
            count = count + 1
            print(text,txt)
        count = 1
        while count != 0:
            print(count)
            driver.swipe(150,400,150,200,6000)
            count = count - 1
        driver.find_element_by_id(POST_VARIABLES.COMMENT_BUTTON_ID).click()
        driver.implicitly_wait(50)
        driver.find_element_by_id(POST_VARIABLES.REPLY_MESSAGE_ID).send_keys(comment)
        driver.find_element_by_id(POST_VARIABLES.REPLY_BUTTON_ID).click()
        return True
    except :
        return False

# send post as a message given headline text in it - done #
def send_post(text):
    try :
        navigate_to_posts()
        count = 0
        txt =" "
        while text != txt:
            print(count)
            txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
            driver.swipe(150,400,150,200,6000)
            count = count + 1
            print(text,txt)
        count = 1
        while count != 0:
            print(count)
            driver.swipe(150,400,150,200,6000)
            count = count - 1

        driver.find_element_by_id(POST_VARIABLES.SEND_AS_MESSAGE_ID).click()
        driver.implicitly_wait(50)
        driver.find_element_by_id(POST_VARIABLES.SHAREING_MESSAGE_IN_ID).send_keys("this post is shared by a text script")
        driver.find_element_by_xpath(POST_VARIABLES.FIRST_BLOG_NAME_XPATH).click()
        driver.find_element_by_id(POST_VARIABLES.SHAREING_SEND_BUTTON_ID).click()
        return True 
    except:
        return False
    
# reblog a post given headline text in it - done #
def reblog_post(text,text2):
    try :
        navigate_to_posts()
        count = 0
        txt =" "
        while text != txt:
            print(count)
            txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
            driver.swipe(150,400,150,200,6000)
            count = count + 1
            print(text,txt)
        count = 1
        while count != 0:
            print(count)
            driver.swipe(150,400,150,200,6000)
            count = count - 1

        driver.find_element_by_id(POST_VARIABLES.REBLOG_BUTTON_ID).click()
        driver.implicitly_wait(50)
        driver.find_element_by_xpath(POST_VARIABLES.TEXT_XPATH).send_keys(text2)
        driver.find_element_by_id(POST_VARIABLES.REBLOG_ACTION_BUTTON_ID).click()
        return True 
    except :
        return False


# function to create post given its text - done #
def create_post(text):
    # try:
    #navigate_to_posts()
       driver.find_element_by_xpath(POST_VARIABLES.CREATE_POST_BUTTON).click()
       driver.implicitly_wait(20)
       driver.find_element_by_xpath(POST_VARIABLES.POST_TEXT_XPATH).send_keys(text)
       driver.find_element_by_xpath(POST_VARIABLES.POST_BUTTON).click()
       driver.find_element_by_xpath("//android.view.View[@content-desc=\"Profile Tab 4 of 4\"]").click()
    #    driver.find_element_by_xpath(POST_VARIABLES.POST_ICON_XPATH).click()
    #    count = 1
    #    while count >= 0:
    #     print(count)
    #     driver.swipe(150,200,150,800,6000)
    #     count = count -1
    #    return True
    # except:
    #     return False


login("mennaahmedali77@gmail.com","1234567menna")
# navigate_to_posts()
create_post("TEMP POST")
# create_post("TEMP POST FOR DELETE")
# create_post("TEMP POST FOR DELETE2")
# delete_post("TEMP POST FOR DELETE")
# add_like_post("by a test script")
# add_comment_post("10","This comment is created via a test script woohwoooooooooooooooooo")
# send_post("8")
# reblog_post("10","rebloged via a test script")
# edit_post("First post is edited by","First post")
# edit_tag("1","First post")
 
