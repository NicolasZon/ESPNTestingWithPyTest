import time

from pytest_bdd import when, scenarios, then

from tests.step_definitions.test_login import assert_login
from tests.util.actions import scroll_to_the_end
from tests.util.data import create_fake_mail
from tests.util.frames import open_frame_login, close_frame

scenarios('../features/signup.feature')


@when('the user performs the flow to create a new account')
def signup(driver):
    open_frame_login(driver)

    signup_button = driver.find_element_by_css_selector(".btn.btn-secondary.ng-isolate-scope")
    signup_button.click()

    first_name = driver.find_element_by_name("firstName")
    first_name.send_keys("Pepito")
    last_name = driver.find_element_by_name("lastName")
    last_name.send_keys("Perez")
    email = driver.find_element_by_name("email")
    email.send_keys(create_fake_mail())
    password = driver.find_element_by_name("newPassword")
    password.send_keys("testing_123")

    scroll_to_the_end(driver)

    signup_button = driver.find_element_by_css_selector(".btn.btn-primary.ng-scope.ng-isolate-scope")
    signup_button.click()

    time.sleep(10)
    close_frame(driver)


@then("the user can see her name in the user section")
def assert_signup(driver):
    assert_login(driver)
