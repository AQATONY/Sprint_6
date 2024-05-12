import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainLocators





class MainPage(BasePage):


    @allure.step('Клик на кнопку заказать вверху стр')
    def click_on_order_1(self):
        self.driver.find_element(By.XPATH, MainLocators.button_order).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    @allure.step('Клик на кнопку заказать в середине')
    def click_on_order_mid(self):
        self.driver.find_element(By.XPATH, MainLocators.button_order_mid).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    @allure.step('Клик на кнопку куки')
    def click_cookie(self):
        self.driver.find_element(By.XPATH, MainLocators.button_cookie_accept).click()

    @allure.step('Клик лого самоката')
    def click_logo_samokat(self):
        self.driver.find_element(By.XPATH, MainLocators.logo_samokat_click).click()

    @allure.step('Клик лого яндекс')
    def click_logo_ya(self):
        self.driver.find_element(By.XPATH, MainLocators.logo_ya_click).click()





