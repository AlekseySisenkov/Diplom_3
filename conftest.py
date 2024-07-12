import pytest
import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import LOGIN_PAGE_REF, RECOVERY_PASSWORD_REF, PERSONAL_CABINET_REF, MAIN_PAGE_REF, payload, URL_API, \
    REGISTER, USER, ORDERS, payload_ing, FEED_PAGE_REF
from locators.main_page_locators import MainPageLocators
from locators.personal_cabinet_page_locators import PersonalCabinetPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.personal_cabinet_page import PersonalCabinetPage
from pages.recovery_password_page import LoginPage, RecoveryPasswordPage

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
    driver.get(LOGIN_PAGE_REF)
    return LoginPage(driver)


@pytest.fixture(scope='function')
def recovery_password_page(driver):
    driver.get(RECOVERY_PASSWORD_REF)
    return RecoveryPasswordPage(driver)


@pytest.fixture(scope='function')
def personal_cabinet_page(driver):
    driver.get(PERSONAL_CABINET_REF)
    return PersonalCabinetPage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    driver.get(MAIN_PAGE_REF)
    return MainPage(driver)


@pytest.fixture(scope='function')
def feed_page(driver):
    driver.get(FEED_PAGE_REF)
    return FeedPage(driver)


@pytest.fixture(scope='function')
def creat_login_delete_user(driver):
    payload_data = payload
    r = requests.post(URL_API + REGISTER, data=payload_data)

    driver.get(LOGIN_PAGE_REF)
    WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located(PersonalCabinetPageLocators
                                                                                    .PERSONAL_CABINET))
    driver.find_element(*PersonalCabinetPageLocators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located(MainPageLocators
                                                                                    .INPUT_EMAIL))
    driver.find_element(*MainPageLocators.INPUT_EMAIL).send_keys(payload_data['email'])
    driver.find_element(*MainPageLocators.INPUT_PASSWORD).send_keys(payload_data['password'])
    driver.find_element(*MainPageLocators.BUTTON_INPUT).click()
    WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located(MainPageLocators
                                                                                    .BUTTON_MAKE_ORDER))

    yield creat_login_delete_user
    requests.delete(URL_API + USER, headers={'Authorization': r.json()['accessToken']})


@pytest.fixture(scope='function')
def creat_order(driver):
    requests.post(URL_API + ORDERS, data=payload_ing())
