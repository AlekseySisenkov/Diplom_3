from faker import Faker

from locators.main_page_locators import MainPageLocators

fake = Faker()

MAIN_REF = 'https://stellarburgers.nomoreparties.site/'
LOGIN_PAGE = 'login'
RECOVERY_PASSWORD_PAGE = 'forgot-password'
PERSONAL_CABINET_PAGE = 'account'
FEED_PAGE = 'feed'
URL_API = 'https://stellarburgers.nomoreparties.site/api'
REGISTER = '/auth/register'
LOGIN = '/auth/login'
USER = '/auth/user'
INGREDIENTS = '/ingredients'
ORDERS = '/orders'

payload = {
    "email": fake.email(),
    "name": fake.name(),
    "password": fake.password()
}


def set_parameter(parameter):
    if parameter == 'BUN':
        return MainPageLocators.INGREDIENT_BUN
    if parameter == 'SOUSE':
        return MainPageLocators.INGREDIENT_SOUSE
    if parameter == 'FILLING':
        return MainPageLocators.INGREDIENT_FILLING
    if parameter == 'BUN_COUNT':
        return MainPageLocators.INGREDIENT_BUN_COUNT_INGREDIENT
    if parameter == 'SOUSE_COUNT':
        return MainPageLocators.INGREDIENT_SOUSE_COUNT_INGREDIENT
    if parameter == 'FILLING_COUNT':
        return MainPageLocators.INGREDIENT_FILLING_COUNT_INGREDIENT
