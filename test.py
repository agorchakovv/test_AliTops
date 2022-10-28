from search import SearchHelper 
from baseApp import BasePage
import pytest

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

#Test main page
def test_main(browser):
    main_page = SearchHelper(browser)
    main_page.main_page(browser)

#Test hot compilation
def test_collection1(browser):
    main_page = SearchHelper(browser)
    main_page.click_button_collection1(browser)

# #Клик на фильтр 1
# def test_filter1(browser):
#     main_page = SearchHelper(browser)
#     main_page.click_filter(browser)

# #Бестселлеры
# def test_collection2(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_button_collection2()
#     response = requests.head(back_browser.current_url)
#     assert response.status_code == 200

# #Покупатели рекомендуют
# def test_collection3(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_button_collection3()
#     response = requests.head(back_browser.current_url)
#     assert response.status_code == 200

# #1 Популярная категория
# def test_popular_category_0(back_browser, browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_popular_category_0(browser)

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
#     response = requests.head(back_browser.current_url)
#     assert response.status_code == 200

# #Клик на фильтр 2
# def test_filter2(browser):
#     main_page = SearchHelper(browser)
#     main_page.click_filter(browser)

# #Добавление в избранное и авторизация
# def test_favorite(browser):
#     main_page = SearchHelper(browser)
#     main_page.click_favorite(browser)

# #Каталог
# def test_catalog(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_catalog(back_browser)

# #Изменение валюты
# def test_currency(back_browser):
#     main_page = SearchHelper(back_browser)
#     main_page.click_currency(back_browser)