v2.0.1 release
------------

Website URL: https://www.ebi.ac.uk/metagenomics/genome-catalogues/human-gut-v2-0

* A total of 289,232 prokaryotic genomes from the human gut microbiome were clustered into 4,744 species representatives.
* Taxonomic annotations were generated with the Genome Taxonomy Database r202. 
* Pan-genome analyses were performed with Panaroo v1.2.8 for all conspecific genomes.
* Functional annotation results generated with eggNOG (emapper-2.1.3) and InterProScan v5.39-77.0 are available for the genomes of all species representatives. COG and KEGG results were derived from the eggNOG annotations.
* A protein catalogue was produced with all protein coding sequences clustered at 100%, 95%, 90% and 50% amino acid identity.


## The following files are available for download in each species directory within the species_catalogue/:

- genome/
    * [species_accession].faa : Protein sequence FASTA file of the species representative.
    * [species_accession].fna : DNA sequence FASTA file of the genome assembly of the species representative.
    * [species_accession].gff : Genome GFF file with various sequence annotations.
    * [species_accession]_eggNOG.tsv : eggNOG annotations of the protein coding sequences.
    * [species_accession]_InterProScan.tsv : InterProScan annotation of the protein coding sequences.
    * [species_accession]_rRNAs.fasta : rRNA sequence FASTA file for the species representative.


## For species where there is more than one conspecific genome, pan-genomes can be found in:
       
- pan-genome/
    * core_genes.txt : List of core genes for the pan-genome (genes found in >=90% of the genomes).
    * pan-genome.fna : Nucleotide sequence FASTA file of the pan-genome.
    * gene_presence_absence.Rtab : Presence/absence binary matrix of the pan-genome across all conspecific genomes.
    * mashtree.nwk : Tree generated from the pairwise Mash distances of conspecific genomes.


## Additional files available in the parent directory:

- all_genomes/: Combined GFF/FASTA file (Prokka output) for each of the 289,232 genomes. 

- kraken2_db_uhgg_v2.0.1 : Kraken 2 and Bracken database files generated from the species representative genomes using the GTDB taxonomy.

- all_genomes.msh: mash sketch for all 289,232 genomes.

- genomes-all_metadata.tsv : Assembly statistics and metadata of all 289,232 genomes.

- protein_catalogue/
    * uhgp-XX.tar.gz
        - uhgp-XX.faa : Protein FASTA file of the clustered, representative sequences.
        - uhgp-XX.tsv : Cluster membership of all the protein sequences.
	For 90% identity catalog only:
        - uhgp-90_eggNOG.tsv : eggNOG annotation results of the protein catalogue.
        - uhgp-90_InterProScan.tsv : InterProScan annotation results of the protein catalogue.


## Changes in release v2.0.2 since v2.0.1

Bug fix: fixed assembly statistics errors in the metadata table. The errors affected four columns: assembly length, number of contigs, GC content, and N50.

## Changes in release v2.0.1 since v2.0

Bug fix: fixed a kraken2 database error where all unknown species were assigned to the same genus. In the current version of the kraken2 database, if a species is not known in GTDB, it is assigned the MGnify genome accession as its taxon name instead of "Unknown species".

Added a folder containing phylogenetic trees for bacterial and archaeal genomes and associated multiple-sequence alignment files:
- phylogenies/: 
    * ar122_iqtree.nwk : A phylogenetic tree for archaeal genomes in Newick format.
    * bac120_iqtree.nwk : A phylogenetic tree for bacterial genomes in Newick format.
    * ar122_alignment.faa.gz : A multiple sequence alignment for archaeal genomes.
    * bac120_alignment.faa.gz : A multiple sequence alignment for bacterial genomes.

## Changes in release v2.0 since v1.0

* Genomes that are likely to contain chimeric sequences were identified using GUNC v1.0.1. The following genomes were removed from the catalog as likely containing chimeric sequences:

GUT_GENOME007158
GUT_GENOME010067
GUT_GENOME019023
GUT_GENOME024279
GUT_GENOME069124
GUT_GENOME085404
GUT_GENOME093918
GUT_GENOME095599
GUT_GENOME116624
GUT_GENOME125804
GUT_GENOME127408
GUT_GENOME138473
GUT_GENOME138794
GUT_GENOME157017
GUT_GENOME170556
GUT_GENOME172433
GUT_GENOME218106
GUT_GENOME219168
GUT_GENOME219438
GUT_GENOME225144
GUT_GENOME227599
GUT_GENOME231710
GUT_GENOME236231
GUT_GENOME236239
GUT_GENOME236882
GUT_GENOME237015
GUT_GENOME237450
GUT_GENOME237519
GUT_GENOME283609

