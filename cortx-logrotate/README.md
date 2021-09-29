# Sample Logger with Logrotate enabled

## Quick Description of Files

### log_rollover.conf
- This is a sample logrotate config file with template of log_dir_path instead of actual path.
- This template path in this file will be replaced during runtime.

### component_config.yaml
- This is a sample component configuration file that components create at the end of mini-provisioning stages.
- Log path will be available to component services through this config file at runtime.

### logger.py
- This script simulates a cortx component service which logs at a confiured path.
- The logger performs 3 steps
  1. reads the log_dir_path from component_config.yaml file
  2. replaces the template log_dir_path in log_rollover.conf with that read in first step.
  3. keeps loging to component logging dir/file with sleep time of 5s. 

### cron_entries
- The file has cron entry for cmd that needs to be executed periodically
- The commands can be like
  1. @daily logrotate -f /path/to/logrotate/config_file\
     *OR*
  2. @weekly /shell/script/for/logrotation

### run_on_start.sh
- This shell script simply starts the crond service and starts the logger.

### Dockerfile
- Dockerfile is used to create a image for demo application which runs logger and deploys\
  the cron job to rotate the logs

### deployment.yaml
- The file has k8 Deployment configuration.
- The component-logger image used in the config is built using the Docker file included.

