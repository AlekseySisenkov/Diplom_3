from selenium.webdriver.common.by import By


class PersonalCabinetPageLocators:
    HISTORY_ORDERS = By.XPATH, '//a[text()="История заказов"]'
    BUTTON_OUTPUT = By.XPATH, '//button[text()="Выход"]'
    NUM_ORDERS = By.XPATH, '//div[@class="OrderHistory_textBox__3lgbs mb-6"]/p[@class="text text_type_digits-default"]'
