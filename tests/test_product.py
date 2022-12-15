import pytest
from search.search_product import SearchHelper 
from base_app import BasePage

#Fixture open main page
@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_poduct(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.product(back_browser)

def test_button_reviews(browser):
    main_page = SearchHelper(browser)
    main_page.more_reviews(browser)