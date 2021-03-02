from selenium.webdriver.remote.webelement import WebElement
from common.webdriver_factory import get_driver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def select_listDropdown(wait: WebDriverWait, option: str):
    locator = (By.XPATH, "//*[contains(@class, 'p-dropdown__standings')]")
    element = wait.until(EC.element_to_be_clickable(locator))
    dropdown = Select(element)
    dropdown.select_by_value(option)

def select_Option(wait:WebDriverWait,datavalue):
    locator = (By.XPATH, f"//*[@data-value='{datavalue}']")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

def get_teams_info(wait: WebDriverWait) -> dict:
    locator = (By.XPATH, "//*[@class='responsive-datatable__scrollable']//tbody//tr")
    rows = wait.until(EC.visibility_of_all_elements_located(locator))
    info = []
    for row in rows:
        tmp = parse_team_row(row)
        info.append(tmp)
    return info


def parse_team_row(row: WebElement):
    info = []
    for cell in row.find_elements_by_tag_name('td'):
        info.append(cell.text)
    return info

#se usa para decirle a python que cargue la logica de lo que  se necesita crear
if __name__ == "__main__":
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 10)

    my_driver.get('https://www.mlb.com/es/standings')
    select_listDropdown(my_wait, 'league')
    select_Option(my_wait,"standard")
    select_Option(my_wait, "advanced")


    # Get team info
    teams = get_teams_info(my_wait)
    for team in teams:
        print(' | '.join(team))
        
    my_driver.quit()









