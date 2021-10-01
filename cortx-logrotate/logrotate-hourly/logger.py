# /usr/bin/python3

import yaml
import os
import time

config_file = "/opt/cortx/component/component_config.yaml"
rotate_config = "/etc/logrotate.d/log_rollover.conf"
log_dir = ""
lines = []


def read_log_location():
    with open(config_file) as f:
        conf = yaml.load(f, Loader=yaml.loader.SafeLoader)
        log_dir = (conf["log_config"]["log_path"])
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


def replace_temp_log_dir():
    with open(rotate_config, "r") as f:
        lines = f.readlines()
        if "<COMPONENT_LOG_PATH>" in lines[0]:
            lines[0] = lines[0].replace("<COMPONENT_LOG_PATH>", log_dir)

    with open(rotate_config, "w") as f:
        f.truncate()
        f.writelines(lines)
        for line in lines:
            print(line, end="")


def keep_logging_to_file():
    print("writing infinitely to log file ", end="")
    log_file = os.path.join(log_dir, "component.log")
    i = 0
    while True:
        try:
            with open(log_file, 'a') as logf:
                logf.write(f"Logging the Count: {i}\n")
            i += 1
            print(".", end="")
            time.sleep(20)
        except KeyboardInterrupt:
            print()
            exit(0)
        except Exception as err:
            print(err)
            exit(1)


if __name__ == "__main__":
    log_dir = read_log_location()
    print(log_dir)
    print("______________________")
    replace_temp_log_dir()
    print("______________________")
    keep_logging_to_file()
