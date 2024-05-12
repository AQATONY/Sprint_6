import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from conftest import driver
from conftest import Urls


@allure.title('Проверка редиректов')
@allure.description('Кликаем на элементы и проверяем редирект')
def test_logo_samokat(driver):
    driver.get(Urls.url + "/order")
    main_page = MainPage(BasePage)
    main_page.click_logo_samokat()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


@allure.title('Проверка редиректов')
@allure.description('Кликаем на элементы и проверяем редирект')
def test_logo_samokat(driver):
    main_page = MainPage(BasePage)
    main_page.click_logo_ya()
    new_window = driver.window_handles[1]  # Переключаемся на новое окно
    driver.switch_to.window(new_window)
    # Проверяем URL
    assert "https://dzen.ru" in driver.current_url
