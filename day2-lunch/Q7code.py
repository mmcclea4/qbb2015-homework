#!/usr/bin/env python

# Counts number of reads that start their alignment on chromosome 2L between base 10000 and 20000 in SRR072893.sam

filename = "/Users/cmdb/qbb2015/day2/SRR072893.sam"

f = open( filename )

LINE_COUNT = 0

for line in f:
    fields = line.split()
    if "@" == line[0]:    # Skips the header lines
        pass
    if fields[2] == "2L" and 10000 <= int(fields[3]) <= 20000: # finds alighnemts along chromosome 2L whose left-most position begins between 10000 and 20000
        LINE_COUNT += 1
    else:
        pass
        
print LINE_COUNT
       