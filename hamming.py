sample = ["GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"]

def parsefile(file):
    with open(file, "r") as fh:
        opened = fh.readlines()
        seq1, seq2 = opened[0], opened[1]
    return seq1, seq2

seq1, seq2 = parsefile("rosalind_hamm.txt")

def computeHammingDistance(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

print(computeHammingDistance(seq1, seq2))