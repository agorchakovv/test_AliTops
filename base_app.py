from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    #Init driver and get base url
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://alitops.ru/"

    #Open base url
    def go_to_site(self):
        return self.driver.get(self.base_url)

    #Explicit waits for finding an element by locator
    def find_element(self, locator,time=5):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=5):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")