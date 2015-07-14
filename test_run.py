# test run

from Bio.Restriction import *
from Bio import Seq
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

bases = np.array(['A', 'T', 'C', 'G'])

bases = KpnI.site + 'ATCGGCTACCCTATCGTC' + BamHI.site

l = len(bases)

cdna = Seq(bases)

KpnI_sites = KpnI.search(cdna)
BamHI_sites = BamHI.search(cdna)
        
for k in xrange(0,len(KpnI_sites)):
    cdna_target = cdna[(KpnI_sites[k] - len(KpnI.site) + 1):(BamHI_sites[k]-len(KpnI.site) + 1)]
    aa_target.append(cdna_target.translate())
    # find the zfn residue using re
for aa in aa_target:
    zfn_residue.append(re.findall(exprs, str(aa), re.I))
        