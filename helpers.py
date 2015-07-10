#!/usr/bin/python


import getopt
import pandas as pd
import sys
import csv
import yaml

'''
Contains functions that are used in the main zfn_finder.py file
'''

def arg_parse(argv):
    in_dir =''
    out_file = ''
    file_type = ''
    exprs = ''
    try:
        opts, args = getopt.getopt(argv, "hd:f:o:e:", ["f_dir=", "type=", "ofile=", "exprs="])
    except getopt.GetoptError:
        print('An error occurred with the input')
        sys.exit(2)
    for opt, arg in opts, args:
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
    
def out_pretty(results, name):

    tmp_csv = open(str(name) + '.csv', 'w')
    tmp_csv.close()
    '''
    take the output from the residues and outputs
    a yaml file with the fasta id, KpnI sites, BamHI sites
    then creates a csv file with the hexamers and the 
    corresponding sites in the genome
    '''
    with open(str(name)+'.yml', 'w') as yaml_file:
        for res in results:
            tmp = {'Fasta ID' : res.id, 'KpnI Sites' : res.KpnI_sites,
            'BamHI Sites' : res.BamHI_sites} 
            yaml_file.write( yaml.dump(tmp, default_flow_style=False))
  
    with open(str(name) + '.csv', 'a') as f: 
        for res in results:            
            df = res.sites
            df.to_csv(f, sep='\t')