from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import time



class FaqPageObjects(BasePage):
    TITLE = "JoBins Recruitment"

    # Locators for tabs and job board
    faq_section_xp = "//h2[normalize-space(text())='FAQs']"
    faq_card_xp="//h3[contains(@class, 'flex') and @data-orientation='vertical' and button[contains(@class, 'font-bold')]]"
    faq_card_close_xp="//button[@aria-controls and @aria-expanded='true' and @data-orientation='vertical' and contains(@class, 'font-bold')]"


    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_title(self):
        """Verify the page title."""
        assert self.driver.title == self.TITLE, f"Expected title '{self.TITLE}', but got '{self.driver.title}'"

    def move_to_faq_section(self):
        """Scroll to the FAQ Opening section and click on it."""
        self._scroll_and_click(self.faq_section_xp, "FAQs section")

    # FAQ section actions
    def click_faq_card(self):
        """Click on an FAQ card."""
        faq_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.faq_card_xp))
        )
        faq_card.click()

    def close_faq_card(self):
        """Click on an FAQ card."""
        faq_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.faq_card_close_xp))
        )
        faq_card.click()
        
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
