from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.implicitly_wait(10)

driver.get('https://www.amazon.com/')

elements = driver.find_elements_by_xpath("//a")
for element in elements:
    print(element.get_attribute("href"))

head_children = driver.find_elements_by_xpath("//head/*")
for element in head_children:
    print(element.get_attribute("href"))


driver.quit()