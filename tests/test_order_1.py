import allure
from data import Urls
from selenium import webdriver
from pages.main_page import order


@allure.title('Проверка заказа кнопка справа вверху')
@allure.description('Заполняем поля и заказываем самокат')
def test_order_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.url)
    order_page = order(driver)
    order_page.click_on_order_1()
    input_page = order(driver)
    input_page.order_filling_fields()
    input_page.order_samokat_fields_1()

