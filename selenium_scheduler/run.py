import schedule

from selenium_scheduler.classes.runner import BaseRunner, RunnerAdapterManager
from selenium_scheduler.classes.runner.adapters import (
    ConnectionRunnerAdapter,
    DriverRunnerAdapter,
)
from selenium_scheduler.classes.webdriver import CustomWebdriver
from selenium_scheduler.utils.logging import logger


def run_now(runner: BaseRunner) -> None:
    driver = CustomWebdriver(
        headless=runner.headless, cache_session=runner.cache_session
    )
    adapter = ConnectionRunnerAdapter(
        runable=DriverRunnerAdapter(
            runable=None, custom_driver=driver, runner=runner
        ),
        max_retries=runner.conn_max_retries,
    )
    RunnerAdapterManager(adapter=adapter).run()


def sched(runner: BaseRunner, job: schedule.Job) -> None:
    logger.info(f"Job started successfully for {runner.__class__.__name__}")
    job.do(run_now, runner=runner)
