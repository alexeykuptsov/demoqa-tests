from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.element import LabelElement, ButtonElement, TreeListItemElement


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, browser):
        self.browser = browser
        self.driver = browser.driver
        self.wait = browser.wait

    def wait_until_loaded(self):
        self.wait.until(lambda _: self.driver.execute_script('return document.readyState') == 'complete')


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.elements_button = ButtonElement(
            self.browser, (By.XPATH, '//*[contains(concat(" ", @class, " "), " card ") and contains(.//*, "Elements")]'))

    def wait_until_loaded(self):
        super().wait_until_loaded()
        self.wait.until(lambda _: self.elements_button is not None)


class ElementsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.check_box_button = ButtonElement(
            self.browser, (By.XPATH, '//*[@class="menu-list"]/li[contains(.//span, "Check Box")]'))
        self.home_tree_list_item = TreeListItemElement(
            self.browser, (By.XPATH, '//*[contains(concat(" ", @class, " "), " rct-node ") and contains(.//*, "Home")]'))
        self.downloads_list_item = TreeListItemElement(
            self.browser, (By.XPATH, '//*[contains(concat(" ", @class, " "), " rct-node ") and contains(.//*, "Downloads")]'))
        self.word_file_item = TreeListItemElement(
            self.browser, (By.XPATH, '//*[contains(concat(" ", @class, " "), " rct-node ") and contains(.//*, "Word File.doc")]'))
        self.result_label = LabelElement(self.browser, (By.ID, 'result'))

    def wait_until_loaded(self):
        super().wait_until_loaded()
        self.wait.until(lambda _: self.check_box_button is not None)
