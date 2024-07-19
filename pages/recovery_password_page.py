import allure

from data import payload
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):

    @allure.step('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def check_go_to_recovery_password(self):
        return self.find_element_with_wait(RecoveryPasswordPageLocators.INPUT_EMAIL)

    @allure.step('Вводим почту')
    def input_email(self):
        self.set_text_to_field(RecoveryPasswordPageLocators.INPUT_EMAIL, payload['email'])

    @allure.step('Нажимаем кнопку «Восстановить»')
    def click_recovery(self):
        self.click_element(RecoveryPasswordPageLocators.BUTTON_RECOVERY)

    @allure.step('Проверка нажатия кнопки «Восстановить»')
    def check_click_recovery(self):
        return self.find_element_with_wait(RecoveryPasswordPageLocators.IS_NOT_ACTIVE_PASSWORD)

    @allure.step('Нажимаем кнопку «показать/скрыть пароль»')
    def click_view_password(self):
        self.click_element(RecoveryPasswordPageLocators.BUTTON_VIEW_PASS)

    @allure.step('Проверяем, что поле «Пароль» стало активным')
    def check_view_password(self):
        if ('input_status_active' in self.find_element_with_wait(RecoveryPasswordPageLocators.IS_NOT_ACTIVE_PASSWORD)
                .get_attribute("class")):
            return True
        else:
            return False
