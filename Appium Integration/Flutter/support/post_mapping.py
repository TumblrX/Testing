class POST_VARIABLES():
    ################ LOGIN ############################
    LOGIN_BUTTON_XPATH = "//android.widget.Button[@content-desc=\"Log in\"]"
    LOGIN_WITH_EMAIL_XPATH = "//android.widget.Button[@content-desc=\"Log in with Email\"]"
    EMAIL_INPUT_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"
    PASSWORD_INPUT_XPATH ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]"
    LOGIN_FINAL_BUTTON_XPATH = "//android.widget.Button[@content-desc=\"Login\"]"
    ##############CREATE POSTS ###################
    CREATE_POST_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button"
    POST_TEXT_XPATH= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.EditText"
    POST_BUTTON ="//android.widget.Button[@content-desc=\"Post\"]"