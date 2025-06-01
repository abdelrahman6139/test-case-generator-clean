import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods remain the same) ...

    def test_login_after_failure(self):
        # ... (similar to previous tests, but with two login attempts) ...