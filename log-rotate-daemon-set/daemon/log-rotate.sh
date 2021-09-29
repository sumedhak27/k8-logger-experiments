#! /bin/bash

set -euo pipefail

# Gracefully handle the TERM signal sent while deleting the DaemonSet
trap 'exit' TERM

# Rotate the log files
/usr/sbin/logrotate -v -f /etc/logrotate.d/demo-logger

# Inform that logrotate cmd is executed by logging done
echo "done"

# Sleep till DaemonSet is not deleted, to avoid
# restart of container as per RestartPolicy of DaemonSet
while true
do
    sleep 1
done
