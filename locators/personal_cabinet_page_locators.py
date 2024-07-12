from selenium.webdriver.common.by import By


class PersonalCabinetPageLocators:
    PERSONAL_CABINET = By.XPATH, '//p[text()="Личный Кабинет"]'
    HISTORY_ORDERS = By.XPATH, '//a[text()="История заказов"]'
    BUTTON_OUTPUT = By.XPATH, '//button[text()="Выход"]'
