#!/usr/bin/perl
use strict;
use warnings;

my $protein_file = $ARGV[0];
my $mgv_file = $ARGV[1];
my $output_file = $ARGV[2];
my $length = 23674396;
my $num_proteins = `grep -o "MGV" $protein_file | wc -l`;

print("Number of proteins: ".$num_proteins."\n");

# read file
open my $wfh, '>>', $output_file or die "Can't open file for writing: $!";
open my $fh, '-|', "zcat $mgv_file" or die "Can't open pipe to zcat: $!";
my $index = 0;
my $x = "";
while (my $line = <$fh>) {
    $line=~ m/MGV-GENOME-\d+_\d+/;
    my $mgv = $&;
    if (defined $mgv) {
        $x = `grep -A1 $mgv $protein_file`;
    }
    if ($x) {
        $x =~ m/VPC-\d+/;
        my $vpc = $&;
        if ($line =~ m/^>/){
            # print($vpc.",".$line);
            print $wfh $vpc.",".$line;
        }
        else{
            # print($line);
            print $wfh $line;
        }
    }
    $index++;
    if ($index % 1000 == 0) {
        print($index."/".$length."\n");
        if (`grep -o "MGV" $output_file | wc -l` == $num_proteins){
            last;
        }
    }
}

close $fh;
close $wfh;
