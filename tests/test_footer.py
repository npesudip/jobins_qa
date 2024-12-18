import pytest
from pages.footer_page import FooterObject  
from utils.driver_manager import DriverManager  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFooterSection:
    
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

    def test_wantedly_link(self, driver):
        """Test the Wantedly link in the footer."""
        footer_page = FooterObject(driver)  # Pass WebDriver to the FooterObject
        
        # Click on the Wantedly link
        footer_page.click_wantedly_link()

        # Wait for the new tab to load and verify the URL
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        original_window = driver.current_window_handle
        new_window = [window for window in driver.window_handles if window != original_window][0]

        driver.switch_to.window(new_window)

        # Verify the URL for the new tab
        assert driver.current_url == footer_page.wantedly_url, \
            f"Expected URL {footer_page.wantedly_url}, but got {driver.current_url}"

        # Close the new tab and switch back to the original window
        driver.close()
        driver.switch_to.window(original_window)


    def test_facebook_link(self, driver):
        """Test the Facebook link in the footer."""
        footer_page = FooterObject(driver)  # Pass WebDriver to the FooterObject
        
        # Click on the Facebook link
        footer_page.click_facebook_link()

        # Wait for the new tab to load and verify the URL
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        original_window = driver.current_window_handle
        new_window = [window for window in driver.window_handles if window != original_window][0]

        driver.switch_to.window(new_window)

        # Verify the URL for the new tab
        assert driver.current_url == footer_page.facebook_url, \
            f"Expected URL {footer_page.facebook_url}, but got {driver.current_url}"

        # Close the new tab and switch back to the original window
        driver.close()
        driver.switch_to.window(original_window)
