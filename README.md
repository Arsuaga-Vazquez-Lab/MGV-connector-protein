# Constructing the Connector Protein of Bacteriophages 

## Introduction

This project is based on data obtained from the paper [Metagenomic compendium of 189,680 DNA viruses from the human gut microbiome](https://www.nature.com/articles/s41564-021-00928-6) which contains a very interesting set of data connecting bacteriophages found in the microbiome to their bacterial hosts. As the TMBL lab works largely on DNA folding and packaging in bacteriophages, we will be focusing on the connector protein and the goal of this project is to construct a "general structure" of the protein using the sequences found in this paper. We will also attempt to visualize the evolutionary relationships between the structure of the connector protein across families of bacteriophages using a phylogenetic tree. 

As a side project, we will also be looking at small capsids (T < 4) identified in [The Missing Tailed Phages: Prediction of Small Capsid Candidates](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7762592/) and constructing a structure of the capsid to evaluate its interactions with the connector protein. 

## Workflow

1. **Data Collection**: 
    - Protein sequences in the MGV database are clustered into viral protein clusters (VPCs) which have been annotated using various databases such as Pfam, KEGG, and InterPro.
    - Extract VPC's that are annotated with the term "connector" from the MGV database
    - Extract protein sequences that belong to these VPCs from the MGV database
    - Files for this are located in the [scripts](https://github.com/Arsuaga-Vazquez-Lab/MGV-connector-protein/tree/0cc42c4bffefd5a69b6dfe705fca0d5478359317/scripts) directory

2. **Modelling with AlphaFold2**
    - We use the AlphaFold2 algorithm to predict the 3D structure of the connector protein.
3. **Analysis**
    - Using TM Align (may change) to do pair-wise structural comparisons of the predicted structures + comparisons with known structures of the connector protein (PDB database)

5. **Structural Analysis**
    - Build a tree (code is in [Podoviridae](https://github.com/Arsuaga-Vazquez-Lab/MGV-connector-protein/tree/main/Podoviridae) directory for now)
    - `Podoviridae` is just a proof of concept (contains some phages annotated with connector from the PDB website)
    - Structural Phylogenetic tree can be found in [tree](https://github.com/Arsuaga-Vazquez-Lab/MGV-connector-protein/tree/main/tree)
	
6. **Compare Structural Phylogenetic Tree with Hosts**
	- hosts can be found in [heatmap](https://github.com/Arsuaga-Vazquez-Lab/MGV-connector-protein/tree/main/heatmap)
    	


## Future Directions

- Instead of using TM-align (which looks at global similarities), we should compare structures based on local similarities. One software that does this is [DALI](http://ekhidna2.biocenter.helsinki.fi/dali/)
    
- We only looked compared the structure of the monomer in this project. Using the complete structure of the complex would be more biologically accurate. 

- And last but not least, it's always better to have more data. We only used structures in the database that were annotated as "connector". "Portal" is synonymous with "connector" in bacteriophage physiology. Those structures can also be used here. 


** Note**
    
- data from the MGV paper can be found in the [data](https://github.com/Arsuaga-Vazquez-Lab/MGV-connector-protein/tree/0cc42c4bffefd5a69b6dfe705fca0d5478359317/data) directory