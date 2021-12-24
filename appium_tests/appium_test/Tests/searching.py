from support import log_in_func, searching_func
import unittest

class TestLogin(unittest.TestCase):
    def to_log_in(self):
        log_in_func.working_log_in("nadaelsayed@gmail.com", "nadaelsayed147258369")
    def is_there_placeholder(self):
        self.assertEqual(searching_func., "That email doesn't have a Tumblr account. Sign up now?")
    def test_empty_search(self):
        self.assertEqual(log_in_func.invalid_email(""), "Make sure both fields are filled.")
    def test_only_spaces(self):
        self.assertEqual(log_in_func.false_password("123"), "Incorrect email address or password. Please try again.")
    def test_text_with_spaces_in(self):
        self.assertEqual(log_in_func.false_password(""), "Make sure both fields are filled.")
    def unknowen_tag(self):
        self.assertTrue(log_in_func.working_log_in("nadaelsayed@gmail.com", "nadaelsayed147258369"))
    def knowen_tag(self):
        self.assertTrue(log_in_func.working_log_in("nadaelsayed@gmail.com", "nadaelsayed147258369"))


if __name__ == '__main__':
    unittest.main()
