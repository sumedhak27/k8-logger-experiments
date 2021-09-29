FROM centos:7.9.2009

RUN yum install -y logrotate

# COPY ./log-rotate.conf /etc/logrotate.d/demo-logger

CMD ["/usr/sbin/logrotate", "-v", "-f", "/etc/logrotate.d/demo-logger"]