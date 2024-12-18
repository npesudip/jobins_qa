import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus

# Ensure chromedriver is in PATH
driver = webdriver.Chrome()
driver.maximize_window()

# Basic Auth credentials embedded in URL (escaping special characters)
username = "jobins"
password = "g4vrh5vo5hqogd0dprfj"
base_url = "recruit.release.jobins.net/"
encoded_password = quote_plus(password)  # Escape special characters in password
url = f"https://{username}:{encoded_password}@{base_url}"
print(f"URL with Basic Authentication: {url}")

try:
    driver.get(url)
    print("Page loaded with Basic Authentication")

    # Ensure the screenshots folder exists (relative to this script)
    screenshot_dir = os.path.abspath("../jobins/screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    # Debug: Wait for page load and capture screenshot
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    screenshot_path = os.path.join(screenshot_dir, "initial_auth_page.png")
    driver.save_screenshot(screenshot_path)
    print(f"Initial screenshot saved at: {screenshot_path}")
    time.sleep(1)

    # List of menu items and their expected URLs
    menu_items = [
        ("ホーム", "https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/"),
        ("JoBinsについて", "https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/about-us"),
        ("メンバー紹介", "https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/team-member"),
        ("働き方", "https://jobins:g4vrh5vo5hqogd0dprfj@recruit.release.jobins.net/working")
    ]

    for menu_text, expected_url in menu_items:
        try:
            # Find the menu item
            menu = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, menu_text))
            )
            print(f"Clicking on: {menu.text}")
            menu.click()

            # Wait for the page to load and get the new URL
            WebDriverWait(driver, 10).until(
                EC.url_changes(driver.current_url)
            )
            new_url = driver.current_url

            # Assert that the new URL matches the expected URL
            assert new_url == expected_url, f"Expected URL: {expected_url}, but got: {new_url}"
            print(f"Successfully navigated to: {new_url}")

            # Optional delay for stability
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred while clicking on '{menu_text}': {e}")
            print(f"Current URL: {driver.current_url}")
            # Capture a screenshot of the error state
            error_screenshot_path = os.path.join(screenshot_dir, f"error_state_{menu_text}.png")
            driver.save_screenshot(error_screenshot_path)
            print(f"Error screenshot saved at: {error_screenshot_path}")
            continue  # Continue with the next menu item

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Debug: Capture final state
    final_screenshot_path = os.path.join(screenshot_dir, "final_state_auth.png")
    driver.save_screenshot(final_screenshot_path)
    title = driver.title
    print(f"Title: {title}")
    print(f"Final screenshot saved at: {final_screenshot_path}")
    driver.quit()
