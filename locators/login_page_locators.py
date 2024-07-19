from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_RECOVERY_PASS = By.XPATH, ('//p[text()="Забыли пароль?"]/a[@class="Auth_link__1fOlj" and text('
                                      ')="Восстановить пароль"]')