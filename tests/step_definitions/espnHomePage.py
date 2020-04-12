import pytest
from pytest_bdd import given
from selenium import webdriver

ESPN_HOME_PAGE = "https://www.espn.com/?src=com"


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given("the ESPN page is displayed")
def espnHome(browser):
    browser.get(ESPN_HOME_PAGE)