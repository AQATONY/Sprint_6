import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver
from locators import MainLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@allure.title('Проверка заказа кнопка справа вверху')
@allure.description('Заполняем поля и заказываем самокат')
def test_order_1(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    main_page.click_on_order_1()
    order_page.order_filling_fields()
    order_page.order_samokat_fields_1()
    button = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, MainLocators.button_check_order)))
    assert button, "Кнопка посмотреть статус заказа не найдена"
