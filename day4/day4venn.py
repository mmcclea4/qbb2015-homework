#!/usr/bin/env python

"""
Count intersection of three BED files
"""

from __future__ import division

import sys
import numpy
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

def arrays_from_len_file( fname ):
    arrays = {}
    for line in open( fname ):
        fields = line.split()
        name = fields[0]
        size = int( fields[1] )
        arrays[name] = numpy.zeros( size, dtype=bool )
    return arrays
    
def set_bits_from_file( arrays, fname):
    temparr = arrays
    for line in open(fname):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        temparr[ chrom ][ start : end ] = 1
    return temparr

arrC = arrays_from_len_file( sys.argv[1] )
arrB = arrays_from_len_file( sys.argv[1] )
arrS = arrays_from_len_file( sys.argv[1] )
CTCF = set_bits_from_file( arrC, sys.argv[2] ) 
BEAF = set_bits_from_file( arrB, sys.argv[3] )
SuHW = set_bits_from_file( arrS, sys.argv[4] )


any_overlapC = 0
any_overlapB = 0
any_overlapS = 0
any_overlapCB = 0
any_overlapBS = 0
any_overlapSC = 0
any_overlapCBS = 0

for filename in sys.argv[2:]:
    for line in open( filename ):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        # Get slice
        slC = CTCF[ chrom ][ start : end ]
        slB = BEAF[ chrom ][ start : end ]
        slS = SuHW[ chrom ][ start : end ]
        # .any increments the count if a true vaue is encountered
        if slC.any() & ~slB.any() & ~slS.any():
            any_overlapC += 1
        if ~slC.any() & slB.any() & ~slS.any():
            any_overlapB += 1
        if ~slC.any() & ~slB.any() & slS.any():
            any_overlapS += 1
        if slC.any() & slB.any() & ~slS.any():
            any_overlapCB += 1
        if ~slC.any() & slB.any() & slS.any():
            any_overlapBS += 1
        if slC.any() & ~slB.any() & slS.any():
            any_overlapSC += 1
        if slC.any() & slB.any() & slS.any():
            any_overlapCBS += 1
            
print "Overlap CTCF: %d" % (any_overlapC)
print "Overlap BEAF: %d" % (any_overlapB)
print "Overlap SuHW: %d" % (any_overlapS)
print "Overlap between CTCF and BEAF: %d" % (any_overlapCB)
print "Overlap between BEAF and SuHW: %d" % (any_overlapBS)
print "Overlap between SuHW and CTCF: %d" % (any_overlapSC)
print "Overlap between CTCF, BEAF, and SuHW: %d" % (any_overlapCBS)

plt.figure()
venn3(subsets = (any_overlapC, any_overlapB, any_overlapCB, any_overlapS, any_overlapSC, any_overlapBS, any_overlapCBS), set_labels = ('CTCF', 'BEAF', 'SuHW'))
plt.savefig("day4venn.png")
#plt.show()
