import allure

from locators.feed_page_locators import FeedPageLocators, HistoryOrdersLocators
from locators.personal_cabinet_page_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Открываем окно деталей заказа')
    def open_window_details_order(self):
        self.click_element(FeedPageLocators.WINDOW_DETAILS_ORDER)

    @allure.step('Проверяем открытие окна деталей заказа')
    def check_open_window_details_order(self):
        return self.find_element_with_wait(FeedPageLocators.BUTTON_CLOSE_DETAILS_ORDER)

    @allure.step('Переходим в раздел «История заказов»')
    def go_to_history_orders(self):
        self.click_element(PersonalCabinetPageLocators.PERSONAL_CABINET)
        self.click_element(PersonalCabinetPageLocators.HISTORY_ORDERS)

    @allure.step('Берем номер заказа из раздела «История заказов»')
    def make_list_history_orders(self):

        return self.get_text(HistoryOrdersLocators.NUM_ORDERS)

    @allure.step('Проверяем отображение на странице «Лента заказов» заказов пользователя из раздела «История заказов»')
    def check_visible_history_orders(self):
        if self.make_list_history_orders() in self.get_text(FeedPageLocators.LIST_ORDERS):
            return True
        else:
            return False

    @allure.step('Сохраняем счетчик «Выполнено за все время»')
    def save_count_done_all_time_orders(self):

        return self.get_text(FeedPageLocators.DONE_ALL_TIME_ORDERS)

    @allure.step('Сохраняем счетчик «Выполнено за сегодня»')
    def save_count_done_today_orders(self):

        return self.get_text(FeedPageLocators.DONE_TODAY_ORDERS)

    @allure.step('Получаем номер заказа в работе')
    def get_number_in_work(self):
        self.wait_text("0", FeedPageLocators.NUMBER_IN_WORK)

        return self.get_text(FeedPageLocators.NUMBER_IN_WORK)
