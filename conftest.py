import pytest
from selenium import webdriver

class Urls:
    url = 'https://qa-scooter.praktikum-services.ru/'
@pytest.fixture(scope='function')
def driver():
    # инициализируем драйвер
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get(Urls.url)

    # передаем управление тесту
    yield chrome_driver
    # после выполнения теста закрываем браузер
    chrome_driver.quit()
