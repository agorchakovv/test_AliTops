import requests
import time
from base_app import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SearchHelper(BasePage):

    def product (self, browser):
        search_products_compilation = self.find_element(Locators.LOCATOR_PRODUCTS_COMPILATION)
        search_products_compilation.click()
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        search_reviews = self.find_elements(Locators.LOCATOR_REVIEWS)
        search_schedule = self.find_elements(Locators.LOCATOR_SCHEDULE)
        search_product_shufffle  = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
        search_link_category1 = self.find_elements(Locators.LOCATOR_LINK_CATEGORY1)
        search_link_category2 = self.find_elements(Locators.LOCATOR_LINK_CATEGORY2)
        response = requests.head(browser.current_url)
        assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen36.png")}'
        assert len(search_reviews) != 0, f'No reviews, {browser.save_screenshot("./screensots/screen37.png")}'
        assert len(search_schedule) != 0, f'No schedule, {browser.save_screenshot("./screensots/screen38.png")}'
        assert len(search_product_shufffle) == 10, f'Amount shuffle products - {len(search_product_shufffle), browser.save_screenshot("./screensots/screen39.png")}'
        assert len(search_link_category1) == 4, f'Amount of link - {len(search_link_category1), browser.save_screenshot("./screensots/screen40.png")}'
        assert len(search_link_category2) == 3, f'Amount of link - {len(search_link_category2), browser.save_screenshot("./screensots/screen41.png")}'

    def more_reviews (self, browser):
        search_button_reviews = self.find_element(Locators.LOCATOR_BUTTON_REVIEWS)
        search_button_reviews.click()
        time.sleep(1)
        search_reviews = self.find_elements(Locators.LOCATOR_REVIEWS)
        assert len(search_reviews) >= 40, f'Amount of reviews{len(search_reviews), browser.save_screenshot("./screensots/screen37.png")}'

