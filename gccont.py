from Bio import SeqIO

parsedSeq = {}
gcContCompilation = {}

highestGC = 0

highestGCSeq = {}

for seq_record in SeqIO.parse("data.txt", "fasta"):
    gcCont = (seq_record.seq.count("G") + seq_record.seq.count("C")) / len(seq_record.seq) *100
    gcContCompilation[seq_record.id] = gcCont

for seqid, gc in gcContCompilation.items():
    if gc > highestGC:
        highestGC = gc

for seqid, gc in gcContCompilation.items():    
    if gc == highestGC:
        print(seqid)
        print(gc)
    