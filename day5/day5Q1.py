#!/usr/bin/env python

import sys

"""
Using Blast alignments - print the sequence name, ratio of identities, and ratio of gaps
"""

# argv = subset_refMrna_aligned.txt

alignment = []

for line in open(sys.argv[1]):

    if line.startswith( ">" ):
        sequence_name = line[1:].rstrip( "\r\n" )
    if line.startswith( " I" ):
        if "Identities" in line:
            identities = line.split()[2]
        if "Gap" in line:
            gap = line.split()[6]
            alignment.append([sequence_name, identities, gap ])

print alignment
