from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

class TeamMemberPage:

    team_section_xp="//h2[normalize-space(text())='Our Team']"


    def __init__(self, driver):
        self.driver = driver
        self.team_member_cards = (By.CSS_SELECTOR, ".flex.flex-col.items-center.text-center.rounded-lg")

    
    def scroll_to_team_section(self):
        """Scroll to the 'Our Team' section of the page."""
        self._scroll_and_click(self.team_section_xp, "Team section")
        

    
    def hover_on_team_member(self, index):
        """Hover over a specific team member card."""
        team_member_card = self.driver.find_elements(*self.team_member_cards)[index]
        actions = ActionChains(self.driver)
        actions.move_to_element(team_member_card).perform()

    def get_hovered_team_member_opacity(self, index):
        """Get the opacity of a hovered team member card."""
        team_member_card = self.driver.find_elements(*self.team_member_cards)[index]
        return team_member_card.value_of_css_property('opacity')
    
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
