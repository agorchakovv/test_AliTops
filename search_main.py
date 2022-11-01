import requests
# import time
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
        assert response.status_code == 200
        assert len(search_elements) == 30

    #Hot compilation
    def click_button_collection1(self, browser):
        search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[0]
        search_field.click()
        search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200
        assert len(search_elements) == 60

    #Bestsellers
    def click_button_collection2(self, browser):
        search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[1]
        search_field.click()
        search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200
        assert len(search_elements) == 60

    #Buyers recommend
    def click_button_collection3(self, browser):
        search_field = self.find_elements(Locators.LOCATOR_COLLECTION)[2]
        search_field.click()
        search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
        response = requests.head(browser.current_url)
        assert response.status_code == 200
        assert len(search_elements) == 60

    #Click on the filter and dropdown list
    def click_filter(self,browser):
        
        i = 0

        for i in range(5):
            search_field = self.find_element(Locators.LOCATOR_FILTER)
            search_field.click()
            search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_fields.click()
            search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
            response = requests.head(browser.current_url)
            assert response.status_code == 200
            assert len(search_elements) == 60
            i += 1

    # #Currency change
    # def click_currency(self, browser):

    #     i = 0

    #     for i in range(6):
    #         search_field = self.find_element(Locators.LOCATOR_CURRANCY)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         # time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         i += 1