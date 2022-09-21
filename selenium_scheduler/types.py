from typing import Protocol

import undetected_chromedriver as uc

UCDriver = uc.Chrome


class RunCallback(Protocol):
    def __call__(self, driver: UCDriver) -> None:
        ...
