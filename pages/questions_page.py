import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainLocators


class Questions(BasePage):

    @allure.step('Клик на вопросы')
    def set_question(self, i):
        self.click_cookie()
        MainLocators.question = (By.ID, f'accordion__heading-{i}')
        MainLocators.answer = (By.ID, f'accordion__panel-{i}')
        self.driver.find_element(*MainLocators.question).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainLocators.answer))
        return self.driver.find_element(*MainLocators.answer).text

    def click_cookie(self):
        self.driver.find_element(By.XPATH, MainLocators.yes_all).click()