* Contigs that are likely to have been derived from the host genome were identified using BLAST. The following contigs were removed from their respective genomes:

GUT_GENOME027317_228
GUT_GENOME076199_17
GUT_GENOME076199_9
GUT_GENOME095971_12
GUT_GENOME096049_35
GUT_GENOME096049_41
GUT_GENOME096271_27
GUT_GENOME096271_29
GUT_GENOME096271_38
GUT_GENOME096401_41
GUT_GENOME096402_70
GUT_GENOME186046_274
GUT_GENOME226031_31
GUT_GENOME226031_35
GUT_GENOME231320_10
GUT_GENOME231320_12
GUT_GENOME231320_13
GUT_GENOME231320_14
GUT_GENOME231320_15
GUT_GENOME231320_19
GUT_GENOME231320_21
GUT_GENOME231320_23
GUT_GENOME231320_25
GUT_GENOME231320_26
GUT_GENOME231320_3
GUT_GENOME231320_33
GUT_GENOME231320_38
GUT_GENOME231320_4
GUT_GENOME231320_44
GUT_GENOME231436_1433
GUT_GENOME231436_1450
GUT_GENOME231722_1
GUT_GENOME231722_10
GUT_GENOME231722_11
GUT_GENOME231722_12
GUT_GENOME231722_13
GUT_GENOME231722_14
GUT_GENOME231722_15
GUT_GENOME231722_18
GUT_GENOME231722_19
GUT_GENOME231722_2
GUT_GENOME231722_20
GUT_GENOME231722_22
GUT_GENOME231722_23
GUT_GENOME231722_25
GUT_GENOME231722_28
GUT_GENOME231722_4
GUT_GENOME231722_7
GUT_GENOME231722_9
GUT_GENOME232084_3
GUT_GENOME232145_13
GUT_GENOME232145_2
GUT_GENOME232145_25
GUT_GENOME232145_29
GUT_GENOME232145_45
GUT_GENOME232145_9
GUT_GENOME237056_218
GUT_GENOME237839_164
GUT_GENOME243998_237
GUT_GENOME243998_290
GUT_GENOME243998_293
GUT_GENOME243998_301
GUT_GENOME243998_317
GUT_GENOME243998_330
GUT_GENOME243998_340
GUT_GENOME243998_353
GUT_GENOME243998_364
GUT_GENOME243998_374
GUT_GENOME243998_382
GUT_GENOME243998_384
GUT_GENOME243998_392
GUT_GENOME243998_397
GUT_GENOME243998_437
GUT_GENOME243998_438
GUT_GENOME243998_439

* All genomes were assigned accession numbers starting with MGYG. Original accession numbers for all genomes as well as their new assigned accession numbers are provided in genomes-all_metadata.tsv.

* For genomes that were assigned MGYG accession numbers in v1.0, the format of the accession number has changed from MGYG-HGUT-XXXXX to MGYGXXXXXXXXX. However, the assigned number did not change between the catalog versions. For example, a genome with the accession number MGYG-HGUT-00110 in v1.0 of the catalog will have the accession number MGYG000000110 in v2.0.

* Genomes from which host contigs had been removed were assigned accession numbers ending in ".1" to indicate a new genome version.

* 2,426 MAGs from study PRJEB37358 and 3,452 isolate genomes from study PRJNA544527 were added to the catalog. This resulted in 129 new species and 2135 new strains.  

* For 132 species identified in the previous version of the catalog and containing more than one conspecific genome, the species representative genome has been replaced with a newly added strain. The replaced species representative genomes, the new species representatives and the reason for replacement are listed below:

