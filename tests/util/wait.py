from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_element_located_disappear(driver, locator: str, by=By.ID):
    WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element_located((by, locator)))


def wait_until_element_disappear(driver, element):
    WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element(element))