#!/usr/bin/python

"""
main part of the hexamer finding program

uses fasta_parser.py, trns.py

"""

from __future__ import print_function, division
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet import generic_dna
#from fasta_parser import fasta_parser as fp
from fasta_parser import fasta_parser
from trns import trns
import sys



if __name__ == '__main__':
    print("""
            Zfn Finder: finds amino acid
            sequences that correspond to
            the general framework supplied as 
            either the running default in the program
            or specified as one of the arguments 
            Directory --- 
            """)
    

#import 

import glob, os


amb = IUPACAmbiguousDNA()



arg1 = "\\\dasnas01\\rd\\home\\nb93358\\projects\\gover_zfn\\"
os.chdir(arg1)

# regular expressions
exprs= "(?:C[A-Z][A-Z]C[A-Z]{5})([A-Z]{7})(?:H[A-Z]{3}[HC])"

# grab all of the fasta files in the directory
parsed = []

# parse 'dem
for file in glob.glob("*.fasta"):
    parsed.append(fasta_parser(file))

         
         