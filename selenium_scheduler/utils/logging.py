import logging
import sys

logger = logging.getLogger("selenium_scheduler_logger")

handlers = [logging.FileHandler("logs.log"), logging.StreamHandler(sys.stdout)]
formatter = logging.Formatter("%(asctime)s - [%(levelname)s] %(message)s")

for h in handlers:
    h.setFormatter(formatter)
    logger.addHandler(h)

logger.setLevel(logging.DEBUG)
