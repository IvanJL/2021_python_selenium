from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select


driver = get_driver('chrome')
driver.get('https://formsmarts.com/html-form-example')
driver.switch_to.frame(driver.find_element_by_class_name('fs_embed'))

first_name = driver.find_element_by_id('u_jSx_4607')
first_name.clear()
first_name.send_keys('Ivan')

last_name = driver.find_element_by_id('u_jSx_338354')
last_name.clear()
last_name.send_keys('Jimenez')

email = driver.find_element_by_id('u_jSx_4608')
email.clear()
email.send_keys('ijimenez@anexinet.com')

dropdown = driver.find_element_by_id("u_jSx_338367")
dropdown = Select(dropdown)
dropdown.select_by_value("Sales Inquiry")

inquiry = driver.find_element_by_id('u_jSx_4609')
inquiry.clear()
inquiry.send_keys('My Inquiry')

continue_btn = driver.find_element_by_name('submit')
continue_btn.click()