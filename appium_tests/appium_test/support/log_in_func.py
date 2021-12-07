from appium import webdriver

desiredcap = {
  "platformName": "Android",
  "appium:platformVersion": "8.0.0",
  "appium:deviceName": "HUAWEI GR3 2017",
  "appium:automationName": "Appium",
  "appium:udid": "PSE7N17802001262"
}
def invaled_email(email, msg):
    driver.find_element_by_id("com.tumblr:id/email_auth_button").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/email").send_keys("nadaelsayed163@ex")
    driver.find_element_by_id("com.tumblr:id/primary_button").click()
    driver.implicitly_wait(30)
    text = driver.find_element_by_id("com.tumblr:id/action_message_text").text
    assertEquals(msg, text)
    return

def false_password(password, msg):
    driver.find_element_by_id("com.tumblr:id/email_auth_button").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/email").send_keys("nadaelsayed163@gmail.com")
    driver.find_element_by_id("com.tumblr:id/primary_button").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/use_password_button").click()
    driver.implicitly_wait(50)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.MultiAutoCompleteTextView").send_keys(password)
    driver.implicitly_wait(50)
    driver.find_element_by_id("com.tumblr:id/action_button").click()
    driver.implicitly_wait(50)
    text = driver.find_element_by_id("com.tumblr:id/action_message_text").text
    assertEquals(msg, text)
    text = driver.find_element_by_id("com.tumblr:id/action_message_text").text
    assertEquals(msg, text)
    return

def working_log_in(email, password):
    driver.find_element_by_id("com.tumblr:id/login_button").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/email_auth_button").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/email").send_keys(email)
    driver.find_element_by_id("com.tumblr:id/primary_button").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("com.tumblr:id/use_password_button").click()
    driver.implicitly_wait(50)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.MultiAutoCompleteTextView").send_keys(password)
    driver.implicitly_wait(50)
    driver.find_element_by_id("com.tumblr:id/action_button").click()
    return