import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import MainLocators



class OrderPage(BasePage):
    @allure.step('Ввод ФИ, города, станции, номера')
    def order_filling_fields(self):
        self.driver.find_element(By.XPATH, MainLocators.name_input).send_keys("Антон")
        self.driver.find_element(By.XPATH, MainLocators.surname_input).send_keys("Горохов")
        self.driver.find_element(By.XPATH, MainLocators.where_input).send_keys("Москва")
        self.driver.find_element(By.XPATH, MainLocators.metro).send_keys("Черкизовская")
        self.driver.find_element(By.XPATH, MainLocators.select_by_value).click()
        self.driver.find_element(By.XPATH, MainLocators.phone).send_keys("89995402422")
        self.driver.find_element(By.XPATH, MainLocators.click_next).click()


    @allure.step('Ввод даты, срока, цвета, комментария')
    def order_samokat_fields_1(self):
        self.driver.find_element(By.XPATH, MainLocators.date_input).send_keys("06.05.2024")
        self.driver.find_element(By.XPATH, MainLocators.choose_date).click()
        self.driver.find_element(By.XPATH, MainLocators.period_click).click()
        self.driver.find_element(By.XPATH, MainLocators.choose_period).click()
        self.driver.find_element(By.XPATH, MainLocators.input_color).click()
        self.driver.find_element(By.XPATH, MainLocators.input_comment).send_keys('i wanna sleep')
        self.driver.find_element(By.XPATH, MainLocators.click_order).click()
        self.driver.find_element(By.XPATH, MainLocators.order_yes_button).click()
