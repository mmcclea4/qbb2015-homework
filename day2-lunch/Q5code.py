#!/usr/bin/env python

# Printing the columns indicating the chromosome the read maps to, for 10 alignments only, in SRR072893.sam

filename = "/Users/cmdb/qbb2015/day2/SRR072893.sam"

f = open( filename )

LINE_COUNT = 0

chromosome = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0}

for line in f:
    fields = line.split()
    chromosome_mapped = fields[2]
    # Skips the header lines
    if "@" in line:
       pass
    if chromosome_mapped in chromosome:
        chromosome[chromosome_mapped] += 1
        
print "Chromosome 2L", chromosome["2L"]
print "Chromosome 2R", chromosome["2R"]
print "Chromosome 3L", chromosome["3L"]
print "Chromosome 3R", chromosome["3R"]
print "Chromosome 4", chromosome["4"]
print "Chromosome X", chromosome["X"]
 