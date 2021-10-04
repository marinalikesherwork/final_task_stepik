from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_items_to_buy(self):
        assert not self.is_element_present(*BasketPageLocators.ITEMS_TO_BUY),\
            "Items to buy now is presented"
            
    def should_be_message_busket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BUSKET_EMPTY_MESSAGE), "Message that busket is empty is not presented"