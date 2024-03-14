# Constructing the Connector Protein of Bacteriophages 

## Introduction

This project is based on data obtained from the paper [Metagenomic compendium of 189,680 DNA viruses from the human gut microbiome](https://www.nature.com/articles/s41564-021-00928-6). We are specifically interested in the connector protein and the goal of this project is to construct a "general structure" of the connector protein using the protein sequences found in this paper. We will also attempt to visualize the evolutionary relationships between the structure of the connector protein across families of bacteriophages using a phylogenetic tree. 

## Workflow

1. **Data Collection**: 
    - Protein sequences in the MGV database are clustered into viral protein clusters (VPCs) which have been annotated using various databases such as Pfam, KEGG, and InterPro.
    - We first extract VPC's that are annotated with the term "connector" from the MGV database.
    - We then extract the protein sequences of these VPCs from the MGV database.
    - The files to do this are located in the `scripts` directory.

2. **Modelling with AlphaFold2**
    - We use the AlphaFold2 algorithm to predict the 3D structure of the connector protein.

3. **Protein Docking with HSYMDOC**
    - We will use HSYMDOC to construct the connector protein complex (12 fold symmetry). 

4. **Analysis**
    - Using TM Align (may change) to do pair-wise structural comparisons of the predicted structures + comparisons with known structures of the connector protein (PDB database)

5. **Phylogenetic Analysis**
    - Build a tree (code is in `Podoviridae` directory for now)
    - `Podoviridae` is just a proof of concept (contains some phages annotated with connector from the PDB website)
    
- data from the MGV paper can be found in the `data` directory