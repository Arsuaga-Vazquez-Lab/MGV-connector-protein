use strict;
use warnings;

my $output = $ARGV[0];
`echo "" > $output`;

open my $fh, '>>', $output or die "Could not open file '$output' $!";
my @files = glob "*.pdb.gz";

decompress all files with gzip
for my $file (@files) {
    `gzip -d $file`;
}

for my $file1 (@files) {
    for my $file2 (@files){
        if ($file1 ne $file2) {
            print("Comparing $file1 and $file2\n")
            my $cmd = "TMalign $file1 $file2";
            print $fh `$cmd`;
        }
    }
}

compress all files
for my $file (@files) {
    `gzip $file`;
}
close $fh;