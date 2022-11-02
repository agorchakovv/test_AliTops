import requests
import time
# from fcntl import LOCK_EX
from base_app import BasePage
from locators import Locators
# from selenium.webdriver.common.action_chains import ActionChains

#Search for elements
class SearchHelper(BasePage):

    #Main page
    def main_page(self, browser):
        main_page = BasePage(browser)
        main_page.go_to_site()
        search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код {response.status_code}'
        assert len(search_elements) == 30, f'Количество элементов {len(search_elements)}'

    #Hot compilation
    def click_button_collection1(self, browser):
        search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[0]
        search_field.click()
        search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код {response.status_code}'
        assert len(search_elements) == 60, f'Количество элементов {len(search_elements)}'

    #Bestsellers
    def click_button_collection2(self, browser):
        search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[1]
        search_field.click()
        search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код {response.status_code}'
        assert len(search_elements) == 60, f'Количество элементов {len(search_elements)}'

    #Buyers recommend
    def click_button_collection3(self, browser):
        search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[2]
        search_field.click()
        search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'Сайт вернул код {response.status_code}'
        assert len(search_elements) == 60, f'Количество элементов {len(search_elements)}'

    #Click on the filter and dropdown list
    def click_filter(self,browser):
        
        for i in range(5):
            search_field = self.find_element(Locators.LOCATOR_FILTER)
            search_field.click()
            search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_fields.click()
            search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
            response = requests.head(browser.current_url)
            assert response.status_code == 200, f'Сайт вернул код {response.status_code}'
            assert len(search_elements) == 60, f'Количество элементов {len(search_elements)}'
            

    #Currency change
    def click_currency(self, browser):

        currency  = {
            "RUB": "₽",
            "USD": "$",
            "EUR": "€",
            "UAH": "₴",
            "BYR": "BYR",
            "BRL": "R$"
        }

        for i in range(6):
            search_field = self.find_element(Locators.LOCATOR_CURRANCY)
            search_field.click()
            search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_fields_text = search_fields.text
            search_fields.click()
            time.sleep (2)
            search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
            # print(search_elements[0].text)
            response = requests.head(browser.current_url)
            assert response.status_code == 200, f'Сайт вернул код {response.status_code}'
            assert len(search_elements) == 30, f'Количество элементов {len(search_elements)}'

            for search in search_elements:
                assert (currency[search_fields_text.split()[0]] in search.text), f'Ошибка в елементе {currency[search_fields_text]}'

