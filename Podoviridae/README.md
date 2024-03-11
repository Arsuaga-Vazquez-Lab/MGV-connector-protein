# Scripts

- run all scripts in a folder with pdb files

1. `alignment.pl`
    - Aligns the protein sequences using TM-align
    - Usage: `perl alignment.pl`
    - outputs a file `output.txt` with the alignment scores
    - requires TM align: https://zhanggroup.org/TM-align/

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
    
        