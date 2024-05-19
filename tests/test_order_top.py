import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver


@allure.feature('Заказ самоката по клику на кнопку вверху страницы')  # Добавляем общую категорию теста
class TestOrderTop:  # Объединяем тесты в класс
    @allure.title('Проверка заказа кнопка справа вверху')
    @allure.description('Заполняем поля и заказываем самокат')
    def test_order_button_at_the_top_of_the_page(driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_order_1()
        order_page.order_filling_fields()
        order_page.order_samokat_fields_1()
        button = order_page.wait_of_alert()
        assert button, "Кнопка посмотреть статус заказа не найдена"
