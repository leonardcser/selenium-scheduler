import time

import schedule


def wait(sleep_time: float = 0.5):
    while True:
        schedule.run_pending()
        time.sleep(sleep_time)
