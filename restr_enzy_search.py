#!/usr/bin/python

"""
Part of the z

"""
from Bio.Restriction import *
from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet import generic_dna
#from fasta_parser import fasta_parser as fp
from Bio import SeqIO
from fasta_parser import fasta_parser

#import 
import re
import sys
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
hexamer_seq = []

# parse 'dem
for file in glob.glob("*.fasta"):
    parsed.append(fasta_parser(file))

         
         


#aa_target 
 # aa_target = cdna_target.translate()

# zfn_residue = re.findall(exprs, str(aa_target), re.I)
    
    
    
