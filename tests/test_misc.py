import os

import pytest
import selenium.webdriver
import webdriver_manager.chrome
import webdriver_manager.firefox

from tests.browser import Browser
from tests.page import MainPage, ElementsPage


@pytest.fixture
def browser():
    # Первый раз пользуюсь webdriver_manager, не успел разобраться, как сделать аналог `addopts = --driver=Chrome`,
    # поэтому выбираю браузер с помощью env variable
    browser_name = os.environ.get("BROWSER_NAME")
    if browser_name is None:
        raise AssertionError('Environment variable BROWSER_NAME should be set')
    elif browser_name == 'Chrome':
        driver = selenium.webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
    elif browser_name == 'Firefox':
        driver = selenium.webdriver.Firefox(executable_path=webdriver_manager.firefox.GeckoDriverManager().install())
    else:
        raise ValueError('Unexpected value of environment variable BROWSER_NAME')
    return Browser(driver)


def test_navigate_to_checkbox_page_and_select_word_file(browser):
    main_page = browser.go_to('https://demoqa.com/', MainPage)
    main_page.elements_button.click()
    elements_page = browser.get_current_page(ElementsPage)
    elements_page.check_box_button.click()
    elements_page.home_tree_list_item.wait_until_displayed()
    elements_page.home_tree_list_item.click_on_collapse_button()
    elements_page.downloads_list_item.wait_until_displayed()
    elements_page.downloads_list_item.click_on_collapse_button()
    elements_page.word_file_item.wait_until_displayed()
    elements_page.word_file_item.click_on_check_box()
    elements_page.result_label.wait_until_displayed()

    assert elements_page.result_label.text == 'You have selected :\nwordFile'
