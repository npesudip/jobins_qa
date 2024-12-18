from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class FooterObject(BasePage):
    TITLE = "JoBins Recruitment"


    '''
    Footer Section : 1. Link validation for social media icons. 2. Footer content validation.
    '''

    # locators at footer (dynamic) and response on the click action
    wantedly_xp="//a[@href='https://www.wantedly.com/companies/jobins?ref=jobins.jp']"
    wantedly_url = "https://www.wantedly.com/companies/jobins?ref=jobins.jp"
    facebook_xp="//a[@href='https://www.facebook.com/jobins.jp?ref=jobins.jp']"
    facebook_url="https://www.facebook.com/jobins.jp?ref=jobins.jp"


    wantedly_url_keyword = "wantedly"
    facebook_url_keyword="facebook"


    def __init__(self, driver):
        super().__init__(driver)

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