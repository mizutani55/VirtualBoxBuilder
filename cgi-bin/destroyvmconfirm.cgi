#! /usr/bin/perl
print "Content-type: text/html\n\n";
print "Destory VirtualBox instance...<br />";
print "<html>";
print "<head>";
print "<meta http-equiv=\"Content-Type\" content~\"text/html;
charset=EUC-JP\">";
print "</head>";
print "<body>";

print "<form method=\"get\" action=\"/cgi-bin/destroyvm.cgi\">";

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


print "You selected. : " ;
print "<h2>$KEY{VMNAME}</h2>";
print "<br />";

open(IN,"nextIP.txt"); my $nextIP=<IN>; chop $nextIP; close(IN);
print "Confirmation CODE <h2>$nextIP</h2>";
print $KEY{VMNAME};
print  "Please enter confirmation3 digit CODE: on this page<br />
<textarea name=\"confcode\" cols=4 rows=1>";
print "</textarea>";
print "<br />";

#    print "sudo VBoxManage controlvm $KEY{OS} acpipowerbutton";
#    $results = `sudo VBoxManage controlvm $KEY{OS} acpipowerbutton`;
#    print "$results<br />";

print "<input type=\"hidden\" name=\"VMNAME\" value=$KEY{VMNAME}>";
print "<input type=\"hidden\" name=\"email\"  value=$KEY{email}>";

print "Are you sure? " ;
print "<input type=\"submit\" name=\"submit\" value=\"DestoryVM\"><br />";

print "<br />";
print "<a href=index.cgi> index.cgi</a>";
print "</body>";
print "</html>";
