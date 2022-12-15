import requests
import time
from base_app import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SearchHelper(BasePage):

    def popular_category_0(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_0)
            ActionChains(browser).click(search_popular_category).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen22.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen23.png")} Error in url - {url}'

    def popular_category_1(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_1)
            ActionChains(browser).click(search_popular_category).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen24.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen25.png")} Error in url - {url}'

    def popular_category_2(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_2)
            ActionChains(browser).click(search_popular_category).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen26.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen27.png")} Error in url - {url}'

    def popular_category_3(self, browser):

        for i in range(4):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_3)
            ActionChains(browser).click(search_popular_category).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen28.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen29.png")} Error in url - {url}'

    def popular_category_4(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_4)
            ActionChains(browser).click(search_popular_category).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen30.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen31.png")} Error in url - {url}'

    def popular_category_5(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_5)
            ActionChains(browser).click(search_popular_category).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen32.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen33.png")} Error in url - {url}' 

    def popular_category_6(self, browser):

        for i in range(5):
            search_popular_category = self.find_element(Locators.LOCATOR_POPULAR_CATEGORY_6)
            ActionChains(browser).click(search_popular_category).perform()
            search_dropdown = self.find_elements(Locators.LOCATOR_DROPDOWN)[i]
            ActionChains(browser).key_down(Keys.COMMAND).click(search_dropdown).perform()
            handles = browser.window_handles
            size = len(handles)

            for j in range(size):
                browser.switch_to.window(handles[j])

            search_products = self.find_elements(Locators.LOCATOR_PRODUCTS_CATALOG)
            response = requests.head(browser.current_url)
            url = browser.current_url
            # assert browser.current_url == "https://alitops.ru/category/mobilnye-telefony/smartfony-c001788", f"received url is - {browser.current_url}"
            assert response.status_code == 200, f'The site returned the code - {response.status_code, browser.save_screenshot("./screensots/screen34.png")} Error in url - {url}'
            assert len(search_products) == 70, f'Amount of elements - {len(search_products), browser.save_screenshot("./screensots/screen35.png")} Error in url - {url}'