from selenium.webdriver.common.by import By


class FeedPageLocators:
    WINDOW_DETAILS_ORDER = By.XPATH, '//div[@class="OrderFeed_contentBox__3-tWb"]/ul/li[1]/a'
    BUTTON_CLOSE_DETAILS_ORDER = By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//button'
    LIST_ORDERS = By.XPATH, ('//div[@class="OrderFeed_contentBox__3-tWb"]/ul/li[1]/a/div/p[@class="text '
                             'text_type_digits-default"]')
    DONE_ALL_TIME_ORDERS = By.XPATH, ('//div[@class="OrderFeed_ordersData__1L6Iv"]/div[@class="undefined mb-15"]/p['
                                      '@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    DONE_TODAY_ORDERS = By.XPATH, ('//p[text()="Выполнено за сегодня:"]/parent::div/p[@class="OrderFeed_number__2MbrQ '
                                   'text text_type_digits-large"]')
    NUMBER_IN_WORK = By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li'
