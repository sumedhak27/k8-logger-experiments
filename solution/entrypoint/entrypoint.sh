#! /bin/bash

# Execute the either of the startup script.
# /usr/bin/python3 /opt/cortx/component/logrotate/config/startup.py --config /opt/cortx/component/config.yaml
/usr/bin/python3 /opt/cortx/component/logrotate/cron/startup.py --config /opt/cortx/component/config.yaml

# start the crond service
/usr/sbin/crond start

# call to the original entrypoint of a component logger in this case.
/usr/bin/python3 /opt/cortx/component/logger.py
