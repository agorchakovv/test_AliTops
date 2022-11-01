import pytest
from search_main import SearchHelper 
from base_app import BasePage

#Fixture open main page
@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

#Test main page
def test_main(browser):
    main_page = SearchHelper(browser)
    main_page.main_page(browser)

#Click on the hot compilation
def test_collection1(browser):
    main_page = SearchHelper(browser)
    main_page.click_button_collection1(browser)

#Click on the compilation filter 
def test_filter1(browser):
    main_page = SearchHelper(browser)
    main_page.click_filter(browser)

#Click on the bestellers compilation
def test_collection2(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.click_button_collection2(back_browser)
 
#Click on the buyers recommend compilation
def test_collection3(back_browser):
    main_page = SearchHelper(back_browser)
    main_page.click_button_collection3(back_browser)

# #Currency change
# def test_currency(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_currency(back_browser)