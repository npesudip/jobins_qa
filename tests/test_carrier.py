import pytest
from utils.driver_manager import DriverManager  
from pages.carrier_page import CarrierPageObjects  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    def carrier_page(self, driver):
        """Fixture to initialize CarrierPageObjects and provide it to the tests."""
        return CarrierPageObjects(driver)


    def test_carrier_recruiting_filter(self, carrier_page):
        """Test if the recruiting filter displays correct job listings."""
        
        # Move to the Career Opening section and click on the recruiting filter tab
        carrier_page.move_to_carrier_opening_section()

        # Use the method that ensures the element is clickable and not blocked
        carrier_page.click_filter_carrier_requirement()

        # Assert that job listings are displayed
        job_blocks = carrier_page.get_job_blocks()  # Assuming this method returns the list of job blocks
        assert len(job_blocks) > 0, "No job listings found after applying recruiting filter."

        # Verify that each job block contains relevant keywords
        for job in job_blocks:
            assert "システムエンジニア" in job.text or "正社員" in job.text, \
                f"Job block {job.text} does not match expected categories (e.g., System Engineer, Full-Time)."



    def test_carrier_new_graduate_filter(self, carrier_page):
        """Test if the new graduate filter displays correct job listings."""
        carrier_page.click_filter_carrier_new_graduate_tab()

        # Assert the job listings are displayed
        job_blocks = carrier_page.get_job_blocks()  # Assuming this method returns the list of job blocks
        assert len(job_blocks) > 0, "No job listings found after applying new graduate filter."

        # Verify that each job block contains relevant keywords like "New Graduate"
        for job in job_blocks:
            assert "新卒" in job.text or "New Graduate" in job.text, \
                f"Job block {job.text} does not match expected categories for new graduates."


    def test_click_filter_carrier_long_term_tab(self, carrier_page):
        """Test if the long term internship filter displays correct job listings."""
        carrier_page.click_filter_carrier_long_term_tab()

        # Assert the job listings are displayed
        job_blocks = carrier_page.get_job_blocks()  # Assuming this method returns the list of job blocks
        assert len(job_blocks) > 0, "No job listings found after applying long-term internship filter."

        # Verify that each job block contains relevant keywords for long-term internships
        for job in job_blocks:
            # Check for terms that represent long-term internships in the job text
            assert "Long-term intern" in job.text or "長期インターン" in job.text or "Long Term Internship" in job.text, \
                f"Job block {job.text} does not match expected categories for long-term internships."


    def test_job_board_link(self, carrier_page):
        """Test if job board link is clickable and navigates to the correct page."""
        carrier_page.click_job_board()
        WebDriverWait(carrier_page.driver, 10).until(
            EC.url_contains("JV")  # Updated condition
        )
        assert "JV" in carrier_page.driver.current_url, \
            f"Expected URL to contain 'career/JV', but got '{carrier_page.driver.current_url}'"

