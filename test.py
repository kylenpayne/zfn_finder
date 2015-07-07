''' tests the functionality of using matplotlib to 
 plot the amino acid sequences as annotated lettters
'''

from __future__ import print_function, division
from Bio import Restriction
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet import generic_dna
#from fasta_parser import fasta_parser as fp
from fasta_parser import fasta_parser as fp
from trns import trns
import sys, glob, os
import pandas as pd
import numpy as np
from matplotlib import 
