import allure


class TestPersonalCabinetPage:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_personal_cabinet(self, creat_login_delete_user, personal_cabinet_page, main_page):
        main_page.go_to_personal_cabinet()

        assert personal_cabinet_page.check_go_to_personal_cabinet()

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_go_to_history_orders(self, creat_login_delete_user, personal_cabinet_page):
        personal_cabinet_page.go_to_history_orders()

        assert personal_cabinet_page.check_go_to_history_orders()

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_account(self, creat_login_delete_user, main_page, personal_cabinet_page):
        personal_cabinet_page.exit_account()

        assert main_page.check_exit_account()
