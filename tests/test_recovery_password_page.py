import allure


class TestRecoveryPasswordPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recovery_password(self, login_page):
        login_page.go_to_recovery_password()

        assert login_page.check_go_to_recovery_password()

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_input_email_click_recovery(self, recovery_password_page):
        recovery_password_page.input_email()
        recovery_password_page.click_recovery()

        assert recovery_password_page.check_click_recovery()

    @allure.title('Проверка, что поле «Пароль» стало активным')
    def test_password_active(self, recovery_password_page):
        recovery_password_page.click_recovery()
        recovery_password_page.click_view_password()

        assert recovery_password_page.check_view_password()