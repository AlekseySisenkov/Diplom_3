import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Переходим на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def go_to_recovery_password(self):
        self.click_element(LoginPageLocators.BUTTON_RECOVERY_PASS)
