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
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}'

    def popular_category_1(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_1)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}'

    def popular_category_2(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_2)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}'

    def popular_category_3(self, browser):

        for i in range(3):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_3)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}'

    def popular_category_4(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_4)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}'

    def popular_category_5(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_5)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}' 

    def popular_category_6(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_6)
            search_popular_category.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}'

    def catalog(self, browser):

        for i in range(16):
            search_catalog = self.find_element(Locators.LOCATOR_CATALOG)
            search_catalog.click()
            search_element_catalog = self.find_elements(Locators.LOCATOR_ELEMENT_CATALOG)[i]
            search_element_catalog.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)} Error in url - {url}'
            
    def input(self, browser):
        search_input = self.find_element(Locators.LOCATOR_INPUT)
        search_button_search = self.find_element(Locators.LOCATOR_BUTTON_SEARCH)
        search_input.clear()
        search_input.send_keys("iPhone")
        search_button_search.click()
        time.sleep (2)
        search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'The site returned the code - {response.status_code}'
        
        for search in search_products:
            assert ("iphone" in search.text.lower()), f'Error in product - {search.text}'

    def filter_input(self,browser):

        filter  = {
            "По релевантности": "page=1",
            "Сначала: Дешевые": "sort=cheap",
            "Сначала: Дорогие": "sort=expensive",
            "По рейтингу": "sort=rating",
            "По количеству продаж": "sort=sale",
            "По скидке": "sort=discount"
        }
        
        for i in range(6):
            search_filter = self.find_element(Locators.LOCATOR_FILTER)
            search_filter.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown_text = search_dropdown.text
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 60, f'Amount of elements - {len(search_products)}'
            assert (filter[search_dropdown_text] in url), f'Error in url - {url}'   

    def filter_catalog(self,browser):

        filter  = {
            "По умолчанию": "page=1",
            "Сначала: Дешевые": "sort=cheap",
            "Сначала: Дорогие": "sort=expensive",
            "По рейтингу": "sort=rating",
            "По количеству продаж": "sort=sale",
            "По скидке": "sort=discount"
        }
        
        for i in range(6):
            search_filter = self.find_element(Locators.LOCATOR_FILTER)
            search_filter.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown_text = search_dropdown.text
            search_dropdown.click()
            time.sleep (2)
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products)}'
            assert (filter[search_dropdown_text] in url), f'Error in url - {url}' 