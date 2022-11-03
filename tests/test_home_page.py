from pages.home_page import HomePage
from time import sleep

def test_home_page(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    sleep(5)
    assert home_page.is_logo_imagine_displayed() , "Logo Is Not Displayed"
    # assert home_page.is_down_imagine_arrow_displayed() , "Down Imagine Is Not Displayed"
    # assert home_page.is_help_link_displayed() , "Help Link Is Not Displayed"

def test_search_functionality(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    sleep(2)
    home_page.insert_search_input("panda")
    home_page.click_search_button()

# assert ca toate rezultate contin cuvantul "panda"
# se salveaza cu find_elements
