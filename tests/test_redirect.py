import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from conftest import driver
from conftest import Urls


@allure.feature('Тесты редиректов')  # Добавляем общую категорию теста
class TestLogoRedirects:  # Объединяем тесты в класс
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
        base_page = BasePage(BasePage)
        base_page.switch_to_new_window()
        assert "https://dzen.ru" in driver.current_url
