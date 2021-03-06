from selenium.common.exceptions import NoSuchElementException

from tests.util.actions import open_user_info


def close_frame(driver):
    driver.switch_to.default_content()


def close_iframe_banner_if_exists(driver):
    try:
        banner_iframe = driver.find_element_by_xpath("//div[contains(@class, 'promo-banner-container')]/child::iframe")
        driver.switch_to_frame(banner_iframe)
        close_banner_button = driver.find_element_by_class_name("PromoBanner__CloseBtn")
        close_banner_button.click()
        close_frame(driver)
    except NoSuchElementException:
        print("INFO: Banner does not appear")


def switch_to_frame_login(driver):
    open_user_info(driver)
    login_option = driver.find_elements_by_link_text('Log In')
    login_option[1].click()
    switch_to_main_frame(driver)


def switch_to_frame_profile(driver):
    open_user_info(driver)
    profile_option = driver.find_element_by_link_text('ESPN Profile')
    profile_option.click()
    switch_to_main_frame(driver)


def switch_to_main_frame(driver):
    main_iframe = driver.find_element_by_id("disneyid-iframe")
    driver.switch_to.frame(main_iframe)
