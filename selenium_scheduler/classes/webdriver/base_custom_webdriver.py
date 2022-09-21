from abc import abstractmethod

from selenium_scheduler.types import UCDriver


class BaseCustomWebdriver:
    @abstractmethod
    def init_driver(self) -> None:
        pass

    @abstractmethod
    def get_driver(self) -> UCDriver:
        pass

    # @abstractmethod
    # def __enter__(self):
    #     pass

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if issubclass(exc_type, Exception):
    #         raise exc_type(exc_val, exc_tb)
