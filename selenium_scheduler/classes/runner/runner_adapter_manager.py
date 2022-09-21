from dataclasses import dataclass

from selenium_scheduler.classes.runner import BaseRunnerAdapter
from selenium_scheduler.interfaces import Runable


@dataclass
class RunnerAdapterManager(Runable):
    adapter: BaseRunnerAdapter

    def run(self):
        self.adapter.run()
