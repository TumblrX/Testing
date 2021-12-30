from support import sign_up_func
import unittest

class TestSignUp(unittest.TestCase):
#---- Email ---------------------------------------------------------------------------------------------------------
    # def test_empty_email(self):
    #     self.assertEqual(sign_up_func.invalid_email(""), "Make sure all fields are filled")
    # def test_space_email(self):
    #     self.assertEqual(sign_up_func.invalid_email(" "), "Make sure all fields are filled")
    # def test_invalid_email(self):
    #     self.assertEqual(sign_up_func.invalid_email("mennaahmedali@ex"), "Enter a correct email")
    # def test_taken_email(self):
    #     self.assertEqual(sign_up_func.invalid_email("test@test.com"), "User is already registered")
#---- Password ---------------------------------------------------------------------------------------------------------
    # def test_empty_password(self):
    #     self.assertEqual(sign_up_func.invalid_password(""), "Make sure all fields are filled")
    # def test_space_password(self):
    #     self.assertEqual(sign_up_func.invalid_password(" "), "Make sure all fields are filled")
    # def test_small_password(self):
    #     self.assertEqual(sign_up_func.invalid_password("123"), "Password is too short")
#---- Blogname ---------------------------------------------------------------------------------------------------------
    def test_empty_blogname(self):
        self.assertEqual(sign_up_func.invalid_blog_name(""), "Make sure all fields are filled")
    def test_space_blogname(self):
        self.assertEqual(sign_up_func.invalid_blog_name(" "), "Make sure all fields are filled")
    def test_big_blogname(self):
        self.assertEqual(sign_up_func.invalid_blog_name("1111111111111111111111111111111111"), "Username is invalid, make sure it is less than 32 characters, and only contains letter, numbers, or dashes (-)")
    def test_char_in_blogname(self):
        self.assertEqual(sign_up_func.invalid_blog_name("Nada Elsayed"), "Username is invalid, make sure it is less than 32 characters, and only contains letter, numbers, or dashes (-)")
    def test_taken_blogname(self):
        self.assertEqual(sign_up_func.invalid_blog_name("Testing"), "User is already registered")
#---- age ---------------------------------------------------------------------------------------------------------
    # def test_empty_age(self):
    #     self.assertEqual(sign_up_func.invalid_age(""), "Make sure all fields are filled")
    # def test_space_age(self):
    #     self.assertEqual(sign_up_func.invalid_age(" "), "Make sure all fields are filled")
    # def test_less_than_13_age(self):
    #     self.assertEqual(sign_up_func.invalid_age("10"), "Enter a valid age between 13 and 130")
    # def test_more_than_130_age(self):
    #     self.assertEqual(sign_up_func.invalid_age("200"), "Enter a valid age between 13 and 130")
#---- working ---------------------------------------------------------------------------------------------------------
#     def test_working_sign_up(self):
#         self.assertTrue(sign_up_func.working_sign_up("nada@test.com", "123456789", "Testing", "20"))


if __name__ == '__main__':
    unittest.main()

