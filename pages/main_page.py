import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls

driver = webdriver.Chrome()
driver.get(Urls.url)


class order(BasePage):
    button_order = "//button[contains(@class,'Button_Button__ra12g')]"  # локатор для кнопки "Заказать" вверху стр
    button_order_mid = "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')]"  # локатор для кнопки "Заказать" в середине стр
    button_cookie_accept = "//button[contains(text(),'да все привыкли')]"
    name_input = "//input[@placeholder = '* Имя']"
    surname_input = "//input[@placeholder = '* Фамилия']"
    where_input = "//input[@placeholder = '* Адрес: куда привезти заказ']"
    metro = "//input[@placeholder = '* Станция метро']"
    phone = "//input[@placeholder = '* Телефон: на него позвонит курьер']"
    select_by_value = "//div[contains(@class,'select-search__select')]/ul/li"
    click_next = "//button[contains(text(),'Далее')]"
    date_input = "//input[@placeholder = '* Когда привезти самокат']"
    choose_date = "//div[contains(@class,'react-datepicker__day react-datepicker__day--005 react-datepicker__day--selected react-datepicker__day--today react-datepicker__day--weekend')]"
    period_click = "//div[contains(@class,'Dropdown-placeholder')]"
    choose_period = "//*[contains(@class,'Dropdown-option') and contains(text(),'сутки')]"
    input_color = '//input[@id="black"]'
    input_comment = "//input[@placeholder = 'Комментарий для курьера']"
    click_order = "//*[contains(@class,'Button_Button__ra12g Button_Middle__1CSJM') and contains(text(),'Заказать')]"
    order_yes_button = "//button[contains(text(),'Да')]"  # она не нажимается

    @allure.step('Клик на кнопку заказать вверху стр')
    def click_on_order_1(self):
        self.click_cookie()
        self.driver.find_element(By.XPATH, self.button_order).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    @allure.step('Клик на кнопку заказать в середине')
    def click_on_order_mid(self):
        self.click_cookie()
        self.driver.find_element(By.XPATH, self.button_order_mid).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    @allure.step('Клик на кнопку куки')
    def click_cookie(self):
        self.driver.find_element(By.XPATH, self.button_cookie_accept).click()

    @allure.step('Ввод ФИ, города, станции, номера')
    def order_filling_fields(self):
        self.driver.find_element(By.XPATH, self.name_input).send_keys("Антон")
        self.driver.find_element(By.XPATH, self.surname_input).send_keys("Горохов")
        self.driver.find_element(By.XPATH, self.where_input).send_keys("Москва")
        self.driver.find_element(By.XPATH, self.metro).send_keys("Черкизовская")
        self.driver.find_element(By.XPATH, self.select_by_value).click()
        self.driver.find_element(By.XPATH, self.phone).send_keys("89995402422")
        self.driver.find_element(By.XPATH, self.click_next).click()

    @allure.step('Ввод даты, срока, цвета, комментария')
    def order_samokat_fields_1(self):
        self.driver.find_element(By.XPATH, self.date_input).send_keys("05.05.2024")
        self.driver.find_element(By.XPATH, self.choose_date).click()
        self.driver.find_element(By.XPATH, self.period_click).click()
        self.driver.find_element(By.XPATH, self.choose_period).click()
        self.driver.find_element(By.XPATH, self.input_color).click()
        self.driver.find_element(By.XPATH, self.input_comment).send_keys('i wanna sleep')
        self.driver.find_element(By.XPATH, self.click_order).click()
        self.driver.find_element(By.XPATH, self.order_yes_button).click()
