#! /usr/bin/perl
use strict;
use Text::CSV_XS;
my $csv = Text::CSV_XS->new ({ binary => 1 });
open my $fh, "<", "resources.csv";

my $basedir="/home/vboxuser/ppap/master/";

print "Content-type: text/html\n\n";
print "<html>";
print "<head>";
print "<meta http-equiv=\"Content-Type\" content~\"text/html; charset=EUC-JP\">";
print "</head>";
print "<body>";

print "<H1>Create VM Machine.</H1>";
print "<p>Select master OS type:<br>";
print "<form method=\"get\" action=\"/cgi-bin/importvm.cgi\">";


while (my $master = $csv->getline ($fh)) {
  #print "$$master[0]\, ";
  #print "$$master[1]\, "; #mastefilename
  #print "$$master[2]";
  #print "$$master[3]\, ";
  #print "$$master[4]\, ";
  #print "$$master[5]\, ";
  #print "<br />";


  print "<input type=\"radio\" name=\"MASTERNO\" value=\"$$master[0]\" />
    $$master[2]
    $$master[3]
    $$master[4]
    $$master[5]
    $$master[6]
  ";

  print "<br />";
}

print "<br />";
print  "Your e-mail: <textarea name=\"email\" cols=20 rows=1>";
print "</textarea>";
print "</p>";

print "It may takes about 10 min. to use the VMmachine.<br />";
print "Please check your email when your VMmaschine become ready.<br .>";

print "<input type=\"submit\" name=\"submit\" value=\"CreateVM\"><br />";
print "<br />";
print "<a href=index.cgi> index.cgi</a>";
print "</form>";
print "</body>";
print "</html>";

$csv->eof;
close $fh;
