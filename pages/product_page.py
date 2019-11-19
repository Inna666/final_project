from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add_to_basket_button is not presented"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self, product_name, product_price):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.is_correct_product_price(product_price)
        self.is_correct_product_name(product_name)

    def is_correct_product_price(self, product_price):
        assert product_price == self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_PRICE_MESSAGE).text, "Incorrect price"

    def is_correct_product_name(self, product_name):
        flag = False
        for message_success in self.browser.find_elements(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS_MESSAGES):
            if product_name == message_success.text:
                flag = True
                break
        assert flag == True, "Incorrect name"

    def is_success_message_not_present(self):
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS_MESSAGES), "success message is presented"

    def is_message_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS_MESSAGES), "success message is presented"


