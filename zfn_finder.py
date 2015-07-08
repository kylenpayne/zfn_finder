#!/usr/bin/python
'''
main part of the hexamer finding program

uses fasta_parser.py, trns.py

'''

from __future__ import print_function, division
from Bio import Restriction
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet import generic_dna
#from fasta_parser import fasta_parser as fp
from fasta_parser import fasta_parser
from trns import trns
import sys, glob, os
import pandas as pd
import numpy as np

'''
Parses the input arguments so that the 
zfn_finder can store them for 
downstream operations
'''

def arg_parse(argv):
    in_dir =''
    out_file = ''
    file_type = ''
    exprs = ''
    try:
        opts, args = getopt.getopt(argv, "hd:foe", ["f_dir=", "type=", "ofile=", "exprs="])
    except getopt.GetoptError:
        print('An error occurred with the input')
        sys.exit(2)
    for opt, arg in opts:
        if opt =='-h':
            print('''
            Thanks for using the -h help option:
            To use zfn_finder, use must specify
            the (-d) directory where the files are located
            (-f) file type (current only fasta files are supported)
            (-o) the output file which contains the corresponding
            amino acid sequences and lastly
            (-e) the regular expression that will be used
            to match the amino acid sequences that are desired.
            
            By default -e is not neccessary, and matches to the 
            default provided in the program, 
             (?:C[A-Z][A-Z]C[A-Z]{5})([A-Z]{7})(?:H[A-Z]{3}[HC])
            
            Ex:
                zfn_finder.py -d my/dir/where/fasta/located -f 
                -o /my/output/file/location/ -e "(?:C[A-Z][A-Z]C[A-Z]{5})([A-Z]{7})(?:H[A-Z]{3}[HC])"
            ''')
            sys.exit()
        elif opt in ('-d', '--f_dir'):
            in_dir = arg
        elif opt in ('-f', '--type'):
            file_type = arg
            print('Input files are to be parsed as fasta files')
        elif opt in ('-o', '--ofile'):
            out_file = arg
        elif opt in ('-e', '--exprs'):
            exprs = arg
        
    print('Input Directory is: ', str(in_dir))
    print('Output file is: ', str(out_file))
    print('The regex used is: ', str(exprs)) 
      
    ret = {"in_dir": in_dir, "file_type" : file_type,
    "out_file" : out_file, "exprs" : exprs} 
     
    return ret
    
def out_pretty(results, out_file):
    '''
    take the output from the residues and prints out a file that 
    looks good
    '''
    f = open(str(out_file), 'w')
    f.write()
    f.close() 

if __name__ == '__main__':
    print("""
            Zfn Finder: finds amino acid
            sequences that correspond to
            the general framework supplied as 
            either the running default in the program
            or specified as one of the arguments                
            """)
            
    import getopt
    # default regex   

    args = arg_parse(argv[1:])
    os.chdir(args["in_dir"])
    
    if(args['exprs'] == ''):
        exprs = "(?:C[A-Z][A-Z]C[A-Z]{5})([A-Z]{7})(?:H[A-Z]{3}[HC])"
    else:
        exprs = str(args['exprs'])  
         
    parsed = []

    if(args["file_type"] == 'fasta'):
        for file in glob.glob("*.fasta"):
            parsed.append(fasta_parser(file))
        results = trns(parsed, exprs)
        out_pretty(results, args["out_file"])
        
    else:
        print("Fasta file are the only type currently supported")
        sys.exit()
    
    
         