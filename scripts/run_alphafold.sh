#!/bin/bash


for file in ./consensus/*; do
	# runs AlphaFold on all files in consensus folder
    echo "Processing file: $file"
	run_alphafold_docker --fasta_paths=$file --data_dir=/media/raid/alphafold/reduced_dbs --output_dir=/media/raid/chsieh/alphafold/output/ --max_template_date=2022-01-01 --db_preset=reduced_dbs 
done

run_alphafold_docker --fasta_paths=/media/raid/chsieh/alphafold/consensus/VPC-99060_consensus.fasta --data_dir=/media/raid/alphafold/reduced_dbs --output_dir=/media/raid/chsieh/alphafold/output/ --max_template_date=2022-01-01 --db_preset=reduced_dbs 

