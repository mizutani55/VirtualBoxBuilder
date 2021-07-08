#/bin/sh
basedir="/home/vboxuser/ppap"
log=$basedir/logs/ppap.batch.log

lines=`cat $basedir/cgi-bin/resources.csv`
#date=`date`
date=`date +"%Y-%m-%d-%I-%M-%S"`
#Prepair previous master to  archives
archivedir="home/archive/ppap"
mkdir $basedir/master/$date
mv    $basedir/master/*.ova $basedir/master/$date

while read line
do
	date=`date`
        #if [[ $line =~ master ]]; then
        #        echo $line
        #fi
	arr=( `echo $line | tr -s ',' ' '`)
	echo "<---- Start export proceess."   &>> $log
	echo ${arr[1]} &>> $log
	echo $date  &>> $log
	echo "VBoxManage controlvm ${arr[1]}.master acpipowerbutton" &>> $log
	      VBoxManage controlvm ${arr[1]}.master acpipowerbutton &>> $log
	sleep 10
	      VBoxManage controlvm ${arr[1]}.master acpipowerbutton &>> $log
	sleep 20
	echo  "VBoxManage controlvm ${arr[1]}.master poweroff" &>> $log
	       VBoxManage controlvm ${arr[1]}.master poweroff &>> $log
	sleep 10
	#### Start to check status the terget vm  ####
	i=0
        while :
         do
	  sleep 1
	  echo "master=${arr[1]}.master" &>> $log
	  status=`VBoxManage showvminfo ${arr[1]}.master |grep State | cut  -d ' ' -f 12` &>> $log
          if [ $status != "running" ]; then 
	    echo "status=$status" &>> $log
	    echo "start to export vm." &>> $log
            echo "VBoxManage export ${arr[1]}.master -o $basedir/master/${arr[1]}.ova" &>> $log
                  VBoxManage export ${arr[1]}.master -o $basedir/master/${arr[1]}.ova  &>> $log
	    break
          fi
	  if [ $i -gt 9 ]; then break;
	   else let i++
	   echo "Machine is  still sunning... tyr again." &>> $log
	   echo "count i=$i" &>> $log
	  fi
	  echo "can not shutdown  ${arr[1]}.master abort process." &>> $log 
        done
	#sleep 1
	#echo "VBoxManage startvm ${arr[1]}.master --type headless" &>> $log
	#     VBoxManage startvm ${arr[1]}.master --type headless  &>> $log
	#echo ${arr[1]} &>> $log
	echo "status=$status" &>> $log
	echo $date  &>> $log
	echo "-----> Done export process"  &>> $log
done <<END
$lines
END

