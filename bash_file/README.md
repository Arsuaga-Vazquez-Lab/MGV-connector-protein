# HOW TO USE THE SCRIPTS:

- `phylogeny.sh`
	- finds proteins that match description given by user
	- ex: `bash bash_file/phylogeny.sh "connector"`
	- outputs: 
		- `connector_protein.txt` 
			- 1st column : VPC (Viral Protein Cluster)
			- rest of the columns : MGV_XXXXXXX_X (Protein IDs)
			
- `phylogeny.py`
	- uses output of `phylogeny.sh` to find the class, family, or order that each VPC belongs to
	- ex: `python3 bash_file/phylogeny.py -i "connector_protein.txt" -p "family" -o "connector_protein_family.csv"
	- outputs:
		- dataframe of VPC and the family / class / order of the proteins found in the Cluster
		