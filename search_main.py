import requests
import time
# from fcntl import LOCK_EX
from base_app import BasePage
from locators import Locators

#Search for elements
class SearchHelper(BasePage):

    def main_page(self, browser):
        main_page = BasePage(browser)
        main_page.go_to_site()
        search_product = self.find_elements(Locators.LOCATOR_PRODUCT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код - {response.status_code}'
        assert len(search_product) == 30, f'Количество товаров - {len(search_product)}'

    def hot_compilation(self, browser):
        search_compilation = self.find_elements(Locators.LOCATOR_COMPILATION)[0]
        search_compilation.click()
        search_product = self.find_elements(Locators.LOCATOR_PRODUCT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код - {response.status_code}'
        assert len(search_product) == 60, f'Количество товаров - {len(search_product)}'

    def bestsellers(self, browser):
        search_compilation = self.find_elements(Locators.LOCATOR_COMPILATION)[1]
        search_compilation.click()
        search_product = self.find_elements(Locators.LOCATOR_PRODUCT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код - {response.status_code}'
        assert len(search_product) == 60, f'Количество товаров - {len(search_product)}'

    def buyers_recommend(self, browser):
        search_compilation = self.find_elements(Locators.LOCATOR_COMPILATION)[2]
        search_compilation.click()
        search_product = self.find_elements(Locators.LOCATOR_PRODUCT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код - {response.status_code}'
        assert len(search_product) == 60, f'Количество товаров - {len(search_product)}'

    def filter(self,browser):
        
        for i in range(5):
            search_filter = self.find_element(Locators.LOCATOR_FILTER)
            search_filter.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown.click()
            search_product = self.find_elements(Locators.LOCATOR_PRODUCT)
            response = requests.head(browser.current_url)
            assert response.status_code == 200, f'Сайт вернул код - {response.status_code}'
            assert len(search_product) == 60, f'Количество элементов - {len(search_product)}'
            #Нужно добавить более полную проверку работы фильтрации как таковой
            
    def currency(self, browser):

        currency  = {
            "RUB": "₽",
            "USD": "$",
            "EUR": "€",
            "UAH": "₴",
            "BYR": "BYR",
            "BRL": "R$"
        }

        for i in range(6):
            search_currency = self.find_element(Locators.LOCATOR_CURRANCY)
            search_currency.click()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown_text = search_dropdown.text
            search_dropdown.click()
            time.sleep (2)
            search_product = self.find_elements(Locators.LOCATOR_PRODUCT)
            response = requests.head(browser.current_url)
            assert response.status_code == 200, f'Сайт вернул код - {response.status_code}'
            assert len(search_product) == 30, f'Количество элементов - {len(search_product)}'

            for search in search_product:
                assert (currency[search_dropdown_text.split()[0]] in search.text), f'Ошибка в продукте - {currency[search_dropdown_text]}'

