from selenium.webdriver import ActionChains


def open_user_info(driver):
    action = ActionChains(driver)
    user_trigger = driver.find_element_by_id("global-user-trigger")
    action.move_to_element(user_trigger).perform()


def open_frame_login(driver):
    open_user_info(driver)
    login_option = driver.find_elements_by_link_text('Log In')
    login_option[1].click()
    login_iframe = driver.find_element_by_id("disneyid-iframe")
    driver.switch_to.frame(login_iframe)


def close_frame(driver):
    driver.switch_to.default_content()