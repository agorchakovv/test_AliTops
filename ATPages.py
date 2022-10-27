# from fcntl import LOCK_EX
import requests
import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Locators
class Locators:
    
    LOCATOR_COLLECTION = (By.XPATH, '//a[@id="collection_link"]')
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
    LOCATOR_PRODUCT = (By.XPATH, '//li[@id="product_list__item_0"]')
    LOCATOR_AUTHORIZATION = (By.XPATH, '//*[contains(text(), "Продолжить без авторизации")]')
    LOCATOR_CURRANCY = (By.XPATH, '//button[@id="footer_change_currancy"]')
    LOCATOR_CATALOG = (By.XPATH, '//button[@id="catalog_button"]')
    LOCATOR_CATEGORY = (By.XPATH, '//*[@id="catalog-root-menu"]/li')
    LOCATOR_CATEGORY_2_ELEMENT = (By.XPATH, '//*[@id="catalog-root-menu"]/li/a')

#Search for elements
class SearchHelper(BasePage):

    #Hot compilation
    def click_button_collection1(self):
        search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[0]
        search_field.click()

    # #Клик на фильтр и выпадающий список
    # def click_filter(self,browser):
        
    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_FILTER)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1
              
    # #Бестселлеры
    # def click_button_collection2(self):
    #     search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[1]
    #     search_field.click()

    # #Покупатели рекомендуют
    # def click_button_collection3(self):
    #     search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[2]
    #     search_field.click()

    # #Клик на 1 популярную категорию и ее подкатегории
    # def click_popular_category_0(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1

    # #Клик на 2 популярную категорию и ее подкатегории
    # def click_popular_category_1(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_1)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1

    # #Клик на 3 популярную категорию и ее подкатегории
    # def click_popular_category_2(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_2)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1

    # #Клик на 4 популярную категорию и ее подкатегории
    # def click_popular_category_3(self, browser):

    #     i = 0

    #     for i in range(4):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_3)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1

    # #Клик на 5 популярную категорию и ее подкатегории
    # def click_popular_category_4(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_4)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1

    # #Клик на 6 популярную категорию и ее подкатегории
    # def click_popular_category_5(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_5)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1

    # #Клик на 7 популярную категорию и ее подкатегории
    # def click_popular_category_6(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_6)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1
            
    # #Поиск
    # def click_input(self):
    #     search_field = self.find_element(Locators.LOCATOR_INPUT)
    #     search_fields = self.find_element(Locators.LOCATOR_BUTTON_INPUT)
    #     search_field.clear()
    #     search_field.send_keys("Мужские летние шорты")
    #     search_fields.click()

    # #Добавление в избранное
    # def click_favorite(self, browser):
    #     action = ActionChains(browser)
    #     search_field = self.find_element(Locators.LOCATOR_PRODUCT)
    #     search_field1 = self.find_element(Locators.LOCATOR_FAVORITE)
    #     search_field2 = self.find_element(Locators.LOCATOR_AUTHORIZATION)
    #     action.move_to_element(search_field)
    #     action.click(search_field1)
    #     action.pause(2)
    #     print("Element is visible? " + str(search_field2.is_displayed()))
    #     action.click(search_field2)
    #     action.perform()
    #     time.sleep (2)
        
    # #Изменение валюты
    # def click_currency(self, browser):
    #     i = 0

    #     for i in range(6):
    #         search_field = self.find_element(Locators.LOCATOR_CURRANCY)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1

    # #Категории
    # def click_catalog(self, browser):
    #     i = 0

    #     for i in range(16):
    #         search_field = self.find_element(Locators.LOCATOR_CATALOG)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_CATEGORY_2_ELEMENT)[i]
    #         search_fields.click()
    #         time.sleep (0.5)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1