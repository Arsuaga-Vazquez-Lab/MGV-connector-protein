import pandas as pd
import argparse
from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Create a tree from a pairwise alignment')
parser.add_argument('-a', type=str, help='The pairwise alignment file')
parser.add_argument('-m', type=str, help='The metadata file')
parser.add_argument('-g', type=str, help='The type of graph to create (single, complete, centroid, all)')
args = parser.parse_args()


def tree(alignment, metadata, graph_type="single"):

    # Read metadata, add description and family to the tree
    with open(metadata, 'r') as m:
        meta_dict = {}
        lines_m = m.readlines()
        pdb = ""
        family = False
        molecule = False
        for line in lines_m:
            if ".pdb" in line:
                family = False
                molecule = False
                pdb = line.strip()
                meta_dict[pdb] = {"Family": [], "Molecule": []}
            if "family" in line:
                family = True
                molecule = False
                continue
            if "molecule" in line:
                molecule = True
                family = False
                continue
            if family:
                meta_dict[pdb]["Family"].append(line.strip().strip(";"))
            if molecule:
                meta_dict[pdb]["Molecule"].append(line.strip().strip(";"))
    metatdata_df = pd.DataFrame(meta_dict).T

    tree_dict = {"Chain 1" : [],
                 "Chain 2": [],
                 "Chain 1 TM Score" : [],
                 "Chain 2 TM Score" : [],
                 "Average TM Score" : []}
    # for each pairwise alignment, average the TM scores
    with open(alignment, 'r') as f:
        alignments = f.readlines()
        for line in alignments:
            line = line.strip()
            if "Name" in line:
                if "Chain_1" in line: 
                    tree_dict["Chain 1"].append(line.split(":")[1].strip())
                else: tree_dict["Chain 2"].append(line.split(":")[1].strip())
            if "TM-score=" in line:
                if "Chain_1" in line: tree_dict["Chain 1 TM Score"].append(float(line.split()[1]))
                else: 
                    tree_dict["Chain 2 TM Score"].append(float(line.split()[1]))
                    tree_dict["Average TM Score"].append((tree_dict["Chain 1 TM Score"][-1] + tree_dict["Chain 2 TM Score"][-1]) / 2)
    tree = pd.DataFrame(tree_dict)
    # tree["Merged"] = "(" + tree["Chain 1"] + "," + tree["Chain 2"] + ")"

    # Replace pdb file with family / protein description
    for i in range(tree.shape[0]):
        tree.iloc[i, 0] = metatdata_df.loc[tree.iloc[i, 0], "Family"][0]
        tree.iloc[i, 1] = metatdata_df.loc[tree.iloc[i, 1], "Family"][0]

    dist_matrix = pd.DataFrame(index = tree["Chain 1"].unique(), columns = tree["Chain 1"].unique())

    # Create distance matrix
    for i in range(tree.shape[0]):
        dist_matrix.loc[tree.iloc[i, 0], tree.iloc[i, 1]] = tree.iloc[i, 4]
    dist_matrix = dist_matrix.fillna(0)

    # Create tree
    if graph_type == "all":
        for j in ["single", "complete", "centroid"]:
            linkage_matrix = linkage(dist_matrix, j)
            dendrogram(linkage_matrix, color_threshold=1, labels=tree.iloc[:,1].unique(),show_leaf_counts=True)
            plt.title=("test")
            plt.show()
    else:
        linkage_matrix = linkage(dist_matrix, graph_type)
        dendrogram(linkage_matrix, color_threshold=1, labels=tree.iloc[:,1].unique(),show_leaf_counts=True)
        # plt.title=("test")
        plt.xticks(rotation=45, ha='right')
        plt.show()

    return(tree, dist_matrix, metatdata_df)

if __name__ == '__main__':
    tree(args.a, args.m, args.g)