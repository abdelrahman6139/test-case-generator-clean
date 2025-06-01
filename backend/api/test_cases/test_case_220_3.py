import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown same as TC_LOGIN_001)
    def test_invalid_password(self):
        # ... (similar to test_invalid_username, changing input values)
        pass
    # ... (tearDown)