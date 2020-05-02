from selenium.webdriver import ActionChains


def open_user_info(driver):
    action = ActionChains(driver)
    user_trigger = driver.find_element_by_id("global-user-trigger")
    action.move_to_element(user_trigger).perform()


def scroll_to_the_end(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
