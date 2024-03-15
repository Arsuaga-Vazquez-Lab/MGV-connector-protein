# Scripts

- run all scripts in a folder with pdb files

1. `alignment.pl`
    - Aligns the protein sequences using TM-align
    - Usage: `perl alignment.pl`
    - outputs a file `output.txt` with the alignment scores 
    - requires TM align: https://zhanggroup.org/TM-align/
    - TM-scores will be used to create a distance matrix in `tree.py`
        - TM-score from pdb1 to pdb2 will be different from pdb2 to pdb1 (so I average them when creating the tree)
        

2. `metadata.pl`
    - Extracts metadata from the pdb files
    - Usage: `perl metadata.pl`
    - outputs a file `metadata.txt` with the metadata in format: 

```
pdb_file
    family
        family_info;
    molecule
        molecule_info;
```

3. `tree.py`
    - Generates a phylogenetic tree from the alignment scores
    - Usage: `python tree.py -a output.txt -m metadata.txt -g ["single", "complete", "centroid", "all"]`
        - `-g` is optional and specifies the type of linkage for the clustering
    - outputs png files with the trees
    - requires:
        - `scipy`
        - `matplotlib`
        - `pandas`
    
        