#/bin/sh
basedir="/home/vboxuser/ppap"
log=$basedir/logs/ppap.batch.log

date=`date +"%Y-%m-%d-%I-%M-%S"`
#Prepair previous master to  archives
archivedir="/home/arcvhive/ppap"

cat $basedir/cgi-bin/resources.other.csv | while read line
do
echo $line
	date=`date`
        #fi
	#arr=( `echo $line` )
	echo "<---- Start export proceess."   &>> $log
	echo $line  &>> $log
	echo $date  &>> $log

	echo "VBoxManage controlvm $line acpipowerbutton" &>> $log
	      VBoxManage controlvm $line acpipowerbutton &>> $log
	sleep 10
	      VBoxManage controlvm $line acpipowerbutton &>> $log
	sleep 20
	echo  "VBoxManage controlvm $line poweroff" &>> $log
	       VBoxManage controlvm $line poweroff &>> $log
	sleep 10
	#### Start to check status the terget vm  ####
	i=0
        while :
         do
	  sleep 1
	  echo "master=$line" &>> $log
	  status=`VBoxManage showvminfo $line |grep State | cut  -d ' ' -f 12` &>> $log
	  echo "status=$status" &>> $log
          if [ $status != "running" ]; then 
	    echo "status=$status" &>> $log
	    echo "start to export vm." &>> $log
            echo "VBoxManage export $line -o $basedir/master/$line.ova" &>> $log
                  VBoxManage export $line -o $basedir/master/$line.ova  &>> $log
	    break
          fi
	  if [ $i -gt 9 ]; then break;
	   else let i++
	   echo "Machine is  still sunning... tyr again." &>> $log
	   echo "count i=$i" &>> $log
	  fi
	  echo "can not shutdown  $line abort process." &>> $log 
        done
	echo "status=$status" &>> $log
	echo $date  &>> $log
	echo "-----> Done export process"  &>> $log
done

