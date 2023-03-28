from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Browser:
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def go_to(self, url, page_object_class):
        self.driver.get(url)
        return self.get_current_page(page_object_class)

    def get_current_page(self, page_object_class):
        page = page_object_class(self)
        page.wait_until_loaded()
        return page
