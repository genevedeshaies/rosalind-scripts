from Bio import SeqIO

def computeGCContent(file, format)->dict:
    """Parses a sequence file and computes GC content for every sequence."""
    gcContCompilation = {}
    with open(file, "r") as fh:
        for seq_record in SeqIO.parse(file, format):
            gcCont = (seq_record.seq.count("G") + seq_record.seq.count("C")) / len(seq_record.seq) *100
            gcContCompilation[seq_record.id] = gcCont
    return gcContCompilation

def findHighestGC(gcContCompilation):
    """Looks at the GC contents in a dict and returns the sequence with the highest one"""
    highestGC = 0
    for seqid, gc in gcContCompilation.items():
        if gc > highestGC:
            highestGC = gc

    for seqid, gc in gcContCompilation.items():    
        if gc == highestGC:
            return (seqid, gc)

computedGC = computeGCContent("gc.txt", "fasta")

print(findHighestGC(computedGC))