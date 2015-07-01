#!/usr/bin/python

import sys
import re
from Bio import SeqIO
from Bio.Seq import Seq

def trns(parsed, exprs):     
    aa_target= []
    zfn_residue = []
    for p in parsed:
        cdna = p[0].seq
        for k in xrange(0,cdna.count(KpnI.site)):
            cdna_target = cdna[(cdna.find(KpnI.site)+1):cdna.find(BamHI.site)]
            aa_target.append(cdna_target.translate())
            cdna = cdna[(cdna.find(BamHI.site) + 1):]
            
    # find the zfn residue using re
    for aa in aa_target:
        zfn_residue.append(re.findall(exprs, str(aa), re.I))
        
    return zfn_residue

if __name__ == '__main__':
    print("This module is the translator and regex finder")