#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)

#print df.info()
    #gives more data about table

#print df.describe()
    #gives additional information about the table

#print df.head()
    #prints shortened version

#print df
    # Prints data table in full
    
#print df[1:5]
    #prints rows 1,2,3,4 (end number isn't inclusive)
    
#print "\n notes (on a separate line) by including them with annotation"

#EX show rows 10 through 15 (1-based, inclusive)
#print df [9:15]


df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]
    # lets us update columns to have descriptive names
#print df.info
    #shows the updated column names

#print df.sort("type")
    #find different sort options via google
    #either enter options in order, or name each option with xx = xx - code wil     throw error if the option are not named and out of order as seen online
    
#print df["chromosome"]

# want to subset chromosome, start, and end
    #print df[["chromosome", "start", "end"]]
        #must specify that the terms are part of an earlier list - done with the extra set of brackets
        
# want to subset by rown and column
    #print df["start"][9:15]
        # order (row vs. column) doesn't matter
 
#print df.shape       
#df2 = df["start"]
#print df2.shape

# to save output to new file
#df2.to_csv("startColumn.txt", sep='\t', index=False)

# want to find features in annotation file whose start value is less than 10
roi = df["start"] < 10
print df[roi]
#print type(roi)
    # will tell you the type of data output - can then google for info
    


