import pytest
from selenium import webdriver
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        self.driver.quit()
    
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)
        assert "inventory" in self.driver.current_url
        print("Valid login test passed")
    
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("invalid_user", "wrong_password")
        time.sleep(2)
        error_msg = login_page.get_error_message()
        assert "Username and password do not match" in error_msg
        print("Invalid login test passed")