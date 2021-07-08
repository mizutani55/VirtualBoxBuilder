#!/bin/bash
#echo "importvm.sh [mastername] [vmname] [nextIP] [RAM SIZE(MB)] [email]
args=("$@")

basedir="/home/vboxuser/ppap"
log="$basedir/logs/ppap.log"
baseIP="192.168.31."
bccemail="t.mizutani@aos.com"
#default for GET parameter.#
masterName=${args[0]}
#masterName="Windows7.Pro.32bit.normal"
vmname=${args[1]}
nextIP=${args[2]}
preMACadd="08002780F"
vmram=${args[3]} #MB
#vmram="1025" #MB
email=${args[4]}
echo "email=$email"  &>> $log
#email="t.mizutani@aos.com"


#Prepair for log
base=${0##*/} 
echo "----$base start----" &>> $log
date=`date +"%Y/%M/%D/%T"`;echo $date &>> $log
echo $@ &>> $log

echo \
"VBoxManage import $basedir/master/$masterName.ova \
--vsys 0 --vmname $masterName.$nextIP" &>> $log 2>&1

VBoxManage import $basedir/master/$masterName.ova \
--vsys 0 --vmname "$masterName.$nextIP" &>> $log 2>&1

sleep 30

VBoxManage showvminfo --details "$masterName.$nextIP" &>> $log 2>&1

echo "increase nextIP=$nextIP+1" &>> $log
IP=$(($nextIP+1)) 
echo $IP>$basedir/bin/nextIP.txt
cat $basedir/bin/nextIP.txt &>> $log

sleep 30

echo \
"VBoxManage modifyvm \"$masterName.$nextIP\" \
  --macaddress1 \"$preMACadd$nextIP\" \
  --memory "$vmram" \
  --description "$email/$date"  "&>> $log 2>&1

VBoxManage modifyvm "$masterName.$nextIP" \
  --macaddress1 "$preMACadd$nextIP" \
  --memory "$vmram" \
  --description "$email/$date" &>> $log 2>&1

VBoxManage startvm "$masterName.$nextIP" --type headless &>> $log 2>&1


#email="mizuttsu@hotmail.com"
#masterName="Windows7"
#nextIP="174"

sendmail -t <<EOF
Subject: Ready to use VMMachine IP:$baseIP$nextIP
To:$email
Bcc:$bccemail
Hi,

RDP information for the VMMachine.

IP: $baseIP$nextIP
VMname: $vmname

RDPUser: aosdata or Administrator(ServerOS)
Pass: Ask AOS Staff.

Create date: `date`
Support:
EOF


echo "$date" &>> $log 2>&1
echo "----$base done.----" &>> $log 2>&1
