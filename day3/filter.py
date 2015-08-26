#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

import sys

# Open using arguments:

#print sys.argv
#filename = sys.argv[1]

#f = open( filename )

f = sys.stdin

name_counts = {}
#a dictionary with function specified below

# Iterate the file line by line
for line_count, line in enumerate(f):
    fields = line.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts[ gene_name ] = 1
    else:
        name_counts[ gene_name ] += 1
        
# Iterate key, value pairs from the name_counts dictionary
for key, value in name_counts.iteritems():
    # Print gene name and count
    print key, value
        
        
   
  
