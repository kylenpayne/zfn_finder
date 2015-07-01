#!/usr/bin/python

"""
parses the fasta files 
for further downstream analysis
"""

import sys
from Bio import SeqIO

# input a fasta file, output a parsed file 
# efficient with memory, and is scalable to avoid 
def fasta_parser(input_file):
    fasta_seqs = SeqIO.parse(open(input_file), 'fasta')
    return list(fasta_seqs)

if __name__ == '__main__':
    print("This module is the fasta file parser, not called on its own :) ")