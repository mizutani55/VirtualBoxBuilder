#/bin/sh
basedir="/home/vboxuser/ppap"
log=$basedir/logs/ppap.batch.log

lines=`cat $basedir/cgi-bin/resources.csv`
date=`date +"%Y-%m-%d-%I-%M-%S"`

while read line
do
	date=`date`
        #if [[ $line =~ master ]]; then
        #        echo $line
        #fi
	arr=( `echo $line | tr -s ',' ' '`)
	echo "<---- Start start all vm master process"  &>> $log
	echo ${arr[1]} &>> $log
	echo $date  &>> $log

	sleep 10
	echo "VBoxManage startvm ${arr[1]}.master --type headless" &>> $log
	      VBoxManage startvm ${arr[1]}.master --type headless  &>> $log
	echo ${arr[1]} &>> $log
	echo "status=$status" &>> $log
	echo $date  &>> $log
	echo "-----> Done start all vm master process"  &>> $log
done <<END
$lines
END
