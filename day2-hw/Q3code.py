#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"


df = pd.read_csv(annotation)
#df.columns = ["sample", "sex", "stage"]

#print df

for sample in df["sample"]:    
    tab = open("/Users/cmdb/qbb2015/stringtie/" + sample + "/t_data.ctab")
    for row in tab:
        if "FBtr0331261" in row:
            print row,