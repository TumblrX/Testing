from support import settings_func ,log_in_func
import unittest


class TestSettings(unittest.TestCase):
    # def Test_0(self):
    #     self.log_in_func.working_log_in("mennaahmedali77@gmail.com","211257mennamenna")
    def test_1(self):
        self.assertTrue(settings_func.navigate_to_settings())
    def test_2(self):
        self.assertTrue(settings_func.change_email("mennaahmedali77@gmail.com","211257mennamenna"))
    def test_3(self):
        self.assertEqual(settings_func.change_password_with_old("211257mennamenna","211257mennamenna","Sorry, you've used that password before. You must choose a new password."), "Sorry, you've used that password before. You must choose a new password.")
    def test_4(self):
        self.assertEqual(settings_func.change_password_weak("2112","211257mennamenna","The password must be at least 8 characters."), "The password must be at least 8 characters.")
    def test_5(self):
        self.assertTrue(settings_func.change_password_working("mennaahmedali77@gmail.com","211257menna","211257mennamenna"))
    def test_6(self):
        self.assertTrue(settings_func.change_messaging_settings("onlytumblrs"))

if __name__ == '__main__':
    unittest.main()

