import pytest
from .pages.product_page import ProductPage
import time
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