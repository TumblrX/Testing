from support import post_func
from support import log_in_func
import unittest

class TestPost(unittest.TestCase):
    def test_0(self):
        self.assertTrue(login("mennaahmedali77@gmail.com","1234567menna"))
    def test_1(self):
        self.assertTrue(post_func.create_post("by a test script2"))
        


if __name__ == '__main__':
    unittest.main()




