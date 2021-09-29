#! /bin/bash

# rotate csm logs
/usr/sbin/logrotate -v -f /opt/log-rotator/csm.conf

# rotate hare logs
/usr/sbin/logrotate -v -v /opt/log-rotator/hare.conf

# rotate utils logs
/usr/sbin/logrotate -v -v /opt/log-rotator/utils.conf

# rotate s3 logs
/bin/bash sh /opt/log-rotator/s3logfilerollover.sh  # for s3-server
# call script to rotate s3authserver logs
# call script to rotate s3backgrounddelete logs

# rotate motr logs
/bin/bash sh /opt/log-rotator/m0trace_logrotate.sh
/bin/bash sh /opt/log-rotator/m0addb_logrotate.sh
