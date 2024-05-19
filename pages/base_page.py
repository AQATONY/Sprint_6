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

    def click(self, locator):
        element = self.wait_and_find_element(locator, self.driver)
        element.click()

    def expect_url_to_be(self, url):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(url))

    def switch_to_new_window(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def get_current_url(self):
        return self.driver.current_url
