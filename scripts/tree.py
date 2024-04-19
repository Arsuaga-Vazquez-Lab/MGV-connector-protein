import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt


def tree(alignment, graph_type="single"):
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
    tree["Merged"] = "(" + tree["Chain 1"] + "," + tree["Chain 2"] + ")"
    dist_matrix = pd.DataFrame(index = tree["Chain 1"].unique(), columns = tree["Chain 1"].unique())
    # Create distance matrix
    for i in range(tree.shape[0]):
        dist_matrix.loc[tree.iloc[i, 0], tree.iloc[i, 1]] = tree.iloc[i, 4]
    dist_matrix = dist_matrix.fillna(0)

    # Create tree
    if graph_type == "all":
        for j in ["single", "complete", "centroid"]:
            plt.figure(figsize=(20, 20))
            linkage_matrix = linkage(dist_matrix, j)           
            dendro = dendrogram(linkage_matrix, 
                       color_threshold=2, 
                       labels=tree.iloc[:,1].unique(), 
                       get_leaves=True,
                       leaf_rotation=90,
                       truncate_mode='level', 
                       p = 10) 

            # Color experimental structures
            labels = plt.gca().get_xmajorticklabels()
            for label in labels:
                if 'VPC' not in label.get_text():
                    label.set_color('red')
                else:
                    label.set_color('black')            
            plt.title(j)
            plt.ylabel("Average TM Score")
            plt.xticks(rotation=65, ha='right', fontsize=10)
            plt.show()
            leaves = dendro["ivl"]
            count = 65
            out = []
            for l in leaves:
                if l.startswith("("):
                    out.append(chr(count) + l)
                    count += 1
            else:
                out.append(l)
            # plt.savefig(j + ".png")
    else:
        plt.figure(figsize=(20, 20))
        linkage_matrix = linkage(dist_matrix, graph_type)
        dendro  = dendrogram(linkage_matrix, 
                    color_threshold=2, 
                    labels=tree.iloc[:,1].unique(), 
                    get_leaves=True,
                    leaf_rotation=90) 
        # Color experimental structures
        labels = plt.gca().get_xmajorticklabels()
        for label in labels:
            # if VPC not in label and label doesn't start with "("
            if 'VPC' not in label.get_text() and label.get_text()[0] != "(":
                label.set_color('red')
            else:
                label.set_color('black')            
        plt.title(graph_type)
        plt.ylabel("Average TM Score")
        plt.xticks(rotation=90, ha='right', fontsize=10)
        plt.show()

        # print out leaves 
        leaves = dendro["ivl"]
        count = 65
        out = []
        for l in leaves:
            if l.startswith("("):
                out.append(chr(count) + l)
                count += 1
        else:
            out.append(l)

            
    return(tree, dist_matrix, out)
