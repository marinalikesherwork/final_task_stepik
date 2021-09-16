from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_book_name()
    page.should_be_price()
    page.should_be_book_name_on_notification
    page.should_be_price_on_notification    
    page.compare_book_name_and_book_name_on_notification()
    page.compare_price_and_price_on_notification