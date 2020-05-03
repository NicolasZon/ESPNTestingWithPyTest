from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_element_located_disappear(driver, locator: str, by=By.ID):
    WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element_located((by, locator)))


def wait_until_element_located_is_present(driver, locator: str, by=By.ID):
    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((by, locator)))
