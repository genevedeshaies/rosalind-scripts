import sys

rna_codon_table = {
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
        'UAU':'Y', 'UAC':'Y', 'UAA':'_', 'UAG':'_', 'UGU':'C', 'UGC':'C', 'UGA':'', 'UGG':'W',
        'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
        'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
        }


def rnaToProt(file)->str:
    """Takes an RNA sequence from a file and returns the translated protein sequence"""
    global rna_codon_table
    prot = ""
    with open(file, "r") as fh:
        fh = fh.read()
        codons = [fh[i:i+3] for i in range(0, len(fh), 3)]
        for codon in codons:
            prot += rna_codon_table[codon]
    return prot

if __name__ == "__main__":
    print(rnaToProt(sys.argv[1]))
    exit()