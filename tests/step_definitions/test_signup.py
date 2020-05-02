from pytest_bdd import when, scenarios, then

from tests.step_definitions.common_steps import open_frame_login, close_frame, scroll_to_the_end

scenarios('../features/signup.feature')


@when('the user performs the flow to create a new account')
def signup(driver):
    open_frame_login(driver)

    signup_button = driver.find_element_by_css_selector(".btn.btn-secondary.ng-isolate-scope")
    signup_button.click()

    first_name = driver.find_element_by_name("firstName")
    first_name.send_keys("pepito")
    last_name = driver.find_element_by_name("lastName")
    last_name.send_keys("perez")
    email = driver.find_element_by_name("email")
    email.send_keys("jiojaanw@mail.com")
    password = driver.find_element_by_name("newPassword")
    password.send_keys("qwertyuiop")

    scroll_to_the_end(driver)

    signup_button = driver.find_element_by_css_selector(".btn.btn-primary.ng-scope.ng-isolate-scope")
    signup_button.click()

    close_frame(driver)


@then("the user can see her name in the user section")
def step_impl():
    raise NotImplementedError(u'STEP: Then the user can see her name in the user section')