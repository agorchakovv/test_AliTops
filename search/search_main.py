import requests
from base_app import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#Search for elements
class SearchHelper(BasePage):

    def main_page(self, browser):
        main_page = BasePage(browser)
        main_page.go_to_site()
        search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen1.png")}'
        assert len(search_products) == 30, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen2.png")}'
        #Разделить количество товаров по подборкам

    def hot_compilation(self, browser):
        search_compilation = self.find_elements(Locators.LOCATOR_COMPILATION)[0]
        search_compilation.click()
        search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen3.png")}'
        assert len(search_products) == 60, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen4.png")}'

    def bestsellers(self, browser):
        search_compilation = self.find_elements(Locators.LOCATOR_COMPILATION)[1]
        search_compilation.click()
        search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen5.png")}'
        assert len(search_products) == 60, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen6.png")}'

    def buyers_recommend(self, browser):
        search_compilation = self.find_elements(Locators.LOCATOR_COMPILATION)[2]
        search_compilation.click()
        search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen7.png")}'
        assert len(search_products) == 60, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen8.png")}'

    def filter(self,browser):

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
            ActionChains(browser).click(search_filter).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown_text = search_dropdown.text
            ActionChains(browser).click(search_dropdown).perform()
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            assert response.status_code == 200, f'The site returned the code - {response.status_code,  browser.save_screenshot("./screensots/screen9.png")} Error in url - {url}'
            assert len(search_products) == 60, f'Amount of elements - {len(search_products, browser.save_screenshot("./screensots/screen10.png"))} Error in url - {url}'
            assert (filter[search_dropdown_text] in url), f'Error in url - {url, browser.save_screenshot("./screensots/screen11.png")}'  

    # def currency(self, browser):

    #     currency  = {
    #         "RUB": "₽",
    #         "USD": "$",
    #         "EUR": "€",
    #         "UAH": "₴",
    #         "BYR": "BYR",
    #         "BRL": "R$"
    #     }

    #     for i in range(6):
    #         search_currency = self.find_element(Locators.LOCATOR_CURRANCY)
    #         search_currency.click()
    #         search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_dropdown_text = search_dropdown.text
    #         search_dropdown.click()
    #         time.sleep (2)
    #         search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200, f'The site returned the code - {response.status_code}'
    #         assert len(search_products) == 30, f'Amount of elements - {len(search_products)}'

    #         for search in search_products:
    #             assert (currency[search_dropdown_text.split()[0]] in search.text), f'Error in product - {search.text}'