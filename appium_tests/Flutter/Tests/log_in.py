from appium import webdriver
import log_in_mapping
from ..desiredcapabilities import driver ,driver_startActivity,desired_cap

driver.find_element_by_id().click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.tumblr:id/email_auth_button").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.tumblr:id/email").send_keys("mennaahmedali77@gmail.com")
driver.find_element_by_id("com.tumblr:id/primary_button").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.tumblr:id/use_password_button").click()
driver.implicitly_wait(50)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.MultiAutoCompleteTextView").send_keys('211257mennamenna')
driver.implicitly_wait(50)
driver.find_element_by_id("com.tumblr:id/action_button").click()