import requests
import time
from base_app import BasePage
from locators import Locators

class SearchHelper(BasePage):

    def popular_category_0(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (1.5)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'

    def popular_category_1(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (1.5)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'

    def popular_category_2(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (1.5)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'

    def popular_category_3(self, browser):

        for i in range(4):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (1.5)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'

    def popular_category_4(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (1.5)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'

    def popular_category_5(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (1.5)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'

    def popular_category_6(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (1.5)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'

    # #Категории
    # def click_catalog(self, browser):

    #     for i in range(16):
    #         search_field = self.find_element(Locators.LOCATOR_CATALOG)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_CATEGORY_2_ELEMENT)[i]
    #         search_fields.click()
    #         time.sleep (2)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1
            
    # #Поиск
    # def click_input(self, browser):
    #     search_field = self.find_element(Locators.LOCATOR_INPUT)
    #     search_fields = self.find_element(Locators.LOCATOR_BUTTON_INPUT)
    #     search_field.clear()
    #     search_field.send_keys("Мужские летние шорты")
    #     search_fields.click()
    #     response = requests.head(browser.current_url)
    #     assert response.status_code == 200
