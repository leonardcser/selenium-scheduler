import time
import urllib
from dataclasses import dataclass
from typing import Union

from selenium.common.exceptions import WebDriverException

from selenium_scheduler.classes.runner import BaseRunner, BaseRunnerAdapter
from selenium_scheduler.classes.webdriver import BaseCustomWebdriver
from selenium_scheduler.utils.logging import logger


@dataclass
class ConnectionRunnerAdapter(BaseRunnerAdapter):
    # If set to -1, it will infinitly try to reconnect
    max_retries: int
    # In seconds
    sleep_time: Union[float, int] = 10

    def run(self) -> None:
        tries = 0
        while self.max_retries == -1 or tries < self.max_retries:
            try:
                self.runable.run()
                break
            except (urllib.error.URLError, WebDriverException) as e:
                tries += 1
                tries_total_str = (
                    f" ({tries}/{self.max_retries})"
                    if self.max_retries != -1
                    else ""
                )
                logger.exception(
                    (
                        "Connection lost, retrying in "
                        f"{self.sleep_time}s...{tries_total_str}"
                    ),
                    exc_info=e,
                )
                time.sleep(self.sleep_time)


@dataclass
class DriverRunnerAdapter(BaseRunnerAdapter):
    custom_driver: BaseCustomWebdriver
    runner: BaseRunner

    def run(self) -> None:
        self.custom_driver.init_driver()
        self.runner.set_driver(self.custom_driver.get_driver())
        logger.info("DriverRunnerAdapter: Started successfully")
        tries = 0
        while tries < self.runner.max_retries:
            retries_str = (
                f", retrying... ({tries+1}/{self.runner.max_retries})"
            )
            try:
                self.runner.run()
                break
            except self.runner.exceptions as e:
                logger.exception(
                    f"DriverRunnerAdapter: Exception found{retries_str}",
                    exc_info=e,
                )
            except Exception as e:
                logger.exception(
                    (f"DriverRunnerAdapter: Uncaught Exception{retries_str}"),
                    exc_info=e,
                )
            tries += 1
        if tries == self.runner.max_retries:
            logger.error("DriverRunnerAdapter: Exited after max retries")
        else:
            logger.info("DriverRunnerAdapter: Exited successfully")
        self.custom_driver.get_driver().quit()
