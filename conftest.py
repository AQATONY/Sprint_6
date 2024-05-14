import pytest
from selenium import webdriver
from data import Urls

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
