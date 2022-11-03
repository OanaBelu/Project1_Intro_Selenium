from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:

    URL = "https://duckduckgo.com/"
    LOGO_IMAGE = (By.ID, "logo_homepage_link")
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.ID, "search_button_homepage")
    HELP_LINK = (By.LINK_TEXT, 'Help Spread DuckDuckGo!')
    DOWN_IMAGE_ARROW = (By.CLASS_NAME, "onboarding-ed__arrow-teaser__alpinist")
    #  si cele 3 butoane de sus din pagina

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get(self.URL)

    def is_logo_imagine_displayed(self):
        return self.browser.find_element(*self.LOGO_IMAGE).is_displayed()

    def insert_search_input(self,text):
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(text)

    def click_search_button(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def is_help_link_displayed(self):
        return self.browser.find_element(*self.HELP_LINK).is_displayed()

    def is_down_imagine_arrow_displayed(self):
        return self.browser.find_element(*self.DOWN_IMAGE_ARROW).is_displayed()

#     si metoda help link click si logo imagine click plus 3 metode ptr cele 3 butoane de sus

