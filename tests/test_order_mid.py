import allure
from data import Urls
from selenium import webdriver
from pages.main_page import order
import time


@allure.title('Проверка заказа кнопка по середине')
@allure.description('Заполняем поля и заказываем самокат')
def test_order_mid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.url)
    order_page = order(driver)
    order_page.click_on_order_mid()
    input_page = order(driver)
    input_page.order_filling_fields()
    input_page.order_samokat_fields_1()
    time.sleep(5)
