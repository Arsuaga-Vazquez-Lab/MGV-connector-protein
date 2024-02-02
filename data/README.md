- The data can be found at: https://portal.nersc.gov/MGV/

- The dataset README is shown below:

## Supporting data for: "Metagenomic compendium of 189,680 DNA viruses from the human gut microbiome"
Bacteriophages have important roles in the ecology and biology of the human gut microbiome but are underrepresented in reference databases. We address this problem by assembling a comprehensive catalogue named the Metagenomic Gut Virus Dataset (MGV) that comprises 189,680 draft genomes of uncultivated viruses with >50% completeness assembled from 11,810 publicly available human gut metagenomic samples. The vast majority of genomes represent dsDNA phages from the Caudovirales order that infect members of the Bacteroidia and Clostridia classes. We analyzed our collection of viral genomes and identified 54,118 candidate species and find that our dataset significantly improve viral detection in metagenomes and that our sequences match nearly 40% of CRISPR spacers found in human gut Bacteria and Archaea. Phylogenetic analyses reveal several diverse and previously unknown clades that are more abundant than crAss-like phages, infect prevalent gut bacteria, and display global phylogeographic population structure. Using a combination of approaches, we identified host-virus connections that cover the majority of prokaryotic and viral diversity in the microbiome. We also produced a catalogue of 459,375 viral protein clusters to enable the functional potential of the gut virome to be analyzed, revealing thousands of diversity-generating retroelements that might be involved in molecular phage-host interactions. We hope that this set of genomes will enable progress in understanding functions of the human gut virome.

#### Data usage policy
* All data presented here is freely available to use without any restrictions.
* If you use these data in your work, please cite: TBD

#### mgv_contigs.fna
* 189,680 viral genomes from the current study
* all with >50% estimated completeness
* non-identical sequences

#### mgv_votu_representatives.fna
* Representative genomes for 54,118 vOTUs
* Reps were prioritized based on (i) circularity, (ii) lack of flanking host regions, and (iii) length

#### mgv_contig_info.tsv
* Metadata for the 189,680 viral genomes. Fields include:
* votu_id: indicate the species-level viral OTU the genome belongs to
* checkv_quality: medium quality (50-90% complete), high quality (>90% complete), complete (closed genome)
* prophage: wheter or not the contig was flanked by DNA from the host (these regions were removed)
* temperate_score: BACPHLIP output indicating the probability the virus lives a temperate lifestyle
* virulent_score: BACPHLIP output indicating the probability the virus lives a virulent lifestyle
* completeness: CheckV estimated completeness
* gc: GC content
* stop_codon_readthrough: indicates whether the virus is predicted to read through a particular stop codon
* baltimore: baltimore classification
* ictv_order, ictv_family, ictv_genus: annotations based on the ICTV taxonomy

#### mgv_host_assignments.tsv
* Viruses were linked to host genomes from the UHGG database using a combination of CRISPR spacer matches and near-identical 1Kb BLAST hits between genomes
* Host genomes were aggregated for each virus and we identified the host rank where >70% of genomes originated from the same taxon

#### mgv_proteins.faa
* 11,837,198 proteins identified from the 189,680 viral genomes using Progigal -p meta

#### mgv_pc_info.tsv
* 11,837,198 proteins were grouped into 459,375 clustering using MMseqs2

#### mgv_pc_functions.tsv
* 11,837,198 proteins were annotated using a combination of databases, including Pfam, KEGG, and TIGRFAM
* The table include the consensus functional annotation for each of the protein clusters

#### mgv_dgrs.tsv
* Diversity Generating Retroelements (DGRs) were identified on viral genomes based on the presence of a reverse transcriptase (RT) gene and a template-region variable-region (TR-VR) repeat
* The TR-VRs were identified using DGRscan and the RTs were identified using Pfam + HMMER

#### uhgg_spacers.fna
* 1,846,441 CRISPR spacers identified from UHGG genomes
* Information is contained in the headers
* Take for example, spacer GUT_GENOME146689|accn|CXHB01000030|1|1
* This is the first spacer on the first CRISPR array found on contig accn|CXHB01000030 from GUT_GENOME146689

#### Code availability
All code can be found at https://github.com/snayfach/MGV
