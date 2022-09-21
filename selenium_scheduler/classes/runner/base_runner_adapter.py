from dataclasses import dataclass

from selenium_scheduler.interfaces import Runable


@dataclass
class BaseRunnerAdapter(Runable):
    runable: Runable
