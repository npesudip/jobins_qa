import sys
import os

import pytest
from utils.driver_manager import DriverManager

# Correctly adjust sys.path to include the utils directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))


@pytest.fixture(scope="session")
def driver():
    """Fixture to initialize WebDriver."""
    driver_manager = DriverManager()
    driver_manager.initialize_driver()

    driver = driver_manager.get_driver()
    driver.capture_screenshot = driver_manager.capture_screenshot  # Attach screenshot method

    yield driver

    driver_manager.quit_driver()

    
def pytest_runtest_makereport(item, call):
    """Automatically capture screenshots on test failures."""
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_path = f"screenshots/{item.name}_failure.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot of failure saved: {screenshot_path}")


