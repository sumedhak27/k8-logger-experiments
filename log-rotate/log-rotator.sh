#! /bin/bash

count=1
while true
do
    sleep 60
    logrotate -f /etc/logrotate.d/demo-logger
    echo "Rotated the log successfully 📃, count - $count"
    ((count++))
done
