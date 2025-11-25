from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "a.btn[href*='basket']")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")  # Это не обязательно, т.к. проверяем URL через браузер
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert-info p")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success strong")
    BASKET_TOTAL_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong")
