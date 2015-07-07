#!/usr/bin/python

"""
main part of the hexamer finding program

"""
from __future__ import print_function, division
import sys



if __name__ == '__main__':
    print("This module is the fasta file parser, not called on its own :) ")
    
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet import generic_dna
#from fasta_parser import fasta_parser as fp

#import 

import glob, os


amb = IUPACAmbiguousDNA()


# this is a test version of the concept, eventually this will 
# imported into a main file with the 
# program taking the required fasta files and performing 
# the parsing on sys args passed to the program


arg1 = "\\\dasnas01\\rd\\home\\nb93358\\projects\\gover_zfn\\"
os.chdir(arg1)

# regular expressions
exprs= "(?:C[A-Z][A-Z]C[A-Z]{5})([A-Z]{7})(?:H[A-Z]{3}[HC])"

# grab all of the fasta files in the directory
parsed = []

# parse 'dem
for file in glob.glob("*.fasta"):
    parsed.append(fasta_parser(file))

         
         