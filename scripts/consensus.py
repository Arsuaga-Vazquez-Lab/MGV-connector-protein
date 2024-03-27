from Bio import AlignIO
from Bio.Align import AlignInfo
import os
import regex as re

filepath = "../Annotations/connector"

if not os.path.exists(f"{filepath}/consensus"):
    os.makedirs(f"{filepath}/consensus")
for file in os.listdir(f"{filepath}/msa"):
    alignment = AlignIO.read(f"{filepath}/msa/{file}", "fasta")
    summary = AlignInfo.SummaryInfo(alignment)
    consensus_seq = summary.dumb_consensus(threshold=0)
    file = file.split(".")[0]
    consensus_seq = str(consensus_seq)
    if "*" in consensus_seq: # only get sequence up until first * (* = stop codon)
        consensus_seq = re.findall(r"^(.*?)\*", consensus_seq)[0]
    with open(f"{filepath}/msa/{file}_consensus.fasta", "w") as w:
        w.write(consensus_seq)