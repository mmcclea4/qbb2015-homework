#!/usr/bin/env python

# Calculating the avg MAPQ score in SRR072893.sam

filename = "/Users/cmdb/qbb2015/day2/SRR072893.sam"

f = open( filename )

LINE_COUNT = 0
total_iMAPQ = 0
for line in f:
    fields = line.split()
    if "@" == line[0]:    # Skips the header lines
       pass
    else:
        MAPQ = fields[4]
        iMAPQ = int(MAPQ) # converts MAPQ to integer
        LINE_COUNT += 1
        total_iMAPQ += iMAPQ
average_MAPQ = total_iMAPQ / LINE_COUNT
print average_MAPQ
        