import socket
import time
import urllib
from dataclasses import dataclass
from typing import Union

import requests
import urllib3
from selenium.common.exceptions import WebDriverException

from selenium_scheduler.classes.runner import BaseRunner, BaseRunnerAdapter
from selenium_scheduler.classes.webdriver import BaseCustomWebdriver
from selenium_scheduler.utils.logging import logger


@dataclass
class ExceptionInterceptRunnerAdapter(BaseRunnerAdapter):
    def run(self) -> None:
        try:
            self.runable.run()
        except Exception as e:
            logger.exception(
                "ExceptionInterceptRunnerAdapter: Uncaught Exception",
                exc_info=e,
            )


@dataclass
class ConnectionRunnerAdapter(BaseRunnerAdapter):
    # If set to -1, it will infinitly try to reconnect
    max_retries: int
    # In seconds
    sleep_time: Union[float, int] = 10
    connection_exceptions = (
        urllib.error.URLError,
        WebDriverException,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ConnectionError,
        urllib3.exceptions.MaxRetryError,
        urllib3.exceptions.NewConnectionError,
        socket.gaierror,
    )

    def run(self) -> None:
        tries = 0
        while self.max_retries == -1 or tries < self.max_retries:
            try:
                self.runable.run()
                break
            except self.connection_exceptions:
                tries += 1
                tries_total_str = (
                    f" ({tries}/{self.max_retries})"
                    if self.max_retries != -1
                    else ""
                )
                logger.error(
                    (
                        "Connection lost, retrying in "
                        f"{self.sleep_time}s...{tries_total_str}"
                    )
                )
                time.sleep(self.sleep_time)


@dataclass
class DriverRunnerAdapter(BaseRunnerAdapter):
    custom_driver: Union[BaseCustomWebdriver, None]
    runner: BaseRunner

    def run(self) -> None:
        if self.custom_driver:
            self.custom_driver.init_driver()
            self.runner.set_driver(self.custom_driver.get_driver())
        logger.info(f"{self.runner.__class__.__name__}: Started successfully")
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
                    (
                        f"{self.runner.__class__.__name__}: "
                        f"Exception found{retries_str}"
                    ),
                    exc_info=e,
                )
            tries += 1
        if tries == self.runner.max_retries:
            logger.error(
                f"{self.runner.__class__.__name__}: Exited after max retries"
            )
        else:
            logger.info(
                f"{self.runner.__class__.__name__}: Exited successfully"
            )

        if self.custom_driver:
            self.custom_driver.get_driver().quit()
