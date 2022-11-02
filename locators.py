from selenium.webdriver.common.by import By

class Locators:
    LOCATOR_PRODUCT = (By.XPATH, '//*[@id="product_list"]/li')
    LOCATOR_COMPILATION = (By.XPATH, '//a[@id="collection_link"]')
    LOCATOR_FILTER = (By.XPATH, '//button[@id="filter_dropdown"]')
    LOCATOR_DROPDOWN = (By.XPATH, '//*[@id="dropdown_item"]/li')
    LOCATOR_POPULAR_CATEGORY_0 = (By.XPATH, '//button[@id="popular_categories_item_0"]')
    LOCATOR_POPULAR_CATEGORY_1 = (By.XPATH, '//button[@id="popular_categories_item_1"]')
    LOCATOR_POPULAR_CATEGORY_2 = (By.XPATH, '//button[@id="popular_categories_item_2"]')
    LOCATOR_POPULAR_CATEGORY_3 = (By.XPATH, '//button[@id="popular_categories_item_3"]')
    LOCATOR_POPULAR_CATEGORY_4 = (By.XPATH, '//button[@id="popular_categories_item_4"]')
    LOCATOR_POPULAR_CATEGORY_5 = (By.XPATH, '//button[@id="popular_categories_item_5"]')
    LOCATOR_POPULAR_CATEGORY_6 = (By.XPATH, '//button[@id="popular_categories_item_6"]')
    LOCATOR_INPUT = (By.XPATH, '//input[@id="search_input"]')
    LOCATOR_BUTTON_INPUT = (By.XPATH, '//button[@id="search_button"]')
    LOCATOR_FAVORITE = (By.XPATH, '//*[@id="product_list__item_0"]/div/div/button')
    LOCATOR_PRODUCTS = (By.XPATH, '//li[@id="product_list__item_0"]')
    LOCATOR_AUTHORIZATION = (By.XPATH, '//*[contains(text(), "Продолжить без авторизации")]')
    LOCATOR_CURRANCY = (By.XPATH, '//button[@id="footer_change_currancy"]')
    LOCATOR_CATALOG = (By.XPATH, '//button[@id="catalog_button"]')
    LOCATOR_CATEGORY = (By.XPATH, '//*[@id="catalog-root-menu"]/li')
    LOCATOR_CATEGORY_2_ELEMENT = (By.XPATH, '//*[@id="catalog-root-menu"]/li/a')