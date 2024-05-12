import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import MainLocators



@allure.title('Проверка заказа кнопка по середине')
@allure.description('Заполняем поля и заказываем самокат')
def test_order_mid(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    main_page.click_on_order_mid()
    order_page.order_filling_fields()
    order_page.order_samokat_fields_1()
    button = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, MainLocators.button_check_order)))
    assert button, "Кнопка посмотреть статус заказа не найдена"
