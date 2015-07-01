#!/usr/bin/python

import sys
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Restriction
def trns(parsed, exprs):   
    '''
    Takes parsed fasta files and matches the exprs in the 
    translated amino acid sequence 
    '''  
    aa_target= []
    zfn_residue = []
    ids = []
    for p in parsed:
        cdna = p[0].seq
        '''
        number of sites should match
        '''
        KpnI_sites = KpnI.search(cdna)
        BamHI_sites = BamHI.search(cdna)
        
        for k in xrange(0,len()):
            cdna_target = cdna[(KpnI_sites[k]):BamHI_sites[k]]
            aa_target.append(cdna_target.translate())
        ids.append(p[0].id)
            
    # find the zfn residue using re
    for aa in aa_target:
        zfn_residue.append(re.findall(exprs, str(aa), re.I))
        
    
if __name__ == '__main__':
    print("This module is the translator and regex finder")