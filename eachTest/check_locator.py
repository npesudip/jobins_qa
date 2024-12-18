import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

# Basic Auth credentials embedded in URL
username = "jobins"
password = "g4vrh5vo5hqogd0dprfj"
base_url = "recruit.release.jobins.net/"
url = f"https://{username}:{password}@{base_url}"

# Define the navigation menu items using meaningful variables
home_lt = "ホーム"
about_lt = "JoBinsについて"
become_member_lt = "メンバー紹介"
work_style_lt = "働き方"

try:
    driver.get(url)
    print("Page loaded with Basic Authentication")

    # Wait for the page to fully load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print("Page loaded successfully.")

    # Define locators to validate
    locators = {
        "menu_home": "//span[contains(@class,'border-[#03275A] font-bold')]",
        "menu_about": "//span[contains(@class,'text-[#03275A] border-transparent') and contains(text(),'JoBinsについて')]",
        "menu_become_member": "//span[contains(text(), 'メンバー紹介')]",
        "menu_work_style": "//span[contains(text(), '働き方')]",
        "menu_entry_btn_xp":"//span[text()='エントリー']",
        "wantedly": "//a[@href='https://www.wantedly.com/companies/jobins?ref=jobins.jp']",
        "facebook": "//a[@href='https://www.facebook.com/jobins.jp?ref=jobins.jp']",
        "carrier_recruiting": "//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, 'キャリア採用') and @role='tab']",
        "carrier_new_graduate": "//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, '新卒採用') and @role='tab']",
        "carrier_long_term": "//button[contains(@id, 'radix-') and contains(@id, '-trigger-') and contains(@aria-controls, '長期インターン採用') and @role='tab']",
        "job_board": "//h4[contains(@class, 'text-sm') and text()='システムエンジニア']",
        "team_member_card": "//div[contains(@class, 'z-[1]') and contains(@class, 'group-hover:opacity-100') and contains(@class, 'absolute')]",
        "faq_card": "//div[contains(@class, 'z-[1]') and contains(@class, 'group-hover:opacity-100') and contains(@class, 'absolute')]",
    }

    # Check if elements are valid
    results = {}
    for name, xpath in locators.items():
        try:
            # Wait for the element to be present in the DOM
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            results[name] = "Valid Locator"
        except Exception as e:
            results[name] = f"Invalid Locator: {e}"

    # Print results
    for name, status in results.items():
        print(f"{name}: {status}")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()
