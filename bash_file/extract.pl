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

# for testing: print dictionary
# foreach my $key (keys %proteins) {
#     print "$key, $proteins{$key}\n";
# }

# Find proteins in mgv_proteins.faa.gz and grab sequence
open(my $mgv_fh, '-|', "zcat $mgv_file") or die "Can't open pipe to zcat: $!";
my $print_next = 0; 

while(my $mgv_line = <$mgv_fh>) {
    chomp $mgv_line;
    $mgv_line =~ m/MGV-GENOME-\d+_\d+/;
    my $mgv = $&;
    if (defined $mgv){
        if (exists $proteins{$mgv}) {
            # print ("$mgv, $proteins{$mgv}\n");
            print ($proteins{$mgv}, $mgv_line."\n");
            $print_next = 1;
        }
    }
    else{
        if ($print_next){
            # print ($wfh, $mgv_line."\n");
            print ($mgv_line."\n");
            $print_next = 0;
        }
    }
}
close $mgv_fh;
close $wfh;

# Read mgv_contig_info.tsv.gz and create dictionary in format: (MGV-GENOME-1_1, family)
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
        print ("$key, $proteins{$key}, $phylo{$protein_id}\n");
    }
}

# to run:
# perl bash_file/extract.pl [file with list of proteins] [order/family/genus]