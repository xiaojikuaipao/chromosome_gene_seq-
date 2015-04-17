#!/usr/bin/env python
from __future__ import print_function
import click


@click.command()
@click.argument('input1')
def read_gff(input1):
    with open(input1) as f1:
        for gff_line in f1:
            gff_hash = gff_line.strip("\n").split("\t")
            gff_orient = gff_hash[3]
            if gff_orient == "+":
                gff_line = gff_line.strip("\n")
                print(gff_line)
            elif gff_orient == "-":
                gff_line = "\t".join([gff_hash[0],gff_hash[2],gff_hash[1],gff_hash[3],gff_hash[4]])
                print(gff_line)

if __name__ == '__main__':
    read_gff()
