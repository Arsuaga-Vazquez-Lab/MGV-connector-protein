import gzip as gz
import regex as re
import pandas as pd
import argparse 
import warnings

warnings.filterwarnings("ignore")
args = argparse.ArgumentParser()
args.add_argument("-i", "--input_file", help="Input file")
args.add_argument("-o", "--output_file", help="Output file")
parser = args.parse_args()


def extract_sequences(input_file, output_file):
    df_temp = pd.read_csv(input_file, header = None)# names=["VPC", "Protein"] 
    df_pc = df_temp.melt(id_vars=df_temp.columns[0], value_vars=df_temp.columns[1:])
    df_pc = df_pc.iloc[:,[0,2]]
    df_pc.columns = ["VPC", "protein_id"]
    df_pc
    length = 23674396
    with open(output_file, "a") as w:
        # with gz.open("data/mgv_proteins.faa.gz", "r") as f:
        with gz.open("temp/look_up_protein_sample.fasta.gz", "r") as f:
            i = 0
            for line in f:
                i += 1
                line = line.strip().decode()
                if line.startswith(">"):
                    mgv = re.findall(r"MGV-GENOME-\d+_\d+", line)[0]
                    if mgv in df_pc["protein_id"].values:
                        vpc = df_pc[df_pc["protein_id"] == mgv]["VPC"].values[0]
                        print(f"{vpc}, {line}")
                        w.write(f"{vpc}, {line}\n")
                        w.write(next(f, None).decode("utf-8")+ "\n")
                if i % 1000 == 0:
                    print(f"{i}/{length}")
    return "Done"

if __name__ == "__main__":
    extract_sequences(parser.input_file, parser.output_file)