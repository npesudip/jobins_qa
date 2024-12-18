import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import CONFIG

class DriverManager:
    def __init__(self):
        self.base_url = CONFIG["base_url"]
        self.username = CONFIG["username"]
        self.password = CONFIG["password"]
        self.driver = None
        self.screenshot_dir = os.path.abspath("screenshots")
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def initialize_driver(self):
        """Initialize WebDriver and bypass authentication."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        auth_url = f"https://{self.username}:{self.password}@{self.base_url}"
        print(f"Loading URL: {auth_url}")
        self.driver.get(auth_url)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def capture_screenshot(self, filename):
        """Save a screenshot to the screenshots directory."""
        screenshot_path = os.path.join(self.screenshot_dir, filename)
        self.driver.save_screenshot(screenshot_path)

    def quit_driver(self):
        """Quit WebDriver."""
        if self.driver:
            self.capture_screenshot("final_state.png")
            print(f"Closing WebDriver. Title was: {self.driver.title}")
            self.driver.quit()

    def get_driver(self):
        """Return the initialized WebDriver instance."""
        return self.driver
