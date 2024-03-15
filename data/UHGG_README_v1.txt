v1.0 release
------------

Website URL: https://www.ebi.ac.uk/metagenomics/genomes 

* A total of 286,997 prokaryotic genomes from the human gut microbiome were clustered into 4,644 species representatives.
* Taxonomic annotations were generated with the Genome Taxonomy Database. 
* Pan-genome analyses were performed with Roary for all conspecific genomes.
* Functional annotation results generated with eggNOG and InterProScan are available for all genomes. COG and KEGG results were derived from the eggNOG annotations.
* A protein catalogue was produced with all protein coding sequences clustered at 100%, 95%, 90% and 50% amino acid identity.
* Single nucleotide variants (SNVs) were identified with MUMmer for species with at least 3 conspecific genomes.
* A BIGSI search database was built with the species representatives.

## The following files are available for download in each species directory within the uhgg_catalogue/:

- genome/
    * [species_accession].faa : Protein sequence FASTA file of the species representative.
    * [species_accession].fna : DNA sequence FASTA file of the genome assembly of the species representative.
    * [species_accession].gff : Genome GFF file with various sequence annotations.
    * [species_accession]_eggNOG.tsv : eggNOG annotations of the protein coding sequences.
    * [species_accession]_InterProScan.tsv : InterProScan annotation of the protein coding sequences.

## For species where this is more than one conspecific genome, pan-genomes can be found in:
       
- pan-genome/
    * core_genes.faa : Protein sequence FASTA file of core genes (>=90% of the genomes with >=90% amino acid identity).
    * accessory_genes.faa : Protein sequence FASTA file of accessory genes.
    * pan-genome.faa : Protein sequence FASTA file of the pan-genome.
    * pan-genome.fna : Nucleotide sequence FASTA file of the pan-genome.
    * pan-genome_eggNOG.tsv : eggNOG annotations of the pan-genome.
    * pan-genome_InterProScan.tsv : InterProScan annotations of the pan-genome.
    * genes_presence-absence.tsv : Presence/absence binary matrix of the pan-genome across all conspecific genomes.
    * genes_presence-absence_locus.csv : Roary output with general statistics on each gene cluster and the matching locus IDs in the conspecific genomes.
    * mashtree.nwk : Tree generated from the pairwise Mash distances of conspecific genomes.

## Additional files available in the parent directory:

- all_genomes/: Combined GFF/FASTA file (Prokka output) for each of the 286,997 genomes. 

- uhgg_kraken2-db : Kraken 2 and Bracken database files generated from the species representative genomes using the GTDB taxonomy.

- genomes-all_metadata.tsv : Assembly statistics and metadata of all 286,997 genomes.

- genomes-nr_metadata.tsv: Assembly statistics and metadata of 204,938 non-redundant genomes (dereplicated at 99.9% ANI and excluding more than one genome per species per sample).

- bigsi_search/
    * human-gut.bigsi : BIGSI search database of the species representatives.
    * human-gut.yaml : Configuration file used to generate/search the BIGSI database.

- uhgp_catalogue/
    * uhgp-XX.tar.gz
        - uhgp-XX.faa : Protein FASTA file of the clustered, representative sequences.
        - uhgp-XX.tsv : Cluster membership of all the protein sequences.
        - uhgp-XX_eggNOG.tsv : eggNOG annotation results of the protein catalogue.
        - uhgp-XX_InterProScan.tsv : InterProScan annotation results of the protein catalogue.
        - uhgp-XX_hq.faa : High-quality subset of the protein catalogue with clusters where at least two proteins from independent genomes were retrieved from the same species.
        - uhgp-XX_hq.tsv : Cluster membership of the high-quality protein catalogue. 

- snv_catalogue/
    * [species_accession]_SNVs.tsv.tar.lz4 : SNV positions and alleles (0 = reference, 1 = alternate, 255 = missing) in relation to the species representative genome.

- phylogenies/
    * ar122_alignment.faa : Protein sequence alignment of 122 marker genes across all archaeal species.
    * ar122_iqtree.nwk :  Newick tree file of the archaeal species generated with IQ-TREE.
    * bac120_alignment.faa : Protein sequence alignment of 120 marker genes across all bacterial species.
    * bac120_iqtree.nwk : Newick tree file of the bacterial species generated with IQ-TREE.
