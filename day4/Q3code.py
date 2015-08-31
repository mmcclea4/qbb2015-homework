#!/usr/bin/env python

"""
Create intervals and venn diagram from the union of CTCF, BEAF, and SuHW 
"""

from __future__ import division

import sys
import numpy
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

import chrombits_extended

# argv[1] = dm3.len
# argv[2] = DM3_Kc_CTCF.bed
# argv[3] = DM3_Kc_BEAF.bed
# argv[4] = DM3_Kc_SuHW.bed

arr = chrombits_extended.ChromosomeLocationBitArrays( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()
suhw = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )
suhw.set_bits_from_file( sys.argv[4] )

combination = ctcf.union( beaf.union( suhw ) )
#beaf.intersect( ctcf.complement() )
#bedTables[0].union(bedTables[1]).union(bedTables[2]
intervals = combination.create_intervals()
#print intervals
