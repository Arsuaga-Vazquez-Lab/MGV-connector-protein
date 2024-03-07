my @files = glob "*.pdb";
my %metadata;
# $metadata{"file"} = {"molecule" => ["a"], "family" => ["a"]};


for my $file (@files) {
    open my $fh, "<", $file or die "Could not open file: $!";
    $metadata{"$file"} = {"molecule" => [], "family" => []};
    while (my $line = <$fh>) {
        if ($line =~ m/MOLECULE:(.*)|SYNONYM:(.*)/){
            # if $1 not in array
            # check if $1 in array: if not, push
            if (!grep( /^$1$/, @{$metadata{"$file"}{"molecule"}}) & !($1 =~ m/\s\d/) & ($1 ne "")){ 
                push @{$metadata{"$file"}{"molecule"}}, $1;
            }
        }        
        if ($line =~ m/ORGANISM_SCIENTIFIC:(.*)/){
            if (!grep( /^$1$/, @{$metadata{"$file"}{"family"}}) & !($1 =~ m/\s\d/) & ($1 ne "")){ 
                push @{$metadata{"$file"}{"family"}}, $1;
            }        
        }

    }
    close $fh;
}

for my $key (keys %metadata) {
    print($key."\n");
    for my $key2 (keys %{$metadata{$key}}) {
        print("\t".$key2."\n");
        for my $value (@{$metadata{$key}{$key2}}) {
            print("\t\t".$value."\n");
        }
    }
}