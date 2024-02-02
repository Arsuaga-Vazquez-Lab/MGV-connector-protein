#!/bin/bash
# tr '\t' ',' < $1 |

if [ "$2" == "family" ]; then
    field=13
elif [ "$2" == "order" ]; then
    field=12
elif [ "$2" == "class" ]; then
    field=14
fi

#echo "VPC,Genome,$2" > "Annotations/${1}_${2}.csv"

# only grabs the VPC's with 90% identity -> makes the checking family part faster
zgrep -i $1 mgv_pc_functions.tsv.gz | awk -F'\t' '$4 >= 0.9' |  cut -f 1 > Annotations/protein_VPC.txt
zgrep -w -f Annotations/protein_VPC.txt mgv_pc_info.tsv.gz | cut -f 1,7 | tr "\t" "," > "Annotations/${1}_protein.txt"
# zcat mgv_contig_info.tsv.gz | cut -f 1,$field > "Annotations/temp.txt"

# while IFS=',' read -ra line; do
#     echo "VPC: ${line[0]}"
#     for i in "${!line[@]}"; do
#         if (( i != 0 )); then
# 			genome=$(awk -F "_" '{print $1}' <<< ${line[$i]})
# 			classification=$(zgrep -m 1 $genome "Annotations/temp.txt" | cut -f 2)
#             echo "${line[0]}, ${line[$i]}, $classification" >> "Annotations/${1}_${2}.csv"
#         fi
#     done
# done < "Annotations/${1}_protein.txt"

# rm Annotations/protein_VPC.txt

# bash bash_file/phylogeny_csv.sh "connector" "family" 

# I have commented out the code that finds the family, class , or order the VPCs correspond to
