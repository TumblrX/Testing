from appium import webdriver
from support import log_in_func, searching_func, desiredcapabilities
import unittest

class TestLogin(unittest.TestCase):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities.desiredcap)
    def test_to_log_in(self):
        log_in_func.working_log_in(self.driver, "ammar@gmail.com", "123456")
    def test_placeholder(self):   #done..
        self.assertEqual(self.driver, searching_func.is_there_placeholder(), "Search Tumblr")
    # def test_empty_search(self): #done..
    #     self.assertEqual(searching_func.test_empty_search(), ["Recent", "Recommended"])
    # def test_only_spaces(self):
    #     self.assertEqual(searching_func.test_only_spaces(), ["Recent", "Recommended"])
    # def test_text_with_spaces_in(self):
    #     self.assertEqual(log_in_func.false_password(""), "Make sure both fields are filled.")
    # def unknowen_tag(self):
    #     self.assertTrue(log_in_func.working_log_in("nadaelsayed@gmail.com", "nadaelsayed147258369"))
    # def knowen_tag(self):
    #     self.assertTrue(log_in_func.working_log_in("nadaelsayed@gmail.com", "nadaelsayed147258369"))


if __name__ == '__main__':
    unittest.main()
