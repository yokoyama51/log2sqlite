#!/bin/sh

gunzip -c $1 | grep '^NorikaeAPI :' | colrm 1 13 |
perl -nle '
{
  my @d=split /,/,$_;
  my $p=join(".",@d[3..$#d-1]);
  my $id=""; if($p=~m/\/ID=([a-zA-Z0-9_\-]*)/) {$id=$1}
  my $fc=""; if($p=~m/\/FC=([0-9]*)/) {$fc=$1}
  if( $id ne "" and $fc ne ""){
  print $id.",".$fc.",".join(",",@d[0..2]).",".$d[$#d].",".$p
  }
}'
