#!/usr/bin/python

import sys
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Restriction import *
from itertools import chain
import trns_results
'''
stolen directly from stack overflow
'''


def trns(parsed, exprs):  
    '''
    Takes parsed fasta files and matches the exprs in the 
    translated amino acid sequence 
    '''  
    res=[]
    for p in parsed:
        
        zfn_residue = []
        aa_target= []
        dna = p.seq
        
        '''
        number of sites should match
        '''
        KpnI_sites = KpnI.search(dna)
        BamHI_sites = BamHI.search(dna)
        
        for k in xrange(0,len(KpnI_sites)):
            cdna_target = dna[(KpnI_sites[k] - len(KpnI_site[k]) + 1):(BamHI_sites[k]-len(KpnI_sites[k]) + 1)]
            aa_target.append(cdna_target.translate())
            # find the zfn residue using re
        for aa in aa_target:
            zfn_residue.append(re.findall(exprs, str(aa), re.I))
        '''
        make a list of results objects
        '''
        res.append(trns_results(zfn_residue, KpnI_sites, BamHI_sites, p))

    return res
    
if __name__ == '__main__':
    print("This module is the translator and regex finder")