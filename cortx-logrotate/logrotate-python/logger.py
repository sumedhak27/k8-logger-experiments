import logging
from logging.handlers import RotatingFileHandler
import os
import yaml
import time

config_file = "/opt/cortx/component/component_config.yaml"


def read_log_location():
    with open(config_file) as f:
        conf = yaml.load(f, Loader=yaml.loader.SafeLoader)
        log_dir = (conf["log_config"]["log_path"])
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


if __name__ == "__main__":
    i = 0
    log_dir = read_log_location()
    log_file = os.path.join(log_dir, "component.log")
    logger = logging.getLogger('logger-with-rotation')
    handler = RotatingFileHandler(log_file, maxBytes=200, backupCount=10)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    try:
        while True:
            logger.info(f"Logging the count {i}")
            print(".")
            i += 1
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nShutting down the logger.")
        exit(0)
