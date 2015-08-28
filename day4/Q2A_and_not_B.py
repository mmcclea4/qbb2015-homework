#!/usr/bin/env python

"""
Read A but not B, create tuple list by extending chrombits class
"""

from __future__ import division

import sys

import chrombits

arr = chrombits.ChromosomeLocationBitArrays( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )

AnotB = beaf.intersect( ctcf.complement() )
regions = AnotB.create_intervals()

print regions 