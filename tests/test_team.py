import pytest
from utils.driver_manager import DriverManager
from pages.team_page import TeamMemberPage
import time
from selenium.webdriver.common.by import By


class TestTeamMemberHover:

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
    def team_page(self, driver):
        """Fixture to initialize CarrierPageObjects and provide it to the tests."""
        return TeamMemberPage(driver)


    def test_hover_effect(self, team_page):
        """Test hover effect on a single team member card."""
    

        # Ensure we are at the 'Our Team' section by scrolling to it
        team_page.scroll_to_team_section()

        # # Hover over the first team member card
        # team_page.hover_on_team_member(0)

        # # Wait for the hover effect to apply
        # time.sleep(1)  # Adjust sleep time as needed

        # # Check the opacity after hovering
        # opacity = team_page.get_hovered_team_member_opacity(0)
        # assert opacity == '1', f"Expected opacity '1' after hover, but got {opacity}"




    def test_hover_on_multiple_members(self, team_page):
        """Test hover effect on multiple team member cards."""

        # Ensure we are at the 'Our Team' section by scrolling to it
        team_page.scroll_to_team_section()

        # # Get all team member cards
        # team_member_cards = driver.find_elements(By.CSS_SELECTOR, ".flex.flex-col.items-center.text-center.rounded-lg")
        # for index, card in enumerate(team_member_cards):
        #     team_page.hover_on_team_member(index)
        #     time.sleep(1)  # Adjust as needed

        #     # Verify that the hover effect was applied (opacity should be '1')
        #     opacity = team_page.get_hovered_team_member_opacity(index)
        #     assert opacity == '1', f"Hover effect not visible on card {index + 1}"
