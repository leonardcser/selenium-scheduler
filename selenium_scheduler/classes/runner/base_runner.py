from dataclasses import dataclass

from selenium_scheduler.interfaces import Runable
from selenium_scheduler.types import UCDriver


@dataclass
class BaseRunner(Runable):
    conn_max_retries = -1
    max_retries = 5
    exceptions = tuple()
    headless = True
    cache_session = False
    driver: UCDriver = None

    def set_driver(self, driver: UCDriver) -> None:
        self.driver = driver
