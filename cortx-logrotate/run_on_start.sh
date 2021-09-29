# /bin/bash

echo "executing crond start."
/usr/sbin/crond start
echo "executing looger.py script."
/usr/bin/python3 /opt/cortx/component/logger.py