GUT_GENOME032708	MGYG000004647	Better quality MAG
GUT_GENOME206032	MGYG000004648	Better quality MAG
GUT_GENOME059449	MGYG000004650	Better quality MAG
GUT_GENOME245868	MGYG000004651	MAG replaced by an isolate genome
GUT_GENOME225852	MGYG000004652	MAG replaced by an isolate genome
GUT_GENOME037499	MGYG000004653	Better quality MAG
GUT_GENOME274864	MGYG000004655	Better quality MAG
GUT_GENOME105006	MGYG000004656	Better quality MAG
GUT_GENOME111543	MGYG000004658	MAG replaced by an isolate genome
GUT_GENOME017603	MGYG000004659	Better quality MAG
GUT_GENOME126693	MGYG000004662	Better quality MAG
GUT_GENOME093693	MGYG000004663	Better quality MAG
GUT_GENOME138463	MGYG000004664	Better quality MAG
GUT_GENOME045330	MGYG000004666	MAG replaced by an isolate genome
GUT_GENOME158031	MGYG000004671	Better quality MAG
GUT_GENOME155428	MGYG000004673	Better quality MAG
GUT_GENOME207897	MGYG000004678	MAG replaced by an isolate genome
GUT_GENOME104300	MGYG000004681	Better quality MAG
GUT_GENOME278449	MGYG000004683	Better quality MAG
GUT_GENOME106243	MGYG000004685	Better quality MAG
GUT_GENOME283623	MGYG000004686	Better quality MAG
GUT_GENOME155926	MGYG000004687	Better quality MAG
GUT_GENOME206574	MGYG000004688	Better quality MAG
GUT_GENOME206795	MGYG000004690	Better quality MAG
GUT_GENOME085442	MGYG000004691	Better quality MAG
GUT_GENOME218496	MGYG000004692	MAG replaced by an isolate genome
GUT_GENOME120773	MGYG000004694	Better quality MAG
GUT_GENOME043611	MGYG000004695	Better quality MAG
GUT_GENOME175166	MGYG000004696	Better quality MAG
GUT_GENOME104392	MGYG000004697	Better quality MAG
GUT_GENOME054531	MGYG000004698	Better quality MAG
GUT_GENOME106095	MGYG000004700	Better quality MAG
GUT_GENOME037509	MGYG000004703	Better quality MAG
GUT_GENOME235948	MGYG000004706	Better quality MAG
GUT_GENOME044174	MGYG000004707	Better quality MAG
GUT_GENOME063431	MGYG000004709	Better quality MAG
GUT_GENOME034183	MGYG000004714	Better quality MAG
GUT_GENOME007188	MGYG000004716	Better quality MAG
GUT_GENOME279576	MGYG000004717	Better quality MAG
GUT_GENOME082534	MGYG000004719	Better quality MAG
GUT_GENOME102109	MGYG000004720	Better quality MAG
GUT_GENOME113426	MGYG000004721	Better quality MAG
GUT_GENOME112066	MGYG000004722	Better quality MAG
GUT_GENOME190114	MGYG000004723	Better quality MAG
GUT_GENOME044231	MGYG000004725	Better quality MAG
GUT_GENOME215875	MGYG000004726	MAG replaced by an isolate genome
GUT_GENOME111495	MGYG000004727	Better quality MAG
GUT_GENOME208213	MGYG000004733	MAG replaced by an isolate genome
GUT_GENOME083450	MGYG000004735	Better quality MAG
GUT_GENOME286625	MGYG000004738	Better quality MAG
GUT_GENOME035511	MGYG000004740	Better quality MAG
GUT_GENOME104352	MGYG000004741	Better quality MAG
GUT_GENOME032405	MGYG000004742	Better quality MAG
GUT_GENOME070996	MGYG000004743	Better quality MAG
GUT_GENOME056112	MGYG000004744	Better quality MAG
GUT_GENOME206604	MGYG000004746	Better quality MAG
GUT_GENOME071857	MGYG000004747	Better quality MAG
GUT_GENOME154813	MGYG000004751	Better quality MAG
GUT_GENOME252961	MGYG000004753	Better quality MAG
GUT_GENOME255347	MGYG000004757	Better quality MAG
GUT_GENOME071810	MGYG000004758	Better quality MAG
GUT_GENOME257519	MGYG000004760	Better quality MAG
GUT_GENOME206546	MGYG000004761	Better quality MAG
GUT_GENOME189606	MGYG000004762	Better quality MAG
GUT_GENOME275347	MGYG000004763	Better quality MAG
GUT_GENOME177793	MGYG000004764	Better quality MAG
GUT_GENOME280428	MGYG000004765	Better quality MAG
GUT_GENOME202124	MGYG000004766	Better quality MAG
GUT_GENOME233517	MGYG000004769	MAG replaced by an isolate genome
GUT_GENOME119839	MGYG000004776	Better quality MAG
GUT_GENOME255264	MGYG000004777	MAG replaced by an isolate genome
GUT_GENOME158639	MGYG000004779	Better quality MAG
GUT_GENOME006298	MGYG000004780	Better quality MAG
GUT_GENOME258967	MGYG000004783	Better quality MAG
GUT_GENOME035872	MGYG000004784	Better quality MAG
GUT_GENOME052918	MGYG000004785	Better quality MAG
GUT_GENOME044204	MGYG000004786	Better quality MAG
GUT_GENOME148088	MGYG000004789	Better quality MAG
GUT_GENOME113023	MGYG000004790	Better quality MAG
GUT_GENOME204129	MGYG000004791	Better quality MAG
GUT_GENOME170057	MGYG000004794	Better quality MAG
GUT_GENOME102353	MGYG000004797	Better quality MAG
GUT_GENOME272874	MGYG000004798	MAG replaced by an isolate genome
GUT_GENOME230891	MGYG000004799	Better quality MAG
GUT_GENOME226031	MGYG000004801	MAG replaced by an isolate genome
GUT_GENOME206730	MGYG000004802	Better quality MAG
GUT_GENOME094594	MGYG000004804	Better quality MAG
GUT_GENOME004691	MGYG000004806	MAG replaced by an isolate genome
GUT_GENOME121397	MGYG000004809	Better quality MAG
GUT_GENOME235296	MGYG000004810	Better quality MAG
GUT_GENOME113208	MGYG000004812	Better quality MAG
GUT_GENOME197527	MGYG000004815	Better quality MAG
GUT_GENOME084337	MGYG000004816	Better quality MAG
GUT_GENOME229574	MGYG000004823	Better quality MAG
GUT_GENOME086272	MGYG000004825	Better quality MAG
GUT_GENOME044142	MGYG000004826	Better quality MAG
GUT_GENOME120497	MGYG000004827	Better quality MAG
GUT_GENOME226406	MGYG000004828	Better quality MAG
GUT_GENOME260051	MGYG000004829	Better quality MAG
GUT_GENOME040960	MGYG000004830	Better quality MAG
GUT_GENOME044136	MGYG000004831	Better quality MAG
GUT_GENOME248577	MGYG000004832	Better quality MAG
GUT_GENOME103990	MGYG000004833	Better quality MAG
GUT_GENOME151605	MGYG000004837	Better quality MAG
GUT_GENOME175344	MGYG000004842	Better quality MAG
GUT_GENOME032358	MGYG000004843	Better quality MAG
GUT_GENOME120636	MGYG000004844	Better quality MAG
GUT_GENOME125744	MGYG000004846	Better quality MAG
GUT_GENOME262257	MGYG000004847	Better quality MAG
GUT_GENOME150307	MGYG000004852	Better quality MAG
GUT_GENOME237779	MGYG000004855	Better quality MAG
GUT_GENOME203607	MGYG000004862	Better quality MAG
GUT_GENOME239257	MGYG000004866	Better quality MAG
GUT_GENOME215504	MGYG000004867	Better quality MAG
GUT_GENOME202428	MGYG000004868	Better quality MAG
GUT_GENOME104704	MGYG000004872	Better quality MAG
GUT_GENOME227824	MGYG000004875	Better quality MAG
GUT_GENOME034446	MGYG000004877	Better quality MAG
GUT_GENOME156886	MGYG000004878	Better quality MAG
GUT_GENOME112247	MGYG000004882	Better quality MAG
GUT_GENOME129153	MGYG000004883	Better quality MAG
GUT_GENOME035741	MGYG000004889	Better quality MAG
GUT_GENOME229667	MGYG000004892	Better quality MAG
GUT_GENOME155166	MGYG000004893	Better quality MAG
GUT_GENOME227151	MGYG000004894	Better quality MAG
GUT_GENOME092436	MGYG000004896	Better quality MAG
GUT_GENOME081328	MGYG000004897	Better quality MAG
GUT_GENOME246421	MGYG000004899	Better quality MAG
GUT_GENOME204201	MGYG000004900	Better quality MAG
GUT_GENOME205238	MGYG000004902	Better quality MAG
GUT_GENOME153241	MGYG000004903	Better quality MAG
GUT_GENOME109882	MGYG000004905	Better quality MAG
