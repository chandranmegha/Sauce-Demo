import pytest
from selenium import webdriver
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class TestCart:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)
    
    def teardown_method(self):
        self.driver.quit()
    
    def test_add_single_item_to_cart(self):
        products_page = ProductsPage(self.driver)
        initial_count = products_page.get_cart_count()
        assert initial_count == 0
        
        result = products_page.add_first_item_to_cart()
        assert result == True
        
        time.sleep(2)
        new_count = products_page.get_cart_count()
        assert new_count == 1
    
    def test_cart_page_displays_items(self):
        products_page = ProductsPage(self.driver)
        
        result = products_page.add_first_item_to_cart()
        assert result == True
        
        time.sleep(2)
        cart_count = products_page.get_cart_count()
        assert cart_count == 1
        
        products_page.click_cart()
        time.sleep(2)
        
        cart_page = CartPage(self.driver)
        item_count = cart_page.get_item_count()
        assert item_count == 1