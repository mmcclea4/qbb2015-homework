#!/usr/bin/env python

# Counting the number of alignments in SRR072893.sam

filename = "/Users/cmdb/qbb2015/day2/SRR072893.sam"

f = open( filename )

LINE_COUNT = 0

for line in f:
    if "@SQ" in line:
        pass
    else:
        LINE_COUNT += 1
print LINE_COUNT
    
    
    
    
