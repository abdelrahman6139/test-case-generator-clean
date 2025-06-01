import unittest
from selenium import webdriver

class TestReportFormat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_basic(self):
        self.assertTrue(True)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()