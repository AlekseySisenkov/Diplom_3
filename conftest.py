import pytest
import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import payload, URL_API, REGISTER, USER, ORDERS, MAIN_REF, LOGIN_PAGE, RECOVERY_PASSWORD_PAGE, \
    PERSONAL_CABINET_PAGE, FEED_PAGE
from helpers import payload_ing
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_cabinet_page import PersonalCabinetPage
from pages.recovery_password_page import RecoveryPasswordPage

fake = Faker()


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.go_to_url(MAIN_REF+LOGIN_PAGE)
    return login_page


@pytest.fixture(scope='function')
def recovery_password_page(driver):
    recovery_password_page = RecoveryPasswordPage(driver)
    recovery_password_page.go_to_url(MAIN_REF+RECOVERY_PASSWORD_PAGE)
    return recovery_password_page


@pytest.fixture(scope='function')
def personal_cabinet_page(driver):
    personal_cabinet_page = PersonalCabinetPage(driver)
    personal_cabinet_page.go_to_url(MAIN_REF+PERSONAL_CABINET_PAGE)
    return personal_cabinet_page


@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver)
    main_page.go_to_url(MAIN_REF)
    return main_page


@pytest.fixture(scope='function')
def feed_page(driver):
    feed_page = FeedPage(driver)
    feed_page.go_to_url(MAIN_REF+FEED_PAGE)
    return feed_page


@pytest.fixture(scope='function')
def creat_login_delete_user(main_page):
    payload_data = payload
    r = requests.post(URL_API + REGISTER, data=payload_data)

    main_page.go_to_personal_cabinet()
    main_page.find_element_with_wait(MainPageLocators.INPUT_EMAIL)
    main_page.set_text_to_field(MainPageLocators.INPUT_EMAIL, payload_data['email'])
    main_page.set_text_to_field(MainPageLocators.INPUT_PASSWORD, payload_data['password'])
    main_page.click_element(MainPageLocators.BUTTON_INPUT)
    main_page.find_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)

    yield creat_login_delete_user
    requests.delete(URL_API + USER, headers={'Authorization': r.json()['accessToken']})


@pytest.fixture(scope='function')
def creat_order(driver):
    requests.post(URL_API + ORDERS, data=payload_ing())
