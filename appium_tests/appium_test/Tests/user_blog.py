from support import user_blog_func
import unittest


class TestUser(unittest.TestCase):
    def test_0(self):
        self.assertTrue(user_blog_func.navigate_to_user_blog())
    def test_1(self):
        self.assertTrue(user_blog_func.edit_appearance_Header_image())
    def test_2(self):
        self.assertTrue(user_blog_func.edit_appearance_name("MENNA"))
    def test_3(self):
        self.assertTrue(user_blog_func.change_name_color())
    def test_4(self):
        self.assertTrue(user_blog_func.change_background())
    def test_5(self):
        self.assertTrue(user_blog_func.change_accent())
    def test_6(self):
        self.assertTrue(user_blog_func.change_description("BUTTERFLIES IMPACT NEVER LOST!!"))
    def test_7(self):
        self.assertTrue(user_blog_func.change_avatar("yes",""))
    def test_8(self):
        self.assertTrue(user_blog_func.following_settings())
    def test_9(self):
        self.assertTrue(user_blog_func.preview_user_blog_as_guest())

if __name__ == '__main__':
    unittest.main()
     