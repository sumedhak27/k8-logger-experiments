#! /usr/bin/python3

import yaml
import os
import shutil

config_file = "/opt/cortx/component/component_config.yaml"
max_file_count = 4


def read_log_location():
    with open(config_file) as f:
        conf = yaml.load(f, Loader=yaml.loader.SafeLoader)
        log_dir = (conf["log_config"]["log_path"])
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


if __name__ == "__main__":
    max_i = min_i = 0
    log_dir = read_log_location()
    log_file = os.path.join(log_dir, "component.log")
    if os.stat(log_file).st_size == 0:
        exit(0)
    for root, dirs, files in os.walk(log_dir):
        for file in files:
            if file[-1].isdigit() and int(file[-1]) > max_i:
                max_i = int(file[-1])
        print(max_i)
        # copy truncates the log file.
        shutil.copyfile(log_file, f"{log_file}.{max_i+1}")
        with open(log_file, 'w') as logf:
            logf.truncate()
        # rollover is not implemented.
