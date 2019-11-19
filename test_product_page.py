import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        loginPage = LoginPage(browser, link)
        loginPage.open()
        email = str(time.time()) + "@fakemail.org"
        loginPage.register_new_user(email, "qa12345678")
        loginPage.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_product_to_basket(product_name, product_price)

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_product_to_basket(product_name, product_price)
        page.is_success_message_not_present()

@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket(product_name, product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket(product_name, product_price)
    page.is_success_message_not_present()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.is_success_message_not_present()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket(product_name, product_price)
    page.is_message_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    basket = BasketPage(browser, browser.current_url)
    basket.should_not_be_products_in_basket()
    basket.should_be_empty_basket()
