from appium import webdriver
from ..desiredcapabilities import driver ,driver_startActivity,desired_cap
from support import log_in_func
import unittest

class TestLogin(unittest.TestCase):

    def test_invalid_email(self):
        self.assertEqual(log_in_func.invalid_email("mennaahmedali@ex","unvalid email"), "unvalid email")
    def test_empty_email(self):
        self.assertEqual(log_in_func.empty_email("","1111", "Please enter some text"), "Please enter some text")
    def test_wrong_email_or_pass(self):
        self.assertEqual(log_in_func.wrong_email_or_pass("mennaahmedali77@gmail.com","1", "wrong Email or password please try again"), "wrong Email or password please try again")
    def test_empty_password(self):
        self.assertEqual(log_in_func.empty_password("mennaahmedali77@gmail.com","", "Please enter some text"), "Please enter some text")
    def test_working_log_in(self):
        self.assertTrue(log_in_func.working_log_in("nadaelsayed@gmail.com", "nadaelsayed147258369"))


if __name__ == '__main__':
    unittest.main()
