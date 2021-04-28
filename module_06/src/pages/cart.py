from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.elements.cart_items import CartItems
from module_06.src.locators.cart import CartLoc
from module_06.src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.header import Header

_URL = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        # Just added by Ivan
        self.products = CartItems(CartLoc.CART_ITEMS, self._wait)
        self.__title = BasePageElement(CartLoc.TITLE, self._wait)
        self.__ctn_shopping = BasePageElement(CartLoc.CTN_SHOPPING, self._wait)
        self.__remove_button = BasePageElement(CartLoc.REMOVE_BUTTON, self._wait)
        self.header = Header(self._wait)

    def back_shopping(self):
        self.__ctn_shopping.click()

    def get_title(self) -> str:
        return self.__title.get_text()

    def remove_item(self):
        self.__remove_button.click()
