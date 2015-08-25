#!/usr/bin/env python

# Printing the columns indicating the chromosome the read maps to, for 10 alignments only, in SRR072893.sam

filename = "/Users/cmdb/qbb2015/day2/SRR072893.sam"

f = open( filename )

LINE_COUNT = 0

for line in f:
    fields = line.split()
    chromosome_mapped = fields[2]
    if "@" in line:
       pass
    else:
        if LINE_COUNT <= 10:
            LINE_COUNT += 1
            print fields[2]
     
