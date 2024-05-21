import allure
from pages.base_page import BasePage
from locators import MainLocators
from data import Urls


class MainPage(BasePage):

    @allure.step('Клик на кнопку заказать вверху стр')
    def click_on_order_1(self):
        self.click(MainLocators.button_order)
        self.expect_url_to_be("https://qa-scooter.praktikum-services.ru/order")

    @allure.step('Клик на кнопку заказать в середине')
    def click_on_order_mid(self):
        self.click(MainLocators.button_order_mid)
        self.expect_url_to_be("https://qa-scooter.praktikum-services.ru/order")

    @allure.step('Клик на кнопку куки')
    def click_cookie(self):
        self.click(MainLocators.button_cookie_accept)

    @allure.step('Клик лого самоката')
    def click_logo_samokat(self):
        self.click(MainLocators.logo_samokat_click)

    @allure.step('Клик лого яндекс')
    def click_logo_ya(self):
        self.click(MainLocators.logo_ya_click)

    def go_to_order_page(self):
        self.open_page(Urls.url + "/order")
        # После перехода на страницу заказа кликнуть на лого "Самокат",
        self.click_logo_samokat()
