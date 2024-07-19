from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/parent::div/input'
    BUTTON_RECOVERY = By.XPATH, '//button[text()="Восстановить"]'
    BUTTON_VIEW_PASS = By.XPATH, '//div[@class="input__icon input__icon-action"]'
    IS_NOT_ACTIVE_PASSWORD = By.XPATH, '//label[text()="Пароль"]/parent::div'
