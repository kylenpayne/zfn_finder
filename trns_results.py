'''
The class header file for the trns function. Used as output from the
trns function in the trns.py

this class was created only out of convience, as passing a 
frankenstein datastructure that consisted of
the hexamers identified, their positions in the amino acid
sequence, the corresponding postitions in the dna sequence, 
and the corresponding

'''
import numpy as np
import pandas as pd



class trns_results:

    def __init__(self, h, K, B, d):
        self.id = d.id
        self.hexamers = h
        self.KpnI_sites = K
        self.BamHI_sites = B
        self.dna_seq = d.seq
        
        '''
        find the positions of the nucleic acids that code 
        for the hexamers.
        
        input: list of hexamers
               KpnI_sites
               BamHI_sites
               dna_seq
        '''
        
        aa = self.dna_seq.translate()
        
        pos = {'hexamer' : [] ,'start' : [], 'stop' : []}
        for h in self.hexamers:
            dna_start = 3*aa.find(h)
            dna_stop = dna_start + 21
            tmp = self.dna_seq[dna_start:dna_stop]
            
            
            if(str(tmp.translate()) == h):
                print 'zfn_finder succesfully found the start and end positions of %s' % str(h) 
                pos['hexamer'] = h
                pos['start'].append(dna_start)
                pos['stop'].append(dna_stop)
            else:
                print 'zfn_finder could not find the start and end positions of %s' % str(h)
                pos['hexamer'] = h
                pos['start'].append('NaN')
                pos['stop'].append('NaN')
                
        self.sites = pd.DataFrame(pos, columns=['hexamer', 'start', 'stop'])

   

