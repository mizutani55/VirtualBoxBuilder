#! /usr/bin/perl
print "Content-type: text/html\n\n";
print "Start Special VM instance...<br />";
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

  print    "sudo VBoxManage startvm $KEY{VMNAME} --type headless";
  $results=`sudo VBoxManage startvm $KEY{VMNAME} --type headless`;
  print "$results<br />";
  print "$results<br />";

print "<a href=othervmlist.cgi> Go back to select list. othervmlist.cgi</a><br />";
print "<a href=index.cgi> index.cgi</a>";
print "</body>";
print "</html>";
