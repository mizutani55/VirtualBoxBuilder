#! /usr/bin/perl
print "Content-type: text/html\n\n";
print "<html>";
print "<head>";
print "<meta http-equiv=\"Content-Type\" content~\"text/html;charset=EUC-JP\">";
my $str = << "EOF";
Welcome main menu PPAP (Ploofing Platform for AOS Products.)<br />
<a href="importvmlist.cgi">1. select master OS and Create VM</a><br />
<a href="startvmlist.cgi">2. select and START VM</a><br />
<a href="stopvmlist.cgi">3. select and STOP VM</a><br />
<a href="destroyvmlist.cgi">4. select and DESTROY VM(NotReady)</a><br />
<br />
<a href="advmlist.cgi">10. ActiveDirectory machine VM(for AOS staff only)</a><br />
<a href="othervmlist.cgi">11. Other special machine(for AOS staff only)</a><br />
EOF

print "$str";
