import allure
from selenium.webdriver import Keys

from data import set_parameter
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Переходим по клику на «Личный кабинет»')
    def go_to_personal_cabinet(self):
        self.click_element(MainPageLocators.PERSONAL_CABINET)

    @allure.step('Переходим по клику на «Конструктор»')
    def go_to_constructor(self):
        self.click_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Проверка перехода по клику на «Конструктор»')
    def check_go_to_constructor(self):
        return self.find_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Переходим по клику на «Лента заказов»')
    def go_to_orders_feed(self):
        self.click_element(MainPageLocators.BUTTON_ORDERS_FEED)

    @allure.step('Проверка перехода по клику на «Лента заказов»')
    def check_go_to_orders_feed(self):
        return self.find_element_with_wait(MainPageLocators.TEXT_ORDERS_FEED)

    @allure.step('Открываем окно «Детали ингредиента»')
    def open_pop_up_window_ingredient(self, locator, num):
        self.skrooll_to_element(self.set_number_to_locator(set_parameter(locator), num))
        self.click_element(self.set_number_to_locator(set_parameter(locator), num))

    @allure.step('Нажимаем на крестик всплывающего окна ингредиента')
    def click_close_pop_up_window_ingredient(self):
        self.click_element(MainPageLocators.BUTTON_INGREDIENT_WINDOW_CLOSE)

    @allure.step('Проверяем закрытия всплывающего окна ингредиента')
    def check_click_close_pop_up_window_ingredient(self):
        if ('Modal_modal_opened' in self.find_element_with_wait(MainPageLocators.DETAILS_INGREDIENT)
                .get_attribute("class")):
            return False
        else:
            return True

    @allure.step('Запоминаем счетчик ингредиента')
    def get_count_ingredient(self, locator, num):
        self.skrooll_to_element(self.set_number_to_locator(set_parameter(locator), num))
        return self.get_text(self.set_number_to_locator(set_parameter(locator), num))

    @allure.step('Добавляем игредиент в заказ')
    def adding_order(self, locator, num):
        self.move_element(self.set_number_to_locator(set_parameter(locator), num), MainPageLocators.FIELD_ORDER)
        return self.get_text(
            self.set_number_to_locator(set_parameter(locator), num))

    @allure.step('Оформляем заказ')
    def click_make_order(self):
        self.click_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Закрываем окно заказа')
    def close_make_order(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_CLOSE_MAKE_ORDER).send_keys(Keys.ESCAPE)

    @allure.step('Проверка оформления заказа')
    def check_make_order(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_PROCESSED)

    @allure.step('Сохраняем номер заказа')
    def save_number_order(self):
        self.find_element_with_wait(MainPageLocators.WAIT_NUMBER_ORDER)

        return self.get_text(MainPageLocators.NUMBER_ORDER)

    @allure.step('Проверка выхода из аккаунта')
    def check_exit_account(self):
        return self.find_element_with_wait(MainPageLocators.BUTTON_INPUT)
