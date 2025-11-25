from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
    
    def should_be_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name == product_name_in_message, \
            f"Product name in message doesn't match. Expected: {product_name}, got: {product_name_in_message}"
    
    def should_be_basket_total_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_IN_MESSAGE).text
        assert product_price == basket_total, \
            f"Basket total doesn't match product price. Expected: {product_price}, got: {basket_total}"
    
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"
    
    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Basket total message is not presented"