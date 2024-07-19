import allure
import pytest


class TestMainPage:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_go_to_constructor(self, creat_login_delete_user, main_page):
        main_page.go_to_constructor()

        assert main_page.check_go_to_constructor()

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_go_to_orders_feed(self, creat_login_delete_user, main_page):
        main_page.go_to_orders_feed()

        assert main_page.check_go_to_orders_feed()

    @allure.title('Проверка закрытия по крестику всплывающего окна ингредиента')
    @pytest.mark.parametrize("num, locator", [
        (1, 'BUN'), (2, 'BUN'),
        (1, 'SOUSE'), (2, 'SOUSE'), (3, 'SOUSE'), (4, 'SOUSE'),
        (1, 'FILLING'), (2, 'FILLING'), (3, 'FILLING'), (4, 'FILLING'), (5, 'FILLING'),
        (6, 'FILLING'), (7, 'FILLING'), (8, 'FILLING'), (9, 'FILLING')
        ])
    def test_close_pop_up_window_ingredient(self, main_page, num, locator):
        main_page.open_pop_up_window_ingredient(locator, num)
        main_page.click_close_pop_up_window_ingredient()

        assert main_page.check_click_close_pop_up_window_ingredient()

    @allure.title('Проверка увеличения счётчика ингредиента при его добавлении в заказ')
    @pytest.mark.parametrize("num, locator", [
        (1, 'BUN_COUNT'), (2, 'BUN_COUNT'),
        (1, 'SOUSE_COUNT'), (2, 'SOUSE_COUNT'), (3, 'SOUSE_COUNT'), (4, 'SOUSE_COUNT'),
        (1, 'FILLING_COUNT'), (2, 'FILLING_COUNT'), (3, 'FILLING_COUNT'), (4, 'FILLING_COUNT'), (5, 'FILLING_COUNT'),
        (6, 'FILLING_COUNT'), (7, 'FILLING_COUNT'), (8, 'FILLING_COUNT'), (9, 'FILLING_COUNT')
    ])
    def test_counter_increase_ingredient(self, main_page, num, locator):
        count_ingredient = main_page.get_count_ingredient(locator, num)
        main_page.adding_order(locator, num)

        assert count_ingredient != main_page.adding_order(locator, num)

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    def test_make_order_login_user(self, creat_login_delete_user, main_page):
        main_page.adding_order('BUN', 1)
        main_page.click_make_order()

        assert main_page.check_make_order()