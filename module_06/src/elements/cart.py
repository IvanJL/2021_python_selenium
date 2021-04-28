from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.cart import CartLoc
from module_06.src.mixin.InventoryItemMixin import InventoryItemMixin


class Cart(InventoryItemMixin, BasePageElement):
    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(CartLoc.TITLE, wait=wait, root=root)
        self._ctn_shoppingBtn = BasePageElement(CartLoc.CTN_SHOPPING, wait=wait, root=root)

