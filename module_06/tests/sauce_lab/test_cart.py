"""Test Cases from Cart"""
import pytest

from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'


class TestCart(TestBase):

    # Ivan Test:  Go to cart and Back
    def test_cart(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        cart = inventory.click_cart()
        assert cart.get_title() == 'YOUR CART', 'Cart page label should be "YOUR CART"'
        cart.back_shopping()
        assert inventory.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    # Ivan Test: Remove Items from the cart
    def test_added_items(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        # Add to cart
        for item in inventory_page.products:
            item.add_to_cart()
        cart_page = inventory_page.open_cart()
        # Delete from Cart
        for item in cart_page.products:
            item.remove_from_cart()





