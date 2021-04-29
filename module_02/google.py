from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.implicitly_wait(10)

driver.get('https://www.google.com/')

element = driver.find_element_by_xpath("//body/div")
print(element.get_attribute("class"))

element = driver.find_element_by_xpath("//body/div[last()]")
print(element.get_attribute("class"))

element = driver.find_element_by_xpath("//*[@role = 'Navigation']")
print(element.get_attribute("text"))

element = driver.find_element_by_xpath("//*[@role = 'Navigation']")
print(element.get_attribute("text"))


driver.quit()