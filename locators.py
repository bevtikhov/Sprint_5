from selenium.webdriver.common.by import By

class TestLocators:
    name = By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input[@class="text input__textfield text_type_main-default"]' # Поле "Имя" на странице "Регистрация"
    email = By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input[@class="text input__textfield text_type_main-default"]' # Поле "Email" на странице "Регистрация"
    password = By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/div/input[@class="text input__textfield text_type_main-default"]' # Поле "Пароль" на странице "Регистрация"
    register_button = By.XPATH, '//button[text() = "Зарегистрироваться"]' # Кнопка "Зарегистрироваться" на странице "Регистрация"
    recovery_password_button = By.XPATH, '//a[text() = "Восстановить пароль"]' # Кнопка восстановления пароля на странице "Вход"
    incorrect_password_alert = By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/p[@class="input__error text_type_main-default"]' # Ошибка некорректного пароля на странице "Регистрация"
    login_button_on_main_page = By.XPATH, '/html/body/div/div/main/section[2]/div/button[text() = "Войти в аккаунт"]' # Кнопка "Войти в аккаунт" на главной странице
    login_email = By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input[@class="text input__textfield text_type_main-default"]' # Поле "Email" на странице "Вход"
    login_password = By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input[@class="text input__textfield text_type_main-default"]' # Поле "Пароль" на странице "Вход"
    login_button = By.XPATH, '/html/body/div/div/main/div/form/button[text() = "Войти"]' # Кнопка "Войти" на странице "Вход"
    order_button = By.XPATH, '/html/body/div/div/main/section[2]/div/button[text() = "Оформить заказ"]' # Кнопка "Оформить заказ" в разделе "Конструктор"
    personal_account_button = By.XPATH, '/html/body/div/div/header/nav/a[@class="AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo"]' # Кнопка "Личный кабинет"
    save_button = By.XPATH, '/html/body/div/div/main/div/div/div/div/button[text() = "Сохранить"]' # Кнопка "Сохранить" в разделе "Личный кабинет"
    profile_button = By.XPATH, '/html/body/div/div/main/div/nav/ul/li[1]/a[text() = "Профиль"]' # Кнопка "Профиль" в разделе "Личный кабинет"
    constructor_button = By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a/p[text() = "Конструктор"]' # Кнопка раздела "Конструктор"
    constructor_burger_h1 = By.XPATH, '/html/body/div/div/main/section[1]/h1[text() = "Соберите бургер"]' # Заголовок раздела "Конструктор"
    logo_burgers = By.XPATH, '/html/body/div/div/header/nav/div/a[@class="active"]' # Логотип "Stellar Burgers"
    logout_button = By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button[text() = "Выход"]' # Кнопка "Выход" в разделе "Личный кабинет"
    register_button_on_login_page = By.XPATH, '/html/body/div/div/main/div/div/p[1]/a[text() = "Зарегистрироваться"]' # Кнопка "Зарегистрироваться" на странице "Вход"
    bun_button = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]/span[text() = "Булки"]' # Раздел "Булки"
    sauce_button = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]/span[text() = "Соусы"]' # Раздел "Соусы"
    filling_button = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]/span[text() = "Начинки"]' # Раздел "Начинки"
    login_button_on_registration_page = By.XPATH, '/html/body/div/div/main/div/div/p/a[text() = "Войти"]'  # Кнопка "Войти" на странице "Регистрация"
    forgot_password_button = By.XPATH, '/html/body/div/div/main/div/div/p[2]/a[text() = "Восстановить пароль"]'  # Кнопка "Восстановить пароль" на странице "Вход"