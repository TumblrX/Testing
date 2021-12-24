from appium import webdriver
from post_mapping import POST_VARIABLES
from desiredcapabilites import DESIRED_CAP

driver = webdriver.Remote("http://localhost:4723/wd/hub",DESIRED_CAP)


def navigate_to_posts():
    try:
       driver.find_element_by_id(POST_VARIABLES.ACCOUNT_ICON).click()
       driver.find_element_by_xpath(POST_VARIABLES.POST_ICON_XPATH).click()
       return True
    except:
        return False

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
    

 

# edit post if it has text only
def edit_post(text,new_text):
    
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

# delete post given its text
def delete_post(text):
    
    count = 0
    driver.swipe(150,400,150,200,2000)
    txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
    while text != txt:
        txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
        driver.swipe(150,800,150,200,2000)
        count = count + 1
    driver.find_element_by_id(POST_VARIABLES.DELETE_BUTTON_ID).click()
    driver.find_element_by_id(POST_VARIABLES.CONFIRM_DELETE_POST_BUTTON).click()
    navigate_to_posts()
    while count >= 0:
        print(count)
        driver.swipe(150,200,150,800,6000)
        count = count -1 
    return True

def add_like_post(text):
    
    count = 0
    temp = " "
    txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
    temp = txt
    while text != txt:
        driver.swipe(150,1000,150,200,6000)
        txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
        if temp != txt: count=count+1
        temp = txt
        print(count,txt)
        
    lis=driver.find_element_by_xpath(POST_VARIABLES.LIKE_BUTTON_XPATH+"["+str(count)+"]")
    lis.click()

def add_comment_post(text,comment):
    
    count = 0
    driver.swipe(150,400,150,200,2000)
    txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
    while text != txt:
        print(count)
        txt = driver.find_element_by_id(POST_VARIABLES.POST_TEXT_ID_FOR_DELETE).text
        driver.swipe(150,800,150,200,2000)
        count = count + 1
    driver.find_element_by_id(POST_VARIABLES.COMMENT_BUTTON_ID).click()



# function to create post given its text

def create_post(text):
    try:
       driver.find_element_by_id(POST_VARIABLES.COMPOSE_POST_BUTTON_ID).click()
       driver.implicitly_wait(20)

       driver.find_element_by_xpath(POST_VARIABLES.POST_TEXTBOX_XPATH).send_keys(text)
       driver.find_element_by_id(POST_VARIABLES.POST_BUTTON_ID).click()

       driver.find_element_by_xpath(POST_VARIABLES.POST_ICON_XPATH).click()
       return True
    except:
        return False

navigate_to_posts()
# create_post("This post is created via a test script")
# delete_post_by_search("This post is created via a test script")
# edit_post("First post is edited by","First post")
# edit_tag("1","First post")
# delete_post("Third post")
add_like_post("5")


 
