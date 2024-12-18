from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def capture_screenshot(self, filename):
        """Capture a screenshot."""
        self.driver.save_screenshot(f"screenshots/{filename}")
        print(f"Screenshot saved: screenshots/{filename}")





