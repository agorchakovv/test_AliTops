import requests
from base_app import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SearchHelper(BasePage):

    def input(self, browser):
        search_input = self.find_element(Locators.LOCATOR_INPUT)
        search_button_search = self.find_element(Locators.LOCATOR_BUTTON_SEARCH)
        search_input.clear()
        search_input.send_keys("iPhone")
        ActionChains(browser).key_down(Keys.COMMAND).click(search_button_search).perform()
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
            ActionChains(browser).click(search_filter).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown_text = search_dropdown.text
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS)
            response = requests.head(browser.current_url)
            url = browser.current_url
            assert response.status_code == 200, f'The site returned the code - {response.status_code}'
            assert len(search_products) == 60, f'Amount of elements - {len(search_products)}'
            assert (filter[search_dropdown_text] in url), f'Error in url - {url}'   