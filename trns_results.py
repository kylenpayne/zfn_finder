#!/usr/bin/python
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

    def __init__(self, h, K, B, d, target):
        self.id = d.id
        self.hexamers = h
        self.KpnI_sites = K
        self.BamHI_sites = B
        self.dna_seq = d.seq
        self.cdna_target = target
        
        '''
        find the positions of the nucleic acids that code 
        for the hexamers.
        
        input: list of hexamers
               KpnI_sites
               BamHI_sites
               dna_seq
        '''
        print('''
        Id is :{0}
        
        '''.format(self.id))
            
        pos = {'hexamer' : [] ,'start' : [], 'stop' : [], 'chunk': []}
        
        aa = []
        
        '''
        We have to enumerate the hierarchical 
        hexamer lists as sometimes there are
        sequences that are parsed from the fasta files
        that have more than one KpnI and BamHI site. 
        In this case (the usual case), we have 
        a list of lists
        
        hexamer = [ # first KpnI--BamHI 
        [hexamer1, hexamer2, ...],
        # second KpnI--BamHI
        [hexamer1, hexamer2, ...]
        ]
        
        Thus we can't flatten these as the corresponding dna chunks 
        
        '''        
        
        for idx, hexamer in enumerate(self.hexamers):  
            aa = self.cdna_target[idx].translate() 
            for k in xrange(0, len(hexamer)):
                dna_start = 3*aa.find(hexamer[k])
                dna_stop = dna_start + 21
                tmp = self.cdna_target[idx]
                tmp = tmp[dna_start:dna_stop]
                    
                if(str(tmp.translate()) == hexamer[k]):
                    print 'zfn_finder succesfully found the start and end positions of {0}'.format(str(hexamer[k]))
                    pos['hexamer'].append(hexamer[k])
                    pos['start'].append(dna_start + self.KpnI_sites[idx])
                    pos['stop'].append(dna_stop + self.KpnI_sites[idx])
                    pos['chunk'].append(idx + 1)
                else:
                    print 'zfn_finder could not find the start and end positions of {0}'.format(str(hexamer[k]))
                    pos['hexamer'].append(hexamer[k])
                    pos['start'].append('NaN')
                    pos['stop'].append('NaN')
                    pos['chunk'].append(idx + 1)
                    
        self.sites = pd.DataFrame(pos, columns=['hexamer', 'start', 'stop', 'chunk'])

   

