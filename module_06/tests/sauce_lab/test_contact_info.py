from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'


class TestContactInfo(TestBase):

    # Ivan Test : Test with Only First name
    def test_contact_info_incomplete(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Ivan")
        contact_info_page.checkout()
        assert contact_info_page.get_error_msg() == "Error: Last Name is required"

    # Ivan Test : Test with Only last name
    def test_contact_info_incomplete_two(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(lastname="Landa")
        contact_info_page.checkout()
        assert contact_info_page.get_error_msg() == "Error: First Name is required"

    # Ivan Test : Test without Postal Code
    def test_contact_info_incomplete_three(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Ivan", lastname="Landa")
        contact_info_page.checkout()
        assert contact_info_page.get_error_msg() == "Error: Postal Code is required"

    # Ivan Test : Test Navigation Back.
    def test_navigation_back(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for item in inventory.products:
            item.add_to_cart()
        cart_page = inventory.open_cart()
        contact_info_page = cart_page.checkout()
        contact_info_page.fill_info(firstname="Ivan", lastname="Landa", postal_code="555555")
        contact_info_page.back_to_cart()
        assert cart_page.get_title() == 'YOUR CART', 'Cart page label should be "YOUR CART"'


