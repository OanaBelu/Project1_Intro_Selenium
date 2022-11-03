"""
This module contains shared fixtures.
"""

import selenium.webdriver
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def browser():
    # Initialize the ChromeDriver instance
    s = Service(ChromeDriverManager().install())
    browser = selenium.webdriver.Chrome(service=s)

    # Make its calls wait up to 10 seconds for elements to appear
    browser.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield browser

    # Quit the WebDriver instance for the cleanup
    browser.quit()
