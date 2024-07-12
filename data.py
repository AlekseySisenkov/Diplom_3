import random

import requests
from faker import Faker

from locators.main_page_locators import MainPageLocators

fake = Faker()

MAIN_PAGE_REF = 'https://stellarburgers.nomoreparties.site/'
LOGIN_PAGE_REF = 'https://stellarburgers.nomoreparties.site/login'
RECOVERY_PASSWORD_REF = 'https://stellarburgers.nomoreparties.site/forgot-password'
PERSONAL_CABINET_REF = 'https://stellarburgers.nomoreparties.site/account'
FEED_PAGE_REF = 'https://stellarburgers.nomoreparties.site/feed'
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


def payload_ing():
    ingredient_id = []
    r_ing = requests.get(URL_API + INGREDIENTS)
    for i in range(len(r_ing.json()['data'])):
        ingredient_id.append(r_ing.json()['data'][i]['_id'])
    return {"ingredients": [random.choice(ingredient_id), random.choice(ingredient_id)]}


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
