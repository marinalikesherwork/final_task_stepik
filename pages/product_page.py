from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_cart(self):        
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button Add to cart is not present"
        
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()
        
    def should_be_book_name(self):        
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not present"
        
    def should_be_price(self):        
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not present"
     
    def should_be_book_name_on_notification(self):        
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_NOTIFICATION), "Book name is not present on notification"
     
    def should_be_price_on_notification(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_NOTIFICATION), "Price is not present on notification"
        
    def compare_book_name_and_book_name_on_notification(self):
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        name_on_notification = self.browser.find_element(*ProductPageLocators.BOOK_NAME_NOTIFICATION)
        assert name.text == name_on_notification.text, "name of the book is different"
        
    def compare_price_and_price_on_notification(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_on_notification = self.browser.find_element(*ProductPageLocators.PRICE_NOTIFICATION)
        assert price.text == price_on_notification.text, "price of the book is different"