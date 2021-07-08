#! /usr/bin/perl
#use strict;
use Text::CSV_XS;
my $csv = Text::CSV_XS->new ({ binary => 1 });

print "Content-type: text/html\n\n";
print "Imprt VirtualBox instance...<br />";
print "<html>";
print "<head>";
print "<meta http-equiv=\"Content-Type\" content~\"text/html;charset=EUC-JP\">";
print "</head>";
print "<body>";

my $basedir = "/home/vboxuser/ppap";
my $preMACadd="08002780F";
#my $nextIP="172"; 
open(IN,"nextIP.txt"); my $nextIP=<IN>; chop $nextIP; close(IN);
my $vmram="1024"; #MB
my $string="";

if ($ENV{'REQUEST_METHOD'} eq "POST") { 
 read(STDIN, $string, $ENV{'CONTENT_LENGTH'}); 
}else {$string = $ENV{'QUERY_STRING'}; 
}
my @pairs = split(/&/,$string);
foreach my $pair (@pairs)
{
 (my $name, my $value) = split(/=/, $pair);
  $value =~ tr/+/ /;
  $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
  $KEY{$name} = $value;
}

#print "MasterIndexNo.=$KEY{MASTERNO}<br />";
#print "IP=$nextIP<br />";
#print "email=$KEY{email}<br />";
#print "vmram=$KEY{vmram}l<br />";
print "Please wait 10min-. An email will send to you with RDP informations.<br />";

open my $fh, "<", "resources.csv";
while (my $master = $csv->getline ($fh)) {
  if ($$master[0] == $KEY{MASTERNO}) {
    #print "$$master[0]\, ";
    #print "$$master[1]"; #mastefilename
    $tergetOS=$$master[1];
    $VMName="$$master[2]$$master[3]$$master[4]$$master[5]$$master[6]$$master[7]";
    $vmram = "$$master[8]";
    #print "$tergetOS ";
    #print "<br />";
    #print "$VMName";
    #print "$VMName";
    #print "<br />";
  }
}

print "<a href=index.cgi> index.cgi</a>";
print "</body>";
print "</html>";

#print "$basedir/bin/importvm.sh \"$tergetOS\"  \"$VMName.$nextIP\" \"$nextIP\" \"$vmram\" \"$KEY{email}\"";


#print "
$results = `
  sudo $basedir/bin/importvm.sh \"$tergetOS\"  \"$VMName.$nextIP\" \"$nextIP\" \"$vmram\" \"$KEY{email}\"&
`;
#";
#print "$results<br />";
