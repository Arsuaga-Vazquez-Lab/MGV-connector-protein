# HOW TO USE THE SCRIPTS:

- `phylogeny.sh`
	- finds proteins that match description given by user
	- ex: `bash scripts/phylogeny.sh "connector"`
	- outputs: 
		- `[description]_protein.txt` 
			- 1st column : VPC (Viral Protein Cluster)
			- rest of the columns : MGV_XXXXXXX_X (Protein IDs)
			- ex: `VPC-XX, MGV_XXXXXXX_X`
	- will be input for `extract.pl`
			
- `extract.pl`
	- ex: `perl scripts/extract.pl [file with list of proteins] [order/family/genus]`
	- input: file with VPC's and corresponding protein IDs
	- output:
		- `[description]_protein_out.faa`
			- fasta file of proteins and their sequence: 
			- ">MGV_XXXXXXX_X"
			- "sequence"
		- `[description]_protein_out.csv`
			- csv file with VPC, protein id, and phylogeny
	- can take a minute to run
			
