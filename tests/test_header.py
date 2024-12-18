import pytest
from selenium import webdriver
from pages.header_page import HeaderObject  
from utils.driver_manager import DriverManager  
import time

class TestHeader:
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver, login, and provide the driver for tests."""
        
        # Initialize DriverManager
        driver_manager = DriverManager()
        
        # Initialize the WebDriver and perform login
        driver_manager.initialize_driver()
        
        # Yield the driver to the test functions
        driver = driver_manager.get_driver()
        yield driver  
        
        # Quit the driver after tests are done
        driver_manager.quit_driver()

    def test_home_menu(self, driver):
        """Test Home menu navigation."""
        home_page = HeaderObject(driver)  # Initialize the HomePage object
        home_page.click_home_menu()  # Clicking Home menu
        assert home_page.home_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.home_url_keyword}', but got '{driver.current_url}'"

    def test_about_menu(self, driver):
        """Test About menu navigation."""
        home_page = HeaderObject(driver)  # Initialize the HomePage object
        home_page.click_about_menu()  # Clicking About menu
        assert home_page.about_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.about_url_keyword}', but got '{driver.current_url}'"
    
    def test_member_menu(self, driver):
        """Test Become Member menu navigation."""
        home_page = HeaderObject(driver)  # Initialize the HomePage object
        home_page.click_member_menu()  # Clicking Become Member menu

        assert home_page.member_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.member_url_keyword}', but got '{driver.current_url}'"
    
    def test_work_style_menu(self, driver):
        """Test Work Style menu navigation."""
        home_page = HeaderObject(driver)  # Initialize the HomePage object
        home_page.click_work_style_menu()  # Clicking Work Style menu
        assert home_page.working_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.working_url_keyword}', but got '{driver.current_url}'"


    def test_entry_button(self, driver):
        """Test Entry button navigation."""
        expected_current_page_title ="採用情報 | Recruit"

        home_page = HeaderObject(driver)  # Initialize the HomePage object
        home_page.click_entry_button()  # Clicking Entry button
        home_page.click_entry_button()  # Clicking Entry button


        assert driver.click_entry_button.current_page_title ==expected_current_page_title

        # # Assert that the URL contains the expected 'career' keyword
        # assert home_page.entry_url_keyword in driver.current_url, \
        #     f"Expected URL to contain '{home_page.entry_url_keyword}', but got '{driver.current_url}'"