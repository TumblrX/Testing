from appium import webdriver
from support import log_in_func, message_func, desiredcapabilities
import unittest

class TestLogin(unittest.TestCase):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities.desiredcap)
    def test_search_for_new_chat(self):   #done..
        log_in_func.working_log_in(self.driver, "ammar@gmail.com", "123456")
        self.assertTrue(message_func.test_search_for_new_chat(self.driver, "Andrew", "Hello Andrew from test script"))
    def test_delete_conversation(self):
        self.assertTrue(message_func.delete_conversation(self.driver))

if __name__ == '__main__':
    unittest.main()
