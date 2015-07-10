#!/usr/bin/python
'''
main part of the hexamer finding program

uses fasta_parser.py, trns.py

'''

from __future__ import print_function, division

#from fasta_parser import fasta_parser as fp
from fasta_parser import fasta_parser
from trns import trns
from helpers import arg_parse, out_pretty
import sys, glob, os
import pandas as pd
import numpy as np

'''
Parses the input arguments so that the 
zfn_finder can store them for 
downstream operations
'''

    

if __name__ == '__main__':
    print('''
            Zfn Finder: finds amino acid
            sequences that correspond to
            the general framework supplied as 
            either the running default in the program
            or specified as one of the arguments                
            ''')
            
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
        for file in glob.glob("*.fas"):
            parsed.append(fasta_parser(file))
            
        results = trns(parsed, exprs)
        out_pretty(results, args["out_file"])
        
    else:
        print("Fasta file are the only type currently supported")
        sys.exit()
    
    
         