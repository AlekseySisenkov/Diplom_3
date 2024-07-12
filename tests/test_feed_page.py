import allure


class TestMainPage:
    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_open_window_details_order(self, creat_order, feed_page):
        feed_page.open_window_details_order()

        assert feed_page.check_open_window_details_order()

    @allure.title('Проверка отображения на странице «Лента заказов» заказов пользователя из раздела «История заказов»')
    def test_visible_history_orders(self, creat_login_delete_user, feed_page, main_page):
        main_page.adding_order('BUN', 1)
        main_page.click_make_order()
        main_page.refresh_page()
        feed_page.go_to_history_orders()
        feed_page.make_list_history_orders()
        main_page.go_to_orders_feed()

        assert feed_page.check_visible_history_orders()

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_increase_done_all_time_orders(self, creat_login_delete_user, main_page, feed_page):
        count_done_all_time_orders = feed_page.save_count_done_all_time_orders()
        main_page.go_to_constructor()
        main_page.adding_order('BUN', 1)
        main_page.click_make_order()
        main_page.refresh_page()
        main_page.go_to_orders_feed()

        assert count_done_all_time_orders != feed_page.save_count_done_all_time_orders()

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_increase_done_today_orders(self, creat_login_delete_user, main_page, feed_page):
        count_done_today_orders = feed_page.save_count_done_today_orders()
        main_page.go_to_constructor()
        main_page.adding_order('BUN', 1)
        main_page.click_make_order()
        main_page.refresh_page()
        main_page.go_to_orders_feed()

        assert count_done_today_orders != feed_page.save_count_done_today_orders()

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе «В работе»')
    def test_make_order_to_number_in_work(self, creat_login_delete_user, feed_page, main_page):
        main_page.adding_order('BUN', 1)
        main_page.click_make_order()
        number_order = main_page.save_number_order()
        main_page.refresh_page()
        main_page.go_to_orders_feed()

        assert number_order in feed_page.get_number_in_work()