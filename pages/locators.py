from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]//span//a[@class='btn btn-default']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    PRODUCT_NAME = (By.XPATH, "//article[@class='product_page']//h1")
    PRODUCT_PRICE = (By.XPATH, "//article[@class='product_page']//p[@class='price_color']")
    PRODUCT_ADD_TO_BASKET_SUCCESS_MESSAGES = (By.XPATH, "//div[contains(@class, 'alert-success')]//div[@class='alertinner ']//strong")
    PRODUCT_ADD_TO_BASKET_PRICE_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-info')]//div[@class='alertinner ']//strong")

class BasketPageLocators():
    BASKET_FORM = (By.XPATH, "//form[@id='basket_formset']")
    BASKET_EMPTY_ITEM = (By.XPATH, "//div[@id='content_inner']//p")