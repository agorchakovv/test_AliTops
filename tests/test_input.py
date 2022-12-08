import pytest
from search.search_input import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_input(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.input(back_browser)
 
def test_filter_input(browser):
    main_page = SearchHelper(browser)
    main_page.filter_input(browser)