import requests
from base_app import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains


#Search for elements
# class SearchHelper(BasePage):

#     # #Добавление в избранное
#     # def click_favorite(self, browser):
#     #     action = ActionChains(browser)
#     #     search_field = self.find_element(Locators.LOCATOR_PRODUCT)
#     #     search_field1 = self.find_element(Locators.LOCATOR_FAVORITE)
#     #     search_field2 = self.find_element(Locators.LOCATOR_AUTHORIZATION)
#     #     action.move_to_element(search_field)
#     #     action.click(search_field1)
#     #     action.pause(2)
#     #     print("Element is visible? " + str(search_field2.is_displayed()))
#     #     action.click(search_field2)
#     #     action.perform()
#     #     time.sleep (2)