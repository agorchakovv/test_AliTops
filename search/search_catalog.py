import requests
from base_app import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SearchHelper(BasePage):

    def catalog(self, browser):

        for i in range(16):
            browser.save_screenshot("./screensots/screen1.png")
            search_catalog = self.find_element(Locators.LOCATOR_CATALOG)
            ActionChains(browser).click(search_catalog).perform()
            search_element_catalog = self.find_elements(Locators.LOCATOR_ELEMENT_CATALOG)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_element_catalog).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])
                
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen12.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen13.png")} Error in url - {url}'


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
            ActionChains(browser).click(search_filter).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_dropdown_text = search_dropdown.text
            ActionChains(browser).click(search_dropdown).perform()
            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen14.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen15.png")} Error in url - {url}'
            assert (filter[search_dropdown_text] in url), f'Error in url - {url, browser.save_screenshot("./screensots/screen16.png")}' 