from Bio import SeqUtils
import sys


def openFile(file):
    s, t = "", ""
    with open(file) as fh:
        fh = fh.read()
        s, t = fh.split("\n")
    return s, t

s, t = openFile((sys.argv[1]))

result = SeqUtils.nt_search(s, t)[1::]

newResults = []
for i in result:
    newResults.append(i+1)


print(*newResults)