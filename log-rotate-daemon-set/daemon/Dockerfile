FROM centos:7.9.2009

RUN yum install -y logrotate && mkdir -p /opt/log-rotator

COPY ./log-rotate.sh /opt/log-rotator/

CMD ["/bin/bash", "/opt/log-rotator/log-rotate.sh"]