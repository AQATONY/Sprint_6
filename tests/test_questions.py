import allure
from pages.questions_page import QuestionsPage
import pytest
from conftest import driver


@allure.feature('Тест выпадающего списка вопросов и ответов')  # Добавляем общую категорию теста
class TestQuestionsAnswers:  # Объединяем тесты в класс
    @allure.title('Проверка вопросов')
    @allure.description('Кликаем по вопросам и смотрим ответ')
    @pytest.mark.parametrize('i, expected_result', [
        (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (1,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (2,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (5,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    def test_question(i, expected_result):
        question_page = QuestionsPage(driver)  # Инициализируем класс с передачей драйвера
        result = question_page.set_question(i)
        assert result == expected_result, f"Expected '{expected_result}', got '{result}'"
