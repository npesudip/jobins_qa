# import pytest
# from selenium import webdriver
# from pages.home_page import HomePage  # Import your HomePage class
# from utils.driver_manager import DriverManager  # Import the DriverManager class

# class TestHeader:
#     @pytest.fixture(scope="class")
#     def driver(self):
#         """Setup WebDriver, login, and provide the driver for tests."""
        
#         # Initialize DriverManager
#         driver_manager = DriverManager()
        
#         # Initialize the WebDriver and perform login
#         driver_manager.initialize_driver()
        
#         # Yield the driver to the test functions
#         driver = driver_manager.get_driver()
#         yield driver  # Give control to the test function
        
#         # Quit the driver after tests are done
#         driver_manager.quit_driver()

#     def test_navigation_menu(self, driver):
#         """Test navigation menu items on the home page."""
#         home_page = HomePage(driver)  # Initialize the HomePage object
        
#         # Test the navigation menu items
#         home_page.click_home_menu()  # Clicking Home menu
#         assert home_page.home_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.home_url_keyword}', but got '{driver.current_url}'"

        
#         home_page.click_about_menu()  # Clicking About menu
#         assert home_page.about_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.about_url_keyword}', but got '{driver.current_url}'"
        
#         home_page.click_member_menu()  # Clicking Become Member menu
#         assert home_page.member_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.member_url_keyword}', but got '{driver.current_url}'"
        
#         home_page.click_work_style_menu()  # Clicking Work Style menu
#         assert home_page.working_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.working_url_keyword}', but got '{driver.current_url}'"
        
#         home_page.click_entry_button()  # Clicking Entry button
#         assert home_page.entry_url_keyword in driver.current_url, f"Expected URL to contain '{home_page.entry_url_keyword}', but got '{driver.current_url}'"

    # def test_footer_links(self, driver):
    #     """Test the social media links in the footer."""
    #     home_page = HomePage(driver)  # Initialize the HomePage object
        
    #     # Test social media links
    #     home_page.click_wantedly_link()  # Clicking Wantedly link
    #     assert driver.current_url == home_page.wantedly_url, f"Expected URL {home_page.wantedly_url}, but got {driver.current_url}"
        
    #     driver.back()  # Go back to the previous page
        
    #     home_page.click_facebook_link()  # Clicking Facebook link
    #     assert driver.current_url == home_page.facebook_url, f"Expected URL {home_page.facebook_url}, but got {driver.current_url}"

    # def test_job_filter_tabs(self, driver):
    #     """Test job filtering functionality."""
    #     home_page = HomePage(driver)  # Initialize the HomePage object
        
    #     # Test job filter tabs
    #     home_page.click_carrier_recruiting_tab()  # Clicking Recruiting tab
    #     assert "採用情報" in driver.page_source, "Recruiting information not found"
        
    #     home_page.click_carrier_new_graduate_tab()  # Clicking New Graduate tab
    #     assert "新卒採用" in driver.page_source, "New Graduate information not found"
        
    #     home_page.click_carrier_long_term_tab()  # Clicking Long Term Internship tab
    #     assert "長期インターン採用" in driver.page_source, "Long-term Internship information not found"

    # def test_team_member_hover(self, driver):
    #     """Test hover effect on team member cards."""
    #     home_page = HomePage(driver)  # Initialize the HomePage object
        
    #     # Test hover effect on team member card
    #     home_page.hover_over_team_member_card()  # Hover over a team member card
    #     assert "team member info" in driver.page_source, "Team member info not visible"

    # def test_faq_expansion(self, driver):
    #     """Test FAQ expansion and collapse behavior."""
    #     home_page = HomePage(driver)  # Initialize the HomePage object
        
    #     # Test FAQ expansion
    #     home_page.click_faq_card()  # Click an FAQ card to expand
    #     assert "answer content" in driver.page_source, "Answer content not found"
        
    #     # Test FAQ collapse
    #     home_page.click_faq_card()  # Click the same FAQ card to collapse
    #     assert "answer content" not in driver.page_source, "Answer content still visible after collapse"
