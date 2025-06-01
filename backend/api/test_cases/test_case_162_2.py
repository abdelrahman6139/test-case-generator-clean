import unittest
from selenium import webdriver

class TestMultipleExecutions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_execution_1(self):
        self.driver.get("about:blank")
        self.assertTrue(True)
    def test_execution_2(self):
        self.driver.get("about:blank")
        self.assertTrue(True)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()