# Building a Tree Based on the Structural Similarity of the Connector Protein

- `consensus_pdb.tar.gz` contains gzipped files of an AlphaFold predicted structure for each of the Viral Protein Clusters (VPC) annotated as "connector" + some additional connector proteins from well studied phages (ie T4, T7, P22, etc.). We also included some Herpesviruses for fun.  
	- looking back connector proteins should be synonymous to portal proteins so future directions could include running this pipeline on the portal proteins and adding them to the tree
	- inside `consensus_pdb.tar.gz` is a script `alignment.pl` (the same as the one in the [Podoviridae](https://github.com/Arsuaga-Vazquez-Lab/MGV-connector-protein/tree/main/Podoviridae) folder
		- run with `perl alignment.pl > scores.txt`, this will output a script 
			- don't name the output file `output.txt` as this is used to produce the full version of the TM-align output
	
- `demo.ipynb`
	- Contains some code that draws a dendrogram based on the structural similarities between the connector proteins and colors the clusters by their family annotations. Because there are so many proteins, we have added an alternative graphs with merged leaves to improve viewability. 
	- requires: `scipy`, `pandas`, `matplotlib`