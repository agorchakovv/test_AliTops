import pytest
from search_categories import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_popular_category_0(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.popular_category_0(browser)

def test_popular_category_1(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.popular_category_1(browser)

def test_popular_category_2(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.popular_category_2(browser)

def test_popular_category_3(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.popular_category_3(browser)

def test_popular_category_4(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.popular_category_4(browser)

def test_popular_category_5(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.popular_category_5(browser)

def test_popular_category_6(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.popular_category_6(browser)

def test_catalog(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.catalog(back_browser)

def test_filter_catalog(browser):
    main_page = SearchHelper(browser)
    main_page.filter_catalog(browser)

def test_input(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.input(back_browser)
 
def test_filter_input(browser):
    main_page = SearchHelper(browser)
    main_page.filter_input(browser)



