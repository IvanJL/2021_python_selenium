from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.webdriver_factory import get_driver

def login(wait: WebDriverWait, email, my_pass):
    login_locator = (By.XPATH, "//*[@data-tests-id='simple-login-button']//button")
    login_btn = wait.until(EC.element_to_be_clickable(login_locator))
    login_btn.click()

    user_locator = (By.ID, 'email')
    user = wait.until(EC.element_to_be_clickable(user_locator))
    user.clear()
    user.send_keys(email)

    password_locator = (By.ID, 'password')
    password = wait.until(EC.element_to_be_clickable(password_locator))
    password.clear()
    password.send_keys(my_pass)

    submit_btn_locator = (By.XPATH, "//*[@data-tests-id='registerFormSubmitButton']//button")
    submit_btn = wait.until(EC.element_to_be_clickable(submit_btn_locator))
    submit_btn.click()


def search(wait: WebDriverWait, value: str):
    textbox_locator = (By.XPATH, "//*[@data-tests-id='search-box-input']")
    textbox = wait.until(EC.element_to_be_clickable(textbox_locator))
    textbox.clear()
    textbox.send_keys(value)
    textbox.send_keys(Keys.ENTER)

def get_elements(wait: WebDriverWait):
    tag_array = (By.XPATH, "//*[@data-tests-id='search-guide']")
    return wait.until(EC.visibility_of_all_elements_located(tag_array))

def print_results_tags(wait: WebDriverWait):
    for element in get_elements(wait):
        print(f'{element.text}')

def scrapper(wait: WebDriverWait):
    visited_tags = get_elements(my_wait)
    while not visited_tags:
        print_results_tags(my_wait)
        next_navigation_tag = visited_tags[0]
        next_navigation_tag.click()
    else:
        my_driver.back()
    return visited_tags





if __name__ == '__main__':

    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 10)

    my_driver.get('https://www.pinterest.com.mx')
    login(my_wait, 'qamindstester@gmail.com', 'Q@Minds4%')
    search(my_wait, 'Selenium')
    get_elements(my_wait)
    print_results_tags(my_wait)
    scrapper(my_wait)

