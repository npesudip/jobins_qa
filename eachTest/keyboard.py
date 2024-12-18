import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def test_keyboard_login():
USERNAME = "jobins"
PASSWORD = "g4vrh5vo5hqogd0dprfj)"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://recruit.release.jobins.net/")  
driver.maximize_window()
time.sleep(1) 

action = ActionChains(driver)
action.click()
action.send_keys_to_element(USERNAME)


    # # Wait for the popup or the body element to be visible
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    
    # # Additional wait for popup to load (this is an assumption that popup is rendered inside body)
    # time.sleep(5)

#     # Use ActionChains to simulate keyboard typing directly into the username field
#     # Since the popup is focused on the username input field, we start with the username field:
#     action = ActionChains(driver)
#     action.send_keys(USERNAME).perform()  # Enter username

#     time.sleep(1)  # Small delay to ensure the username is entered

#     # Press TAB to move to the password field
#     action.send_keys(Keys.TAB).perform()
#     time.sleep(1)  # Wait for field to switch focus

#     # Enter the password
#     action.send_keys(PASSWORD).perform()
#     time.sleep(1)  # Wait for password to be entered

#     # Press ENTER to submit the form
#     action.send_keys(Keys.ENTER).perform()

#     time.sleep(5)  # Wait for the result to be processed

#     # Verify login success (use the actual expected condition here)
#     assert "Dashboard" in driver.title  # Replace "Dashboard" with the actual title text after login
#     print("Login Successful using Popup Keyboard Interaction")

#     # Close the browser
#     driver.quit()


# # Execute the test
# if __name__ == "__main__":
#     test_keyboard_login()
