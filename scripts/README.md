# HOW TO USE THE SCRIPTS:

- `phylogeny.sh`
	- finds proteins that match description given by user
	- ex: `bash bash_file/phylogeny.sh "connector"`
	- outputs: 
		- `connector_protein.txt` 
			- 1st column : VPC (Viral Protein Cluster)
			- rest of the columns : MGV_XXXXXXX_X (Protein IDs)
			
- `phylogeny.py`
	- requires pandas
	- uses output of `phylogeny.sh` to find the class, family, or order that each VPC belongs to
	- ex: `python3 bash_file/phylogeny.py -i "connector_protein.txt" -p "family" -o "connector_protein_family.csv"
	- outputs:
		- dataframe of VPC and the family / class / order of the proteins found in the Cluster

- `extract_proteins_by_VPC.py`
	- requires pandas, regex
	- extracts proteins from a file with VPC and protein_id (output of `phylogeny.sh`) and labels with VPC
	- ex: `python3 bash_file/extract_proteins_by_VPC.py -i "connector_protein.txt" -o "connector_proteins.fasta"`
	- outputs:
		- fasta file of proteins with VPC label
	- NOTE: may take a while to run as `mgv_proteins.faa.gz` is v large
	- Use `extract.pl` instead!!!

- `extract.pl`
	- ex: `perl bash_file/extract.pl [file with list of proteins] [order/family/genus]`
	- output:
		- fasta file of proteins and their sequence: ">MGV_XXXXXXX_X"
		- csv file with VPC, protein id, and phylogeny

- `organize_proteins.pl`
	- manage output of `extract.pl`
	- ex: `perl bash_file/organize_proteins.pl [file with list of proteins]`
	- output: 
		- file matching VPC to protein id
		- file of protein ids
		- file of protein ids and associated sequence