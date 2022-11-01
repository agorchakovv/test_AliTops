import pytest
from search_categories import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

#1 popular category
def test_popular_category_0(back_browser, browser):
    main_page = SearchHelper(back_browser)
    main_page.click_popular_category_0(browser)

# #2 Популярная категория
# def test_popular_category_1(back_browser, browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_popular_category_1(browser)

# #3 Популярная категория
# def test_popular_category_2(back_browser, browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_popular_category_2(browser)

# #4 Популярная категория
# def test_popular_category_3(back_browser, browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_popular_category_3(browser)

# #5 Популярная категория
# def test_popular_category_4(back_browser, browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_popular_category_4(browser)

# #6 Популярная категория
# def test_popular_category_5(back_browser, browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_popular_category_5(browser)

# #7 Популярная категория
# def test_popular_category_6(back_browser, browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_popular_category_6(browser)

# #Поиск
# def test_input(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_input()


# #Клик на фильтр 2
# def test_filter2(browser):
#     main_page = SearchHelper(browser)
#     main_page.click_filter(browser)

# #Каталог
# def test_catalog(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_catalog(back_browser)

