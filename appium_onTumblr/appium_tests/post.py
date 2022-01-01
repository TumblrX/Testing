from support import post_func
import unittest


class TestPost(unittest.TestCase):
    def Test_0(self):
        self.assertTrue(post_func.navigate_to_posts())
    def test_1(self):
        self.assertTrue(post_func.create_post("TEMP POST FOR DELETE"))
    def test_2(self):
        self.assertTrue(post_func.create_post("TEMP POST FOR DELETE2"))
    def test_3(self):
        self.assertTrue(post_func.create_post("3"))
    def test_4(self):
        self.assertTrue(post_func.delete_post("TEMP POST FOR DELETE"))
    def test_5(self):
        self.assertTrue(post_func.add_like_post("TEMP POST FOR DELETE2"))
    def test_6(self):
        self.assertTrue(post_func.add_comment_post("10","This comment is created via a test script woohwoooooooooooooooooo"))
    def test_7(self):
        self.assertTrue(post_func.send_post("8"))
    def test_8(self):
        self.assertTrue(post_func.reblog_post("10","rebloged via a test script"))
if __name__ == '__main__':
    unittest.main()
     