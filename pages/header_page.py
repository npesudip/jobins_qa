from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HeaderObject(BasePage):
    TITLE = "JoBins Recruitment"


    '''
    Header Section: 1. Navigation menu link validation. 2. Button presence and click action testing.

    1.listing out the locators & urls
    
    '''

    # Locator lists (using XPath for linked text)
    menu_home_xp = "//span[contains(@class,'border-[#03275A] font-bold')]"
    menu_about_xp = "//span[contains(@class,'text-[#03275A] border-transparent') and contains(text(),'JoBinsについて')]"
    menu_member_xp = "//span[text()='メンバー紹介']"
    menu_work_style_xp = "//span[contains(text(), '働き方')]"
    menu_entry_btn_xp="//span[contains(@class, 'py-3') and text()='メンバー紹介']"
    become_member_lt = "メンバー紹介"


    home_url_keyword = "jobins.net"
    about_url_keyword = "about"
    member_url_keyword = "team-member"
    working_url_keyword = "working"
    entry_url_keyword="career"
        


    def __init__(self, driver):
        super().__init__(driver)


    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_title(self):
        """Verify the page title."""
        assert self.driver.title == self.TITLE, f"Expected title '{self.TITLE}', but got '{self.driver.title}'"

    # Navigation menu actions
    def click_home_menu(self):
        """Click on the Home menu."""
        home_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_home_xp))
        )
        home_menu.click()

    def click_about_menu(self):
        """Click on the About menu."""
        about_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_about_xp))
        )
        about_menu.click()


    def click_member_menu(self):
        """Click on the Become a Member menu and verify URL change."""
        print(f"Trying to locate member menu using locator: {self.menu_member_xp}")
        
        # Wait for the element to be clickable
        member_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_member_xp))
        )
        
        # Debug: Print confirmation that the element was found
        print(f"Locator found: {self.menu_member_xp}. Element is clickable.")
        
        # Click the element
        member_menu.click()
        
        # Debug: Print confirmation that the click action was performed
        print("Clicked on the member menu.")
        
        # Wait for the URL to change to include the keyword 'team-member'
        WebDriverWait(self.driver, 10).until(EC.url_contains("team-member"))
        
        # Print the current URL after the click
        print(f"Current URL after click: {self.driver.current_url}")


    def click_work_style_menu(self):
        """Click on the Work Style menu."""
        work_style_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_work_style_xp))
        )
        work_style_menu.click()

    # def click_entry_button(self):
    #     """Click on the Entry button."""
    #     entry_btn = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.menu_entry_btn_xp))
    #     )
    #     entry_btn.click()


    def click_entry_button(self):
        """Click on the Entry button and verify URL change."""
        print(f"Trying to locate entry button using locator: {self.menu_entry_btn_xp}")
        
        # Wait for the Entry button to be clickable
        entry_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_entry_btn_xp))
        )
        
        # Debug: Print confirmation that the button was found
        print(f"Locator found: {self.menu_entry_btn_xp}. Button is clickable.")
        
        # Click the Entry button
        entry_btn.click()
        current_page_title=self.driver.title
        print(current_page_title)
        
        # Wait for the URL to contain the keyword 'career'
        WebDriverWait(self.driver, 20).until(EC.url_contains(self.entry_url_keyword))
        
        # Debug: Print the current URL after the click
        print(f"Current URL after click: {self.driver.current_url}")
    