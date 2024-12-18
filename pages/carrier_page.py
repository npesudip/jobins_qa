
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CarrierPageObjects(BasePage):
    TITLE = "JoBins Recruitment"

    # Locators for tabs and job board
    carrier_section_xp = "//h2[normalize-space(text())='Career Opening']"
    carrier_recruiting_xp = "//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, 'キャリア採用') and @role='tab']"
    carrier_new_graduate_xp = "//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, '新卒採用') and @role='tab']"
    carrier_long_term_xp = "//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, '長期インターン採用') and @role='tab']"
    job_board_xp = "//a[contains(@class, 'bg-white') and contains(@href, '/career/')]"
    job_details_page_url = "https://recruit.release.jobins.net/career/JV00000004"

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_title(self):
        """Verify the page title."""
        assert self.driver.title == self.TITLE, f"Expected title '{self.TITLE}', but got '{self.driver.title}'"

    def move_to_carrier_opening_section(self):
        """Scroll to the Career Opening section and click on it."""
        self._scroll_and_click(self.carrier_section_xp, "Career Opening section")

    # def click_filter_carrier_requirement(self):
    #     """Click on the Recruiting tab."""
    #     self._scroll_and_click(self.carrier_recruiting_xp, "Carrier Recruiting")


    def click_filter_carrier_requirement(self):
        """Click on the recruiting filter after ensuring the element is visible and clickable."""
        
        # Close any modal or overlay if present
        self.close_modal_if_exists()

        # Wait for the element to be clickable
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.carrier_recruiting_xp))
        )
        
        # Scroll to the element to ensure it's in view
        element = self.driver.find_element(By.XPATH, self.carrier_recruiting_xp)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # Scroll to the element

        # Click using JavaScript to bypass any visibility issues
        self.driver.execute_script("arguments[0].click();", element)


    def click_filter_carrier_new_graduate_tab(self):
        """Click on the New Graduate tab."""
        self._scroll_and_click(self.carrier_new_graduate_xp, "New Graduate")

    def click_filter_carrier_long_term_tab(self):
        """Click on the Long Term Internship tab."""
        self._scroll_and_click(self.carrier_long_term_xp, "Long Term Internship")

    def click_job_board(self):
        """Click on a job board item."""
        self._scroll_and_click(self.job_board_xp, "Job board")



    def _scroll_and_click(self, xpath, element_name):
        """Scroll to an element and click on it."""
        print(f"Scrolling to and trying to click on: {element_name} using XPath: {xpath}")
        try:
            # Wait for the element to be present and visible
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            # Scroll the element into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)  # Allow scrolling animation to complete

            # Slightly scroll up to avoid sticky headers
            self.driver.execute_script("window.scrollBy(0, -100);")

            # Wait until the element is clickable and click it
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            print(f"Successfully clicked on '{element_name}'.")

            # Verify the page has loaded after the click
            self._check_if_page_loaded()

        except TimeoutException:
            print(f"Failed to locate '{element_name}' using XPath: {xpath}")
            # Fallback to JavaScript click
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                self.driver.execute_script("arguments[0].click();", element)
                print(f"Clicked on '{element_name}' using JavaScript.")
            except Exception as js_click_error:
                print(f"JavaScript click also failed for '{element_name}': {js_click_error}")
                self.driver.save_screenshot("debug_screenshot.png")
                raise


    def _check_if_page_loaded(self):
        """Verify if the page has finished loading."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.carrier_section_xp))
            )
            print("Page has successfully loaded.")
        except Exception as e:
            print(f"Page load failed: {e}")

    def _verify_element_visible(self, xpath, element_name):
        """Verify if an element is visible on the page."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            print(f"Element '{element_name}' is visible on the page.")
        except Exception as e:
            print(f"Element '{element_name}' not visible: {e}")


    def get_job_blocks(self):
        return self.driver.find_elements(By.XPATH, "//a[contains(@class, 'bg-white') and contains(@href, '/career/')]")
    

    def close_modal_if_exists(self):
        """Close any modal or overlay that may be blocking the click action."""
        try:
            modal_close_button = self.driver.find_element(By.XPATH, "//button[@class='modal-close']")
            modal_close_button.click()  # Close the modal if it exists
        except:
            pass  # Ignore if no modal is found