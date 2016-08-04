# zfn_finder is a bio-informatics toolkit that makes it easy to find Zinc Finger Nucleases from a set of FASTA files.
## This program uses up to date methodologies for scanning FASTA file and searches for the grammatical structure of Zinc Finger Nucleases from 
within a set of DNA sequence files.

### This program accomplishes this through a transcription of the DNA sequence information into RNA.

$$
DNA -> RNA
$$

then, the RNA is searched for the higher-level Zinc-Finger Nuclease structure. Once found, the DNA is indexed based on the position of the 
hexamer locations, and the corresponding DNA section is cleaved from the DNA and recorded in a separate file.

### This work was done as part of a Hack-a-thon at Dow AgroScience.

