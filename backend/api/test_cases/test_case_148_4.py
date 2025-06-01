import unittest
from selenium import webdriver
class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_add_to_cart(self):
        self.driver.get("https://example.com/product")
        # Add your add to cart logic here
        # ...
        cart_count = self.driver.find_element_by_id("cart-count").text # Replace with actual element ID
        self.assertGreater(int(cart_count), 0)
    def tearDown(self):
        self.driver.quit()