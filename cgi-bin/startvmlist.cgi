#! /usr/bin/perl
print "Content-type: text/html\n\n";
print "Select to Start VM instance...<br />";
print "<html>";
print "<head>";
print "<meta http-equiv=\"Content-Type\" content~\"text/html; charset=EUC-JP\">";
print "</head>";
print "<body>";

print "<form method=\"get\" action=\"/cgi-bin/startvmconfirm.cgi\">";

if ($ENV{'REQUEST_METHOD'} eq "POST") {
read(STDIN, $string, $ENV{'CONTENT_LENGTH'});
}else { $string = $ENV{'QUERY_STRING'};
}
@pairs = split(/&/,$string);
foreach $pair (@pairs)
{
 ($name, $value) = split(/=/, $pair);
 $value =~ tr/+/ /;
 $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
 $KEY{$name} = $value;
}

@runningvms=`sudo VBoxManage list vms`;
foreach (@runningvms) {
 ($a, $vmname) = split(/\"|\s/, $_);
 $descript = `sudo VBoxManage showvminfo --details $vmname |grep -A 1 -n "Description:"` ;
 #print "$vmname,$descript";
 #print "----------\n";
 if ($descript=~/master/) {
 } else {
   print "<input type=\"radio\" name=\"VMNAME\" value=\"$vmname\" />
   $vmname :
   $descript Created.<br />
   ";
 }

}
print "<br />";

print  "Enter your e-mail: <textarea name=\"email\" cols=20 rows=1>";
print "</textarea>";
print "</p>";

print "<input type=\"submit\" name=\"submit\" value=\"GotoNext\">";
print "</form>";
print "<br />";

#    print "sudo VBoxManage controlvm $KEY{OS} acpipowerbutton";
#    $results = `sudo VBoxManage controlvm $KEY{OS} acpipowerbutton`;
#    print "$results<br />";


print "<a href=index.cgi> index.cgi</a>";
print "</body>";
print "</html>";
