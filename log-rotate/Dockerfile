FROM centos:7.9.2009

RUN yum install -y logrotate

RUN mkdir -p /opt/demoLogger

COPY ./log-rotator.sh /opt/demoLogger
COPY ./log-rotate.conf /etc/logrotate.d/demo-logger

ENTRYPOINT ["/bin/bash", "/opt/demoLogger/log-rotator.sh"]
