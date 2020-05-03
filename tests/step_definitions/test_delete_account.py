from pytest_bdd import when, scenarios, then, given
from selenium.webdriver.common.by import By

from tests.step_definitions.test_login import login
from tests.util.actions import scroll_to_the_end
from tests.util.data import file_data_exist, get_older_created_mail
from tests.util.frames import switch_to_frame_profile
from tests.util.wait import wait_until_element_located_disappear, wait_until_element_located_is_present

scenarios('../features/delete_account.feature')


@given("there is data created previously")
def previous_data_exist():
    if not file_data_exist():
        raise AssertionError(
            "Did you run signup feature first?. It is mandatory run signup feature at least once before.")


@when("the user performs the flow to delete his account")
def delete(driver):
    login(driver, get_older_created_mail(), "testing_123")
    switch_to_frame_profile(driver)

    scroll_to_the_end(driver)
    wait_until_element_located_disappear(driver, "loading-indicator state-loading", By.CLASS_NAME)

    delete_account = driver.find_element_by_id("cancel-account")
    delete_account.click()

    wait_until_element_located_is_present(driver, ".btn.btn-primary.ng-isolate-scope", By.CSS_SELECTOR)
    confirm = driver.find_element_by_css_selector(".btn.btn-primary.ng-isolate-scope")
    confirm.click()


@then("the user can see deleted account message")
def assert_account_was_deleted(driver):
    assert ("Your account has been deleted" in driver.page_source)
