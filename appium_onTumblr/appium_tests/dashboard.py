from support import dashboard_func
import unittest


class TestDashboard(unittest.TestCase):
    def Test_0(self):
        self.assertTrue(dashboard_func.navigate_to_dashboard())
    def test_1(self):
        self.assertTrue(dashboard_func.add_like("3"))
    def test_2(self):
        self.assertTrue(dashboard_func.add_comment("3","BY TEST SCRIPT"))
    def test_3(self):
        self.assertTrue(dashboard_func.create_post("Demo post for testing creating posts from dashboard"))
    def test_4(self):
        self.assertTrue(dashboard_func.delete_post("Demo post for testing creating posts from dashboard"))
    def test_5(self):
        self.assertTrue(dashboard_func.reblog_post("5 days countdown to Christmas！ 🎄​​​​","rebloged by TS"))
    def test_6(self):
        self.assertTrue(dashboard_func.send_post("5 days countdown to Christmas！ 🎄​​​​"))
    def test_7(self):
        self.assertTrue(dashboard_func.upload_image_post())

if __name__ == '__main__':
    unittest.main()
     