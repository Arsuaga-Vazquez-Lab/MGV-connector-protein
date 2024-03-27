import pandas as pd
import regex as re
import os

filepath = "../Annotations/connector/"


if not os.path.exists(f"{filepath}/vpc/"):
    os.makedirs(f"{filepath}/vpc/")
vpc_df = pd.read_csv(f"{filepath}/connector_protein.txt", header=None)
vpc_df = vpc_df.set_index(vpc_df.columns[0])
for vpc in vpc_df.index:
    write_file = f"{filepath}/vpc/{vpc}.faa"
    vpc_temp = {key : "" for key in vpc_df.loc[vpc].unique()}
    with open(write_file, "w") as w:   
        with open(f"{filepath}/connector_protein.faa") as f2:
            for line in f2:
                if line.startswith(">"):
                    if re.search(r'>\s*(.*?)\s', line).group(1) in vpc_temp.keys():
                        w.write(line)
                        w.write(next(f2)) 