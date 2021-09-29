# /bin/bash

# mkdir -p /opt/cortx/component/
# cp /home/752264/demoLogger/cortx-logrotate/component_config.yaml /opt/cortx/component/
component_config='/opt/cortx/component/component_config.yaml'
log_location=`cat $component_config | grep log_path | cut -d: -f2 | sed 's/ *$//g'`
echo $log_location
mkdir -p $log_location
log_file=`echo "$log_location/component.log"`
echo $log_file
touch $log_file
chmod 777 $log_file
i=0
while true
do 
  echo "Logging the count: $i" >> "$log_file"
  sleep 5
  ((i++))
done