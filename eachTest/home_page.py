from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    TITLE = "JoBins Recruitment"


    '''
    Header Section: 1. Navigation menu link validation. 2. Button presence and click action testing.

    1.listing out the locators & urls
    
    '''



    # Locator lists (using XPath for linked text)
    menu_home_xp = "//span[contains(@class,'border-[#03275A] font-bold')]"
    menu_about_xp = "//span[contains(@class,'text-[#03275A] border-transparent') and contains(text(),'JoBinsについて')]"
    menu_become_member_xp = "//span[contains(@class, 'py-3') and text()='メンバー紹介']"
    menu_work_style_xp = "//span[contains(text(), '働き方')]"
    menu_entry_btn_xp="//span[text()='エントリー']",

    # home_url = "https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/"
    # about_url ="https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/about-us"
    # member_url="https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/team-member"
    # working_url="https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/working"
    # entry_url="https://recruit.release.jobins.net/career"

    home_url_keyword = "jobins.net"
    about_url_keyword = "about"
    member_url_keyword = "team-member"
    working_url_keyword = "working"
    entry_url_keyword = "career"
        

    '''
    Footer Section : 1. Link validation for social media icons. 2. Footer content validation.
    '''

    # locators at footer (dynamic) and response on the click action
    wantedly_xp="//a[@href='https://www.wantedly.com/companies/jobins?ref=jobins.jp']"
    wantedly_url = "https://www.wantedly.com/companies/jobins?ref=jobins.jp"
    facebook_xp="//a[@href='https://www.facebook.com/jobins.jp?ref=jobins.jp']"
    facebook_url="https://www.facebook.com/jobins.jp?ref=jobins.jp"

    '''
    Hero Section : Visual regression testing for the hero section.

    '''


    ''' 
    Carrier Opening Sections : 1. Test job filtering functionality. 2. Validate job listing links.

    '''


    #Locator and filter action
    carrier_recruiting_xp="//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, 'キャリア採用') and @role='tab']"
    carrier_new_graduate_xp="//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, '新卒採用') and @role='tab']"
    carrier_logn_term_xp="//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, '長期インターン採用') and @role='tab']"

    # locator for apply button 
    job_board_xp="//h4[contains(@class, 'text-sm') and text()='システムエンジニア']"


    job_details_page_url="https://recruit.release.jobins.net/career/JV00000004" 
    #contains JV on url

    '''
    Our Team Section : Verify team member card structure and hover effects.
    
    '''

    #locators for our team card 
    team_member_card_xp="//div[contains(@class, 'z-[1]') and contains(@class, 'group-hover:opacity-100') and contains(@class, 'absolute')]"


    '''
    FAQ Section : 1. Test expand/collapse behavior programmatically. 2. Validate FAQ content structure.

    '''
    #faq locators 
    faq_card_xp="//div[contains(@class, 'z-[1]') and contains(@class, 'group-hover:opacity-100') and contains(@class, 'absolute')]"



    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_title(self):
        """Verify the page title."""
        assert self.driver.title == self.TITLE, f"Expected title '{self.TITLE}', but got '{self.driver.title}'"

    # Navigation menu actions
    def click_home_menu(self):
        """Click on the Home menu."""
        home_menu = WebDriverWait(self.driver, 10).until(
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
        """Click on the Become a Member menu."""
        member_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_become_member_xp))
        )
        member_menu.click()

    def click_work_style_menu(self):
        """Click on the Work Style menu."""
        work_style_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_work_style_xp))
        )
        work_style_menu.click()

    def click_entry_button(self):
        """Click on the Entry button."""
        entry_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_entry_btn_xp))
        )
        entry_btn.click()

    # Footer section actions
    def click_wantedly_link(self):
        """Click on the Wantedly link."""
        wantedly_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.wantedly_xp))
        )
        wantedly_link.click()

    def click_facebook_link(self):
        """Click on the Facebook link."""
        facebook_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.facebook_xp))
        )
        facebook_link.click()

    # Carrier section actions
    def click_carrier_recruiting_tab(self):
        """Click on the Recruiting tab."""
        recruiting_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.carrier_recruiting_xp))
        )
        recruiting_tab.click()

    def click_carrier_new_graduate_tab(self):
        """Click on the New Graduate tab."""
        new_graduate_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.carrier_new_graduate_xp))
        )
        new_graduate_tab.click()

    def click_carrier_long_term_tab(self):
        """Click on the Long Term Internship tab."""
        long_term_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.carrier_logn_term_xp))
        )
        long_term_tab.click()

    def click_job_board(self):
        """Click on a job board item."""
        job_board = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.job_board_xp))
        )
        job_board.click()

    # Team section actions
    def hover_over_team_member_card(self):
        """Hover over a team member card to check hover effects."""
        team_member_card = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.team_member_card_xp))
        )
        self.driver.actions.move_to_element(team_member_card).perform()

    # FAQ section actions
    def click_faq_card(self):
        """Click on an FAQ card."""
        faq_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.faq_card_xp))
        )
        faq_card.click()


