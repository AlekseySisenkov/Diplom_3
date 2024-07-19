import allure
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход по ссылке')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Прокрутка до элемента')
    def skrooll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))
        self.find_element_with_wait(locator)

    @allure.step('Нажатие на элемент')
    def click_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Ввод текста в поле')
    def set_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @staticmethod
    @allure.step('Добавление номера в метку')
    def set_number_to_locator(locator_num, num):
        method, locator = locator_num
        locator = locator.format(num)
        return method, locator

    @allure.step('Перемещение элемента')
    def move_element(self, locator_from, locator_to):
        source = self.find_element_with_wait(locator_from)
        target = self.find_element_with_wait(locator_to)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    @allure.step('Перезагрузка страницы')
    def refresh_page(self):
        self.driver.refresh()

    @allure.step('Ожидание появления текста')
    def wait_text(self, text, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.text_to_be_present_in_element(locator, text))

        return self.driver.find_element(*locator)
