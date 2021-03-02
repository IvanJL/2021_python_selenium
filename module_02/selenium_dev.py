"""Web Driver Example"""
from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://www.selenium.dev/')
print(driver.current_url)
print(driver.title)


def challenge(element):
    sel_link = driver.find_element_by_link_text(element)

    print(sel_link.get_attribute("href"))
    print(f'{element} link is displayed: {sel_link.is_displayed()}')
    print(f'{element} link is enabled: {sel_link.is_enabled()}')
    print(f'{element} link is selected: {sel_link.is_selected()}')
    print(f'{element} word count: {driver.page_source.count(f"{element}")}')

    if sel_link.is_enabled() and sel_link.is_displayed():
        sel_link.click()


challenge("Downloads")
print("*********------------------------------------------------------*********")
challenge("Projects")
print("*********------------------------------------------------------*********")
challenge("Support")
print("*********------------------------------------------------------*********")
challenge("Blog")
print("*********------------------------------------------------------*********")


driver.quit()
