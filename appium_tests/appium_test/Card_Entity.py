from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "platformVersion": "10.0",
    "deviceName": "Nada",
    "automationName": "Appium",
    "appPackage": "com.tumblr",
    "appActivity": "com.tumblr.ui.activity.RootActivity"
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_cap)
driver.startActivity("com.tumblr", "com.tumblr.ui.activity.RootActivity")
