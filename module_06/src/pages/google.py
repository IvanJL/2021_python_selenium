from selenium.webdriver.android.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.google import GoogleLocators
from module_06.src.pages.base_page import BasePage

_URL = 'https://www.google.com'

class Google(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.__search_textbox = BasePageElement(GoogleLocators.SEARCH_TEXT_BOX, wait=self._wait)
        self.__search_btn = BasePageElement(GoogleLocators.SEARCH_BTN, wait=self._wait)
        self.__feeling_lucky_btn = BasePageElement(GoogleLocators.FEELING_LUCKY_BTN, wait = self._wait)
