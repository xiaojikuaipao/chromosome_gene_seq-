#!/usr/bin/env python
from __future__ import print_function
import click


@click.command()
@click.argument('input1')
@click.argument('input2')
@click.argument('chr_pos')
# input1----chr_seq input2-----gene_seq

def seq_gene_hsa(input1,input2,chr_pos):
    gene_len = {}
    gene_length = 249213345+5000
    for i in range(1,gene_length):
        gene_len[i] = 0
    #print(chr_pos)

    chr_seq = {}
    chr_strong = {}
    #print("len create") 
    gene_seq = {}
    gene_name = {}
    gene_orient = {}
    with open(input1) as f1,open(input2) as f2:
        for seq in f1:
            chr_info = seq.strip("\n").split("\t")
            chr_start = int(chr_info[1])
            chr_end = int(chr_info[2])
            chr_str = chr_info[4]
            if chr_info[0] == chr_pos:
                chr_seq[chr_start] = chr_end
                chr_strong[chr_start] = chr_str
        for gene in f2:
            gene_info = gene.strip("\n").split("\t")
            gene_start = int(gene_info[1])
            gene_end = int(gene_info[2])
            gene_dirct = gene_info[3]
            gene_symbol = gene_info[4]
            promoter = gene_start-2000
            re_promoter = gene_start+2000
            if gene_info[0] == chr_pos:
                gene_seq[gene_start]=gene_end
                gene_name[gene_start] = gene_symbol
                gene_orient[gene_start]=gene_dirct
                for i in range(gene_start,gene_end+1):
                    gene_len[i] = 2
                if gene_dirct == "+":
                    for i in range(promoter,gene_start+1):
                        gene_len[i] = 1
                elif gene_dirct == "-":
                    for i in range(gene_start,re_promoter+1):
                        gene_len[i] = 1
             
        chr_dot_count = 0
        for chr_seq_start in chr_seq.keys():
               # print(chr_key) 
                for chr_dot in range(chr_seq_start,chr_seq[chr_seq_start]+1):
                    if  gene_len[chr_dot] == 1:
                        chr_dot_count = chr_dot_count+1
                if chr_dot_count == (chr_seq[chr_seq_start]+1)-(chr_seq_start):
                    for gene_range in range(chr_seq[chr_seq_start],chr_seq_start+2001):
                        if gene_range in gene_name.keys() and gene_orient[gene_range] == "+" : 
                            chr_seq_end =str(chr_seq[chr_seq_start]) 
                            chr_seq_strong = str(chr_strong[chr_seq_start])                          
                            chr_seq_start = str(chr_seq_start)
                            gene_seq_end = str(gene_seq[gene_range])
                            gene_seq_id = str(gene_name[gene_range])
                            gene_seq_dirct = str(gene_orient[gene_range])
                            gene_range=str(gene_range)
                            output1 = "\t".join([chr_pos,chr_seq_start,chr_seq_end,chr_seq_strong,gene_range,gene_seq_end,gene_seq_dirct,gene_seq_id]) 
                            chr_seq_start = int(chr_seq_start)   
                            gene_range = int(gene_range)
                            print(output1)          
                    for gene_seq_start in range(chr_seq[chr_seq_start]-2000,chr_seq_start+1):
                        if gene_seq_start in gene_name.keys() and gene_orient[gene_seq_start] == "-" :
                            chr_seq_end =str(chr_seq[chr_seq_start]) 
                            chr_seq_strong = str(chr_strong[chr_seq_start])
                            chr_seq_start = str(chr_seq_start)
                            gene_seq_end = str(gene_seq[gene_seq_start])
                            gene_seq_id = str(gene_name[gene_seq_start])
                            gene_seq_dirct = str(gene_orient[gene_seq_start])
                            gene_seq_start = str(gene_seq_start)                           
                            output2 = "\t".join([chr_pos,chr_seq_start,chr_seq_end,chr_seq_strong,gene_seq_start,gene_seq_end,gene_seq_dirct,gene_seq_id]) 
                            gene_seq_start = int(gene_seq_start)  
                            chr_seq_start = int(chr_seq_start)           
                            print(output2)

if __name__ == '__main__':
    seq_gene_hsa()



