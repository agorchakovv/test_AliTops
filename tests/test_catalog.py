import pytest
from search.search_catalog import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_catalog(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.catalog(back_browser)

def test_filter_catalog(browser):
    main_page = SearchHelper(browser)
    main_page.filter_catalog(browser)