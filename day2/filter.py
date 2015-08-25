#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

for line in f:
    fields = line.split()
    # x.split() tells the code to looks for the tabbed columns (must specify the column you want below)   
    if "tRNA" in fields[9]:
        # looks for tRNA in the field specific for gene name in data, and prints those lines
        print line, 
        # the comma suppresses the new line automatically added after each print function, needed beacuse in this instance the file itself includes new lines
