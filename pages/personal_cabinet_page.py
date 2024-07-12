import allure

from data import set_parameter
from locators.feed_page_locators import HistoryOrdersLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_cabinet_page_locators import PersonalCabinetPageLocators
from pages.main_page import MainPage


class PersonalCabinetPage(MainPage):
    @allure.step('Переходим по клику на «Личный кабинет»')
    def go_to_personal_cabinet(self):
        self.click_element(PersonalCabinetPageLocators.PERSONAL_CABINET)

    @allure.step('Проверка перехода по клику на «Личный кабинет»')
    def check_go_to_personal_cabinet(self):
        return self.find_element_with_wait(PersonalCabinetPageLocators.HISTORY_ORDERS)

    @allure.step('Переходим по клику на «История заказов»')
    def go_to_history_orders(self):
        self.click_element(PersonalCabinetPageLocators.HISTORY_ORDERS)

    @allure.step('Проверка перехода по клику на «История заказов»')
    def check_go_to_history_orders(self):
        if ('Account_link_active' in self.find_element_with_wait(PersonalCabinetPageLocators.HISTORY_ORDERS)
                .get_attribute("class")):
            return True
        else:
            return False

    @allure.step('Выходим из аккаунта')
    def exit_account(self):
        self.click_element(PersonalCabinetPageLocators.BUTTON_OUTPUT)

    @allure.step('Проверка выхода из аккаунта')
    def check_exit_account(self):
        return self.find_element_with_wait(MainPageLocators.BUTTON_INPUT)
