import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

from selenium_scheduler.classes.exceptions import (
    WebDriverNotInitialisedException,
)
from selenium_scheduler.classes.webdriver import BaseCustomWebdriver
from selenium_scheduler.types import UCDriver


class CustomWebdriver(BaseCustomWebdriver):
    # 'cache_session' not implemented yet
    def __init__(
        self, headless: bool = False, cache_session: bool = False
    ) -> None:
        self._headless = headless
        self._driver = None

    def init_driver(self) -> None:
        opts = uc.ChromeOptions()
        v = ChromeDriverManager().driver.get_browser_version()
        opts.headless = self._headless
        self._driver = uc.Chrome(options=opts, version_main=v.split(".")[0])

    def get_driver(self) -> UCDriver:
        if self._driver is None:
            raise WebDriverNotInitialisedException
        return self._driver
