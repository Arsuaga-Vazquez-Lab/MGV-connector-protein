#!/usr/bin/perl
use strict;
use warnings;

my $protein_file = $ARGV[0];
my $mgv_file = "data/mgv_proteins.faa.gz";
my $phylo_file = "data/mgv_contig_info.tsv.gz";
my $field = $ARGV[1];
my $length = 23674396;

if ($field eq "order"){
    $field = 11;
}
elsif ($field eq "family"){
    $field = 12;
}
elsif ($field eq "genus"){
    $field = 13;
}


# Read input file and create dictionary in format: (MGV-GENOME-1_1, VPC-1)
open (my $protein_fh, "<", $protein_file) or die "Can't open $protein_file: $!";
my %proteins;
while (my $p_line = <$protein_fh>) {
    chomp $p_line;
    my @p_line = split(/,/, $p_line);
    for (my $i = 1; $i < scalar(@p_line); $i++){
        $proteins{$p_line[$i]} = $p_line[0];
    }
}
close $protein_fh;


# Find proteins in mgv_proteins.faa.gz and grab sequence
$protein_file =~ m/.+(?=\.[^.]+$)/;
my $write_file = "$&"."_out.faa";
`echo "" > $write_file`;
open(my $wfh, '>>', $write_file) or die "Can't open file for writing: $!";
open(my $mgv_fh, '-|', "zcat $mgv_file") or die "Can't open pipe to zcat: $!";
my $print_next = 0; 
my $mgv = 0;

while(my $mgv_line = <$mgv_fh>) {
    chomp $mgv_line;
    if ($mgv_line =~ m/>/){
        $mgv_line =~ m/MGV-GENOME-\d+_\d+/;
        $mgv = $&;
    } 
    # check if $mgv is in %proteins
    if (exists $proteins{$mgv}) {
        print($wfh "$mgv_line\n");
    }
}
close $mgv_fh;
close $wfh;


# Read mgv_contig_info.tsv.gz and create dictionary in format: (MGV-GENOME-1_1, family/ order / genus)
$protein_file =~ m/.+(?=\.[^.]+$)/;
my $write_file_phylo = "$&"."_phylo.csv";
`echo "" > $write_file_phylo`;
open(my $wfh_phylo, '>>', $write_file_phylo) or die "Can't open file for writing: $!";
open(my $phylo_fh, '-|', "zcat $phylo_file") or die "Can't open pipe to zcat: $!";
my %phylo;
while (my $phylo_line = <$phylo_fh>) {
    chomp $phylo_line;
    my @phylo_line = split(/\t/, $phylo_line);
    # get columns 1 and 13
    $phylo{$phylo_line[0]} = $phylo_line[$field];
}
close $phylo_fh;

# foreach my $key (keys %phylo) {
#     print "$key, $phylo{$key}\n";
# }

# Match protein to family
foreach my $key (keys %proteins) {
    $key =~ m/MGV-GENOME-\d+/;
    my $protein_id = $&;
    # print($protein_id);
    if (exists $phylo{$protein_id}) {
        print ($wfh_phylo "$key, $proteins{$key}, $phylo{$protein_id}\n");
    }
}
close $wfh_phylo;

# to run:
# perl scripts/extract.pl [file with list of proteins] [order/family/genus]