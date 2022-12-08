import pytest
from search.search_main import SearchHelper 
from base_app import BasePage

#Fixture open main page
@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_main(browser):
    main_page = SearchHelper(browser)
    main_page.main_page(browser)

def test_hot_compilation(browser):
    main_page = SearchHelper(browser)
    main_page.hot_compilation(browser)

def test_bestsellers(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.bestsellers(back_browser)
 
def test_buyers_recommend(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.buyers_recommend(back_browser)

#Click on the buyers recommend filter 
def test_filter(browser):
    main_page = SearchHelper(browser)
    main_page.filter(browser)

# def test_currency(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.currency(back_browser)