import allure
from pages.base_page import BasePage
from locators import MainLocators


class QuestionsPage(BasePage):

    @allure.step('Клик на вопросы')
    def set_question(self):
        self.click_cookie()
        self.find_element(*MainLocators.question).click()
        self.wait_and_find_element(*MainLocators.answer)
        return self.find_element(*MainLocators.answer).text

    def click_cookie(self):
        self.click(MainLocators.yes_all)
