from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_to_input(wait: WebDriverWait, locator: By, user: str):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.clear()
    element.send_keys(user)


def click(wait: WebDriverWait, locator: By):
    """ Wait until element is clicklable and click it
    :param wait:
    :param locator:
    :return:
    """
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

def get_text(wait: WebDriverWait, locator: By) -> None:
    """Get text """
    try:
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.text
    except TimeoutException:
        return None