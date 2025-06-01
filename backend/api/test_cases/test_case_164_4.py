import unittest
from selenium import webdriver
from unittest import skip

class TestSkippedExecution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    @skip("Skipping this test")
    def test_skipped(self):
        pass
    def test_regular(self):
        self.assertTrue(True)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()