from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BUTTON_ADD = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_NOTIFICATION = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRICE_NOTIFICATION = (By.CSS_SELECTOR, "#messages .alert-info strong")