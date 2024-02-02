import gzip as gz
import pandas as pd
import argparse 

args = argparse.ArgumentParser()
args.add_argument("-i", "--input_file", help="Input file")
args.add_argument("-p", "--phylo", help="Phylogeny level")
args.add_argument("-o", "--output_file", help="Output file")
args = args.parse_args()


def check_phylogeny(input_file, phylo, output_file):

    if (phylo == "family"):
        field=12
    if (phylo == "order"):
        field=13
    if (phylo == "class"):
        field=14


    with gz.open("mgv_contig_info.tsv.gz", "r") as f:
    # cut columns 1 and 13 and place in dataframe
        lines = [line.strip().decode() for line in f.readlines()]
        lines = [line.split("\t") for line in lines]
        lines = [[line[0], line[field]] for line in lines]
        df_phylo = pd.DataFrame(lines[1:], columns=["contig_id", "ictv"])
        # df_phylo.to_csv("Annotations/mgv_pc_info.csv", index=False)
    lines = None

    df_temp = pd.read_csv(input_file, header = None)# names=["VPC", "Protein"] 
    df_pc = df_temp.melt(id_vars=df_temp.columns[0], value_vars=df_temp.columns[1:])
    df_pc = df_pc.iloc[:,[0,2]]
    df_pc.columns = ["VPC", "protein_id"]
    df_pc["contig_id"] = "MGV-GENOME-" + df_pc["protein_id"].str.extract(r"(\d+)")
    # merge df_pc and df_phylo
    df_pc = df_pc.merge(df_phylo, on="contig_id", how="right")
    # count non NaN values in VPC column
    df_pc["VPC"].notna().sum() # same as before
    # drop rows with NaN values in VPC column
    df_pc = df_pc.dropna(subset=["VPC"])
    df_pc = df_pc.dropna(subset=["protein_id"])
    df_pc.groupby(["VPC", f"ictv_{phylo}"]).size().to_csv(output_file)
    # checks for duplicates
    if len(set(df_pc["contig_id"].unique())) == len(df_pc["contig_id"].unique()):
        print("No duplicates")
    df_phylo = pd.read_csv(output_file)
    df_phylo = df_phylo.groupby([f"ictv_{phylo}"]).sum("0")
    df_phylo["proportions"] = df_phylo["0"]/df_phylo["0"].sum()
    
    return df_phylo


if __name__ == "__main__":
    check_phylogeny(args.input_file, args.phylo, args.output_file)