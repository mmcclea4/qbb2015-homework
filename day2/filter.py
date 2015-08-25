#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )


# Iterate the file line by line
for line_count, line in enumerate(f):
    # enumerate serves as the counter by creating line_count which increments up one for each consecutive line
    if line_count <= 10:
        pass 
    elif line_count <= 15:
        print line, 
    else:
        break
        # Stops the program from continuing to read every consecutive line past 15
        
        
   
   
   
   
   
   
    #fields = line.split()
    # x.split() tells the code to looks for the tabbed columns (must specify the column you want below)   
    #if "tRNA" in fields[9]:
        # looks for tRNA in the field specific for gene name in data, and prints those lines
     #   print line, 
        # the comma suppresses the new line automatically added after each print function, needed beacuse in this instance the file itself includes new lines
