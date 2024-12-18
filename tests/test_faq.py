import pytest
from utils.driver_manager import DriverManager  
from pages.faq_page import FaqPageObjects  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestCarrierSection:

    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver, initialize the driver, and provide it for tests."""
        
        # Initialize DriverManager and get WebDriver
        driver_manager = DriverManager()
        driver_manager.initialize_driver()
        
        # Get the WebDriver instance
        driver = driver_manager.get_driver()
        
        # Yield the driver to the test functions
        yield driver
        
        # Quit the driver after tests are done
        driver_manager.quit_driver()

    @pytest.fixture(scope="class")
    def faq_page(self, driver):
        """Fixture to initialize CarrierPageObjects and provide it to the tests."""
        return FaqPageObjects(driver)
    
    def test_open_faq(self, faq_page):
        """Test if the recruiting filter displays correct job listings."""
        
        # Move to the Career Opening section and click on the recruiting filter tab
        faq_page.move_to_faq_section()

        # Use the method that ensures the element is clickable and not blocked
        faq_page.click_faq_card()
        time.sleep(2)
        faq_page.close_faq_card()



