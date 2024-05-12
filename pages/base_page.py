from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator, driver):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_element(self, locator, driver):
        self.driver.find_element(locator).click()
        return self.driver.find_element(*locator)

    def open_page(self, driver):
        self.driver.get(driver)
