#! /usr/bin/perl
print "Content-type: text/html\n\n";
print "Start VirtualBox instance...<br />";
print "<html>";
print "<head>";
print "<meta http-equiv=\"Content-Type\" content~\"text/html;
charset=EUC-JP\">";
print "</head>";
print "<body>";

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

open(IN,"nextIP.txt"); my $nextIP=<IN>; chop $nextIP; close(IN);
print "<br />";

if ($KEY{confcode} == $nextIP) {
  print "Code is confirmed.<br />";
  print    "sudo VBoxManage startvm $KEY{VMNAME} --type headless";
  $results=`sudo VBoxManage startvm $KEY{VMNAME} --type headless`;
  print "$results<br />";
} else {
  print "Confirmation CODE is not much. Try again.<br />";
}

print "<a href=index.cgi> index.cgi</a>";
print "</body>";
print "</html>";
