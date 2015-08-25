#!/usr/bin/env python

# Counting the number of alignments that match perfectly in SRR072893.sam

filename = "/Users/cmdb/qbb2015/day2/SRR072893.sam"

f = open( filename )

LINE_COUNT = 0

for line in f:
    if "NM:i:0" in line:
        LINE_COUNT += 1
print LINE_COUNT
