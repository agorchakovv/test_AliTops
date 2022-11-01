import requests
import time
from base_app import BasePage
from locators import Locators

#Search for elements
class SearchHelper(BasePage):

    #Click on 1 popular category and its subcategories
    def click_popular_category_0(self, browser):

        i = 0

        for i in range(5):
            search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            search_field.click()
            search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            search_fields.click()
            search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
            time.sleep (1)
            response = requests.head(browser.current_url)
            assert response.status_code == 200
            assert len(search_elements) == 70
            i += 1

    # #Click on 2 popular category and its subcategories
    # def click_popular_category_1(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_1)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
    #         time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         assert len(search_elements) == 70
    #         i += 1

    # #Click on 3 popular category and its subcategories
    # def click_popular_category_2(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_2)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
    #         time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         assert len(search_elements) == 70
    #         i += 1

    # #Click on 4 popular category and its subcategories
    # def click_popular_category_3(self, browser):

    #     i = 0

    #     for i in range(4):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_3)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
    #         time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         assert len(search_elements) == 70
    #         i += 1

    # #Click on 5 popular category and its subcategories
    # def click_popular_category_4(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_4)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
    #         time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         assert len(search_elements) == 70
    #         i += 1

    # #Click on 6 popular category and its subcategories
    # def click_popular_category_5(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_5)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
    #         time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         assert len(search_elements) == 70
    #         i += 1

    # #Click on 7 popular category and its subcategories
    # def click_popular_category_6(self, browser):

    #     i = 0

    #     for i in range(5):
    #         search_field = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_6)
    #         search_field.click()
    #         search_fields = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
    #         search_fields.click()
    #         search_elements = self.find_elements(Locators.LOCATOR_ELEMENT)
    #         time.sleep (1)
    #         response = requests.head(browser.current_url)
    #         assert response.status_code == 200
    #         assert len(search_elements) == 70
    #         i += 1

    # #Категории
    # def click_catalog(self, browser):
    #     i = 0

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
