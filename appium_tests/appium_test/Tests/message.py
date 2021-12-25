from support import log_in_func, message_func
import unittest

class TestLogin(unittest.TestCase):
    # def test_to_log_in(self):
    #     log_in_func.working_log_in("nadaelsayed@gmail.com", "nadaelsayed147258369")
    def test_search_for_new_chat(self):   #done..
        self.assertTrue(message_func.test_search_for_new_chat("esraagamal22", "Hello essraaa from test script")) #reginaPhalangePheobe
    def test_send_word(self):   #done..
        self.assertTrue(message_func.test_chat_friend("Hello essraaa from test script"))
    def test_send_photo_camera(self): #done..
        self.assertTrue(message_func.test_send_photo("camera"))
    def test_send_photo_gallery(self): #done..
        self.assertTrue(message_func.test_send_photo("gallerg"))
    def test_send_GIF_top(self):
        self.assertTrue(message_func.test_send_GIF("top"))
    def test_send_GIF_recent(self):
        self.assertTrue(message_func.test_send_GIF("recent"))
    def test_delete_conversation(self):
        self.assertFalse(message_func.delete_conversation("esraagamal22"))

if __name__ == '__main__':
    unittest.main()
