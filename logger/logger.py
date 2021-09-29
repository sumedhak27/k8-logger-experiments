#! /usr/bin/python3

import logging
import socket
import time
import os
import sys

# LOG_DIR, LOG_LEVEL should be stored in Config since,
# CORTX services will read these values from the Config.
APP = os.getenv("POD_NAME")
NODE_NAME = os.getenv("NODE_NAME")
LOG_DIR = os.getenv("LOG_DIR")
PER_NODE_DIR = os.getenv("PER_NODE_DIR")
LOG_LEVEL = logging.INFO
HOSTNAME = socket.gethostname().replace('.', '-')
print(APP, LOG_DIR, PER_NODE_DIR)
if PER_NODE_DIR.lower() == "true":
    LOG_DIR = os.path.join(LOG_DIR, NODE_NAME)
LOG_DIR = os.path.join(LOG_DIR, APP)


def initialize_logger():
    log = logging.getLogger(APP)
    log.setLevel(level=LOG_LEVEL)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(level=LOG_LEVEL)
    fh.setFormatter(formatter)
    log.addHandler(fh)
    return log


def infi_logger(logger=None):
    i = 0
    while True:
        logline = f"Logging count {i}"
        if logger:
            logger.info(logline)
        else:
            print(logline)
        time.sleep(5)
        i += 1


if __name__ == "__main__":
    os.makedirs(LOG_DIR, exist_ok=True)
    LOG_FILE = os.path.join(LOG_DIR, HOSTNAME + ".log")
    print(LOG_FILE)
    try:
        logger = initialize_logger()
        infi_logger(logger)
    except KeyboardInterrupt:
        print(f"Stopping the {APP} service.")
        sys.exit(0)
    except Exception as err:
        print(err)
        sys.exit(1)
