import unittest
from selenium import webdriver

class TestFailedExecution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_pass(self):
        self.assertTrue(True)
    def test_fail(self):
        self.assertTrue(False)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()