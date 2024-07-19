import allure

from locators.personal_cabinet_page_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage


class PersonalCabinetPage(BasePage):

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

    @allure.step('Берем номер заказа из раздела «История заказов»')
    def make_list_history_orders(self):

        return self.get_text(PersonalCabinetPageLocators.NUM_ORDERS)
