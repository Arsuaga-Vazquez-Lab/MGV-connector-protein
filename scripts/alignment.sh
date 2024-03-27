#!/bin/bash
filepath="../Annotations/connector"

if [ ! -d "$filepath/msa" ]; then
    mkdir "$filepath/msa"
fi
echo "$filepath/msa"

for file in ./vpc/*; do
    filename=$(basename "$file" .faa)
    # echo "$filename.faa, $filename.msa"
    clustalo -i "$filepath/vpc/$filename.faa" -o "$filepath/msa/$filename.fasta" -v
done
