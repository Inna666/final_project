from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), "Basket is not empty"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_ITEM), "Basket is not empty"
