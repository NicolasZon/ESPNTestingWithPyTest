import pytest
from pytest_bdd import given
from selenium import webdriver

from tests.util.frames import open_close_iframe_banner_if_exists

ESPN_HOME_PAGE = "https://www.espn.com/?src=com"


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given("the ESPN page is displayed")
def espn_home(driver):
    driver.get(ESPN_HOME_PAGE)
    open_close_iframe_banner_if_exists(driver)
