import time

from pytest_bdd import when, then, scenarios

from tests.step_definitions.common_steps import open_frame_login, open_user_info, close_frame

scenarios('../features/login.feature')


@when('the user performs the flow to log into ESPN with "<mail>" and "<password>"')
def login(driver, mail, password):
    open_frame_login(driver)
    username_input = driver.find_element_by_css_selector("input.ng-valid-pattern")
    username_input.send_keys(mail)
    password_input = driver.find_element_by_css_selector(".ng-pristine")
    password_input.send_keys(password)
    login_button = driver.find_element_by_css_selector("button.btn")
    login_button.click()
    time.sleep(10)
    close_frame(driver)


@then('the user can see the "<name>" in the user section')
def assert_login(driver, name):
    open_user_info(driver)
    welcome_message = driver.find_element_by_class_name("display-user")
    expected_text = 'Welcome' + name + '!'
    assert welcome_message.get_attribute('textContent') == expected_text
