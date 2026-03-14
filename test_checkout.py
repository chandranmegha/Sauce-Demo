import pytest
from selenium import webdriver
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class TestCheckout:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        # Login
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)
        
        # Add item
        products_page = ProductsPage(self.driver)
        products_page.add_first_item_to_cart()
        time.sleep(2)
        
        # Go to cart
        products_page.click_cart()
        time.sleep(2)
    
    def teardown_method(self):
        self.driver.quit()
    
    def test_checkout_with_valid_info(self):
        cart_page = CartPage(self.driver)
        
        # Verify item in cart
        item_count = cart_page.get_item_count()
        assert item_count == 1
        
        # Complete checkout
        cart_page.click_checkout()
        time.sleep(2)
        cart_page.enter_checkout_info("John", "Doe", "12345")
        time.sleep(1)
        cart_page.click_continue()
        time.sleep(2)
        cart_page.finish_checkout()
        time.sleep(2)
        
        # Verify success
        success_msg = cart_page.get_success_message()
        assert "THANK YOU" in success_msg.upper()
    
    def test_checkout_empty_fields(self):
        cart_page = CartPage(self.driver)
        
        # Verify item in cart
        item_count = cart_page.get_item_count()
        assert item_count == 1
        
        # Try checkout with empty fields
        cart_page.click_checkout()
        time.sleep(2)
        cart_page.click_continue()
        time.sleep(2)
        
        # Should stay on checkout page
        current_url = self.driver.current_url
        assert "checkout-step-one" in current_url