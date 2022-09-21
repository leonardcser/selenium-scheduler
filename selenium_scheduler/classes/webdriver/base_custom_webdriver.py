from abc import abstractmethod

from selenium_scheduler.types import UCDriver


class BaseCustomWebdriver:
    @abstractmethod
    def init_driver(self) -> None:
        pass

    @abstractmethod
    def get_driver(self) -> UCDriver:
        pass
