from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_CABINET = By.XPATH, '//p[text()="Личный Кабинет"]'
    BUTTON_CONSTRUCTOR = By.XPATH, '//p[text()="Конструктор"]'
    BUTTON_ORDERS_FEED = By.XPATH, '//p[text()="Лента Заказов"]'
    BUTTON_INGREDIENT_WINDOW_CLOSE = By.XPATH, ('//section[@class="Modal_modal_opened__3ISw4 '
                                                'Modal_modal__P3_V5"]//button')
    BUTTON_MAKE_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'
    BUTTON_CLOSE_MAKE_ORDER = By.XPATH, ('//button[@class="Modal_modal__close_modified__3V5XS '
                                         'Modal_modal__close__TnseK"]')
    TEXT_ORDERS_FEED = By.XPATH, '//h1[text()="Лента заказов"]'
    INGREDIENT_BUN = By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul[1]/a[{}]'
    INGREDIENT_SOUSE = By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul[2]/a[{}]'
    INGREDIENT_FILLING = By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul[3]/a[{}]'
    DETAILS_INGREDIENT = By.XPATH, '//h2[text()="Детали ингредиента"]/parent::div/parent::div/parent::section'
    FIELD_ORDER = By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]/ul'
    NUMBER_ORDER = By.XPATH, ('//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text '
                              'text_type_digits-large mb-8"]')
    INGREDIENT_BUN_COUNT_INGREDIENT = By.XPATH, ('//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo'
                                                 '"]/ul[1]/a[{}]/div/p[@class="counter_counter__num__3nue1"]')
    INGREDIENT_SOUSE_COUNT_INGREDIENT = By.XPATH, ('//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo'
                                                   '"]/ul[2]/a[{}]/div/p[@class="counter_counter__num__3nue1"]')
    INGREDIENT_FILLING_COUNT_INGREDIENT = By.XPATH, ('//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo'
                                                     '"]/ul[3]/a[{}]/div/p[@class="counter_counter__num__3nue1"]')
    ORDER_PROCESSED = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'
    WAIT_NUMBER_ORDER = By.XPATH, '//img[@class="Modal_modal__loading__3534A"]/parent::div[@class="Modal_modal__P3_V5"]'

    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/parent::div/input'  # Поле "Email"
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # Поле "Пароль"
    BUTTON_INPUT = By.XPATH, '//button[text()="Войти"]'  # Кнопка "Войти"
