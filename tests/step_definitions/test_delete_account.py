import time

from pytest_bdd import when, scenarios, then, given
from selenium.webdriver.common.by import By

from tests.step_definitions.test_login import assert_login, login
from tests.util.actions import scroll_to_the_end
from tests.util.data import file_data_exist, get_older_created_mail
from tests.util.frames import switch_to_frame_profile
from tests.util.wait import wait_until_element_located_disappear, wait_until_element_disappear

scenarios('../features/delete_account.feature')


@given("there is data created previously")
def previous_data_exist():
    if not file_data_exist():
        raise AssertionError("Did you run signup feature first?. It is mandatory run signup feature at least once before.")


@when('the user performs the flow to delete his account')
def delete(driver):
    login(driver, get_older_created_mail(), "testing_123")
    switch_to_frame_profile(driver)

    scroll_to_the_end(driver)
    wait_until_element_located_disappear(driver, "loading-indicator state-loading", By.CLASS_NAME)

    delete_account = driver.find_element_by_id("cancel-account")
    delete_account.click()
    wait_until_element_disappear(driver, delete_account)

    # TODO find the way make this part to work
    confirm = driver.find_element_by_class_name("btn btn-primary ng-isolate-scope")
    confirm.click()

    time.sleep(10)



@then("the user can see her name in the user section")
def assert_signup(driver):
    assert_login(driver)
