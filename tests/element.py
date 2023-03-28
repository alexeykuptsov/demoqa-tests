from selenium.webdriver.common.by import By

from tests.browser import Browser


class BaseElement(object):
    def __init__(self, browser: Browser, web_element_locator):
        self.driver = browser.driver
        self.wait = browser.wait
        self.web_element_locator = web_element_locator

    def find_displayed_element(self):
        elements = self.driver.find_elements(*self.web_element_locator)
        displayed_elements = list(filter(lambda x: x.is_displayed(), elements))
        assert len(displayed_elements) == 1
        return displayed_elements[0]

    def wait_until_displayed(self):
        self.wait.until(lambda _: self.find_displayed_element() is not None)


class LabelElement(BaseElement):
    @property
    def text(self):
        return self.driver.find_element(*self.web_element_locator).text


class ButtonElement(BaseElement):
    def click(self):
        return self.find_displayed_element().click()


class TreeListItemElement(BaseElement):
    def click_on_collapse_button(self):
        current_web_element = self.find_displayed_element()
        return current_web_element.find_element(By.CSS_SELECTOR, ".rct-collapse-btn").click()

    def click_on_check_box(self):
        current_web_element = self.find_displayed_element()
        return current_web_element.find_element(By.CSS_SELECTOR, ".rct-checkbox").click()
