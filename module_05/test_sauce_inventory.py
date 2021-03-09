"""Test cases for inventory"""
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_05.sauce_fun_lib.inventory import get_inventory, InventoryItem
from module_05.sauce_fun_lib.login import login, get_login_error

VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']


def test_inventory_size():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) == 6, 'Inventory should contain 6 items'
    driver.close()


_ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'


def test_invalid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'invalid_secret')
    error_msg = get_login_error(wait)
    assert error_msg is not None, 'Error message should be displayed for invalid login'
    assert error_msg == _ERROR_MSG, f'Error message should be {_ERROR_MSG}'
    with pytest.raises(TimeoutException):
        get_inventory(wait)
    driver.close()