import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import Urls
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get(Urls.url)


class Questions(BasePage):
    QUESTION1 = "(By.ID, *accordion__heading-0*)"
    ANS_Q1 = "(By.ID, *accordion__panel-0*)"
    QUESTION2 = "(By.ID, *accoridon__heading-1*)"
    ANS_Q2 = "(By.ID, *accordion__panel-1*)"
    QUESTION3 = "(By.ID, *accordion__heading-2*)"
    ANS_Q3 = "(By.ID, *accordion__panel-2*)"
    QUESTION4 = "(By.ID, *accordion__heading-3*)"
    ANS_Q4 = "(By.ID, *accordion__panel-3*)"
    QUESTION5 = "(By.ID, *accordion__heading-4*)"
    ANS_Q5 = "(By.ID, *accordion__panel-4*)"
    QUESTION6 = "(By.ID, *accordion__heading-5*)"
    ANS_Q6 = "(By.ID, *accordion__panel-5*)"
    QUESTION7 = "(By.ID, *accordion__heading-6*)"
    ANS_Q7 = "(By.ID, *accordion__panel-6*)"
    QUESTION8 = "(By.ID, *accordion__heading-7*)"
    ANS_Q8 = "(By.ID, *accordion__panel-7*)"
    Question = "(By.ID, *accordion__heading-{number}*)"
    Answer = "(By.ID, *accordion__panel-{number}*)"

    @allure.step('Клик на вопросы')
    def set_question(self, i):
        self.click_cookie()
        question = (By.ID, f'accordion__heading-{i}')
        answer = (By.ID, f'accordion__panel-{i}')
        self.driver.find_element(*question).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer))
        return self.driver.find_element(*answer).text

    def click_cookie(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(),'да все привыкли')]").click()